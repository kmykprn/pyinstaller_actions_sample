# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import io

# 標準出力をUTF-8に設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_app_local():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('PyInstallerのバンドルで動作している')
    else:
        print('Pythonプロセスで動作している')

def check_current_directory():
    current_dir = os.getcwd()
    print(f"コードを実行しているパス: {current_dir}")

def display_directory_tree(path, prefix=""):
    """
    指定したディレクトリ配下の構造をツリー形式で表示する関数。
    """
    files = []
    directories = []
    
    # ディレクトリ内のファイルとディレクトリを分けて取得
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)
    
    # ディレクトリを先に表示
    for i, directory in enumerate(directories):
        connector = "├── " if i < len(directories) - 1 or files else "└── "
        print(f"{prefix}{connector}{directory}/")
        new_prefix = f"{prefix}│   " if i < len(directories) - 1 or files else f"{prefix}    "
        display_directory_tree(os.path.join(path, directory), new_prefix)
    
    # ファイルを表示
    for i, file in enumerate(files):
        connector = "└── " if i == len(files) - 1 else "├── "
        print(f"{prefix}{connector}{file}")

print("*********************************************")

# exe上で実行されているかをチェック
check_app_local()

# カレントディレクトリを表示
check_current_directory()

# 現在のディレクトリのツリーを表示
current_dir = os.getcwd()
print(f"Directory tree for: {current_dir}\n")
display_directory_tree(current_dir)
print("*********************************************")


a = Analysis(
    ['src/read_toml.py'],                     # specファイルの位置を基準とした相対パスを指定 
    pathex=["."],                    # sys.pathにパスを追加
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

