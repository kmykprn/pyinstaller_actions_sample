import sys

def check_app_local():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('PyInstallerのバンドルで動作している')
    else:
        print('Pythonプロセスで動作している')