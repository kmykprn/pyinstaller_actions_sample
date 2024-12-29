from mypackage.__main__ import main
import tomli
import time
from check_debug import read_file_from_exe

# 自作パッケージを読み込んでhello_worldを印字
main()

# TOML ファイルを読み込んで中身を印字
filename = "config.toml"
try:
    with open(read_file_from_exe(filename), "rb") as f:
        config = tomli.load(f)
        print(config)
except Exception as e:
    print(f"error: {e}")

time.sleep(1)