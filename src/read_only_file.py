# nuitka actionsで、単体のファイルを読み込んでexe化したときに実行できるか？を確認する
import time

try:
    print("hello_world")
except Exception as e:
    print(e)

time.sleep(5) # 5秒待機