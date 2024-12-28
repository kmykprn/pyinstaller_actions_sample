import tomli
import time
from check_debug import check_work_on_exe, check_current_directory, check_directory, read_file_from_exe

check_work_on_exe()
check_current_directory()
check_directory()

filename = "config.toml"

# TOML ファイルを読み込む
try:
    with open(read_file_from_exe(filename), "rb") as f:
        config = tomli.load(f)
        print(config)
except Exception as e:
    print(f"error: {e}")

time.sleep(5)
