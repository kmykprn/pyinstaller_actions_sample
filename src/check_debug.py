import sys
import os

def check_app_local():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('PyInstallerのバンドルで動作している')
    else:
        print('Pythonプロセスで動作している')

def check_current_directory():
    current_dir = os.getcwd()
    print(f"コードを実行しているパス: {current_dir}")