# -*- mode: python ; coding: utf-8 -*-

import os

a = Analysis(
    ['src/read_toml.py'],                     # specファイルの位置を基準とした相対パスを指定 
    pathex=[],                                # project_rootを追加
    binaries=[],
    datas=[('config.toml', 'config.toml')],   # パス指定の方法はReadMeを参照。
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='read_toml',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

