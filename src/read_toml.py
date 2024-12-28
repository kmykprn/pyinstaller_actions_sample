import tomli
import time
from check_debug import check_app_local, check_current_directory

check_app_local()
check_current_directory()
"""
# TOML ファイルを読み込む
with open("./config.toml", "rb") as f:
    config = tomli.load(f)

# データを確認
print(config)
"""
time.sleep(5)
