# -*- mode: python ; coding: utf-8 -*-

import os

# spec ファイル自身のフルパスを取得
spec_path = os.path.abspath(SPECPATH)
print("spec_path: ", spec_path)

# プロジェクト本体のパスを取得
project_root = os.path.abspath(os.path.join(spec_path, '..'))

# メインアプリのパスを定義
app_path = os.path.join(project_root, 'src', 'read_mypackage.py')

# 依存関係のパスを定義
mypackage_path = os.path.join(project_root, 'mypackage')

a = Analysis(
    [app_path],
    pathex=[project_root, mypackage_path], # プロジェクト本体のパスも忘れずに格納すること！
    binaries=[],
    datas=[],
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
    [],
    exclude_binaries=True,
    name='read_mypackage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='read_mypackage',
)
