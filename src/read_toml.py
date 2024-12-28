import tomli
import time
from src.check_app_local import check_app_local

check_app_local()

# TOML ファイルを読み込む
with open("config.toml", "rb") as f:
    config = tomli.load(f)

# データを確認
print(config)
time.sleep(5)