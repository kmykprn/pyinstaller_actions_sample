import sys
import os
import time

def check_work_on_exe():

    # exeファイル上で動作しているかを確認
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('PyInstallerのバンドルで動作している')
        return True
    else:
        print('Pythonプロセスで動作している')
        return False


def check_datas_imported():
    """
    必要なデータがexeに梱包されたかを確認する。
    """

    # exeファイル上で動作しているかを確認
    is_work_on_exe = check_work_on_exe()
    if is_work_on_exe:

        # sys._MEIPASSはexeを実行したときに展開されるディレクトリ。
        # specファイルで指定したdatasの値などがここに展開され、参照される。
        temp_dir = sys._MEIPASS
        print(f"Temporary directory (_MEIPASS): {temp_dir}")

        # ディレクトリの中に格納されているファイルの可視化
        items = os.listdir(temp_dir)
        print(f"Contents of '{os.path.abspath(temp_dir)}':")
        for item in items:
            print(f"- {item}")
        time.sleep(3)

def read_file_from_exe(filename):

    is_work_on_exe = check_work_on_exe()
    if is_work_on_exe:

        # exe実行時に一時的に展開されるディレクトリからファイルを参照
        temp_dir = sys._MEIPASS
        file_on_temp_path = os.path.join(temp_dir, filename)

        if os.path.exists(file_on_temp_path):
            return file_on_temp_path
        else:
            print(f"エラー: ファイルが存在しません: {filename}")
            sys.exit(1)  # プログラムを終了 (終了コード 1 はエラーを意味します)

    else:
        print("exe上で動作してません。ローカルからコードを読み込みます。")
        return filename