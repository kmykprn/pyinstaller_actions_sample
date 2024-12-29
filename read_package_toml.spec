# -*- mode: python ; coding: utf-8 -*-

# プロジェクトのルートを基準とした、アプリの相対パスを設定
main_app_path = 'src/read_package_toml.py'

# プロジェクトのルートを基準にしたパッケージ(./mypackage)のパスを設定
pathex = []
pathex.append(".")
pathex.append("./mypackage")

# プロジェクトのルートを基準にしたデータのパスを設定
# 指定方法はReadMe.mdを参照
datas = []
datas.append(('config.toml', './'))


a = Analysis(
    [main_app_path],       # アプリのパスを追加
    pathex=pathex,         # sys.pathにパスを追加
    binaries=[],
    datas=datas,           # データのパスを追加
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
    name='read_toml',        # exeファイルの名前を設定 
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

