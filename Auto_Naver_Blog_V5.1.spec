# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

# imageio와 moviepy 관련 데이터 파일 수집
imageio_datas = collect_data_files('imageio', include_py_files=True)
imageio_ffmpeg_datas = collect_data_files('imageio_ffmpeg', include_py_files=True)
moviepy_datas = collect_data_files('moviepy', include_py_files=True)

# 메타데이터 수집 (importlib.metadata를 위해 필수)
imageio_metadata = copy_metadata('imageio')
imageio_ffmpeg_metadata = copy_metadata('imageio-ffmpeg')
moviepy_metadata = copy_metadata('moviepy')
numpy_metadata = copy_metadata('numpy')
decorator_metadata = copy_metadata('decorator')

# imageio 관련 모든 하위 모듈 수집
imageio_hidden = collect_submodules('imageio')
imageio_ffmpeg_hidden = collect_submodules('imageio_ffmpeg')
moviepy_hidden = collect_submodules('moviepy')

# Python DLL 포함 (일부 환경에서 누락되는 경우가 있어 명시)
python_dlls = []
for dll_name in ("python313.dll", "python3.dll"):
    dll_path = os.path.join(sys.base_prefix, dll_name)
    if os.path.exists(dll_path):
        python_dlls.append((dll_path, "."))

a = Analysis(
    ['Auto_Naver_Blog_V5.1.py'],
    pathex=[],
    binaries=python_dlls,
    datas=[
        ('setting/etc/david153.ico', 'setting/etc')
    ] + imageio_datas + imageio_ffmpeg_datas + moviepy_datas + imageio_metadata + imageio_ffmpeg_metadata + moviepy_metadata + numpy_metadata + decorator_metadata,
    hiddenimports=[
        'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets', 'PyQt6.sip',
        'license_check',
        'moviepy', 'moviepy.video.io.VideoFileClip', 'moviepy.video.VideoClip',
        'moviepy.video.fx.all', 'moviepy.audio.fx.all',
        'imageio', 'imageio.plugins', 'imageio.plugins.ffmpeg',
        'imageio_ffmpeg', 'imageio_ffmpeg.binaries',
        'numpy', 'decorator', 'proglog', 'tqdm'
    ] + imageio_hidden + imageio_ffmpeg_hidden + moviepy_hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'tkinter', 'matplotlib'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Auto_Naver_Blog_V5.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['setting\\etc\\david153.ico'],
)
