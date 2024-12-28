import sys
import os
import time

def check_work_on_exe():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('PyInstallerのバンドルで動作している')
        return True
    else:
        print('Pythonプロセスで動作している')
        return False

def check_current_directory():
    current_dir = os.getcwd()
    print(f"コードを実行しているパス: {current_dir}")


def check_directory():

    is_work_on_exe = check_work_on_exe()

    if is_work_on_exe:

        temp_dir = sys._MEIPASS
        print(f"Temporary directory (_MEIPASS): {temp_dir}")

        # 上記ディレクトリへのアクセス権確認
        if not os.access(temp_dir, os.R_OK):
            print("Error: Cannot read the temporary directory (_MEIPASS).")
        else:
            print("Temporary directory (_MEIPASS) is accessible.")
        time.sleep(1)

        # ディレクトリの中に格納されているファイルの確認
        items = os.listdir(temp_dir)
        print(f"Contents of '{os.path.abspath(temp_dir)}':")
        for item in items:
            print(f"- {item}")
        time.sleep(1)


def read_file_from_exe(filename):

    # ディレクトリが存在するか確認
    is_work_on_exe = check_work_on_exe()
    if is_work_on_exe:
        temp_dir = sys._MEIPASS
        file_on_temp_path = os.path.join(temp_dir, filename)

        # ファイルが存在しているか確認
        if os.path.exists(file_on_temp_path):
            print("ファイルは存在している")

            # ファイルへのアクセス許可があるか確認
            if os.access(file_on_temp_path, os.R_OK):
                print("ファイルへのアクセスが許可されています。")
                print(f"ファイルパス: {file_on_temp_path}")
                return file_on_temp_path
            else:
                print("ファイルへのアクセスが拒否されています。")
                print(f"ファイルパス: {filename}")
                return filename

    else:
        print("ファイルは存在しない")
        print(f"ファイルパス: {filename}")
        return filename
