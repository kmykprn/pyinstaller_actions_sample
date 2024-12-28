# pyinstaller_actions_sample
pyinstaller＋Github Actionsを使ってコードをexeに変換するサンプルコード

## pyinstallerの基本的な使い方（ターミナル上）
- 事前にpoetryをインストールしておく
- poetry installを実行し、必要なライブラリをインストール
- `poetry run pyinstaller src/read_only_file.py`で、distディレクトリが作成され、exeファイルが作成される

## pyinstaller + Github Actionsの基本的な使い方
### Github Actionsを実行するための準備
- .github/workflowsディレクトリを作成
- yamlファイルを作成（参照. .github/workflows/pyinstaller_read_only_file.yaml）
- githubにpushする
- Githubの「Actions」タブ上で、Workflowが動いていることを確認する。

## Pyinstaller系情報
### 公式ドキュメント
- https://pyinstaller.org/en/stable/index.html

### exeファイルの実行結果をコマンドラインで表示するオプション
- `--console`を使用する
  - https://pyinstaller.org/en/stable/usage.html#cmdoption-w

### Pyinstaller Actions
- https://github.com/marketplace/actions/pyinstaller-action
- yaml本体：https://github.com/Martin005/pyinstaller-action/blob/main/action.yml

## Github Actions系情報
### runners onで指定できる変数（windows-latestなど）
- https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners



## 依存関係を読み込むには？
- 方法は2つ
  - コマンドラインで指定する
  - .specファイルを作成する

### specファイルの概要
- specファイルだけ作成する
  - コマンド例：
    - poetry run pyi-makespec src/read_mypackage.py --specpath spec/

- 手動設定が必要そうな項目
  - pathex: 
    - モジュールやパッケージをインポートを検索するパスのリスト(PYTHONPATH)。
    - コマンドラインから--pathsで指定した場合と同様。
  - pure:
    - メインスクリプト名.py
  - biranies:
    - pythonファイル以外のバイナリファイル
    - コマンドラインから--add-binaryで指定した場合と同様。
  - datas:
    - pythonファイル以外の非バイナリファイル
    - コマンドラインから--add-dataで指定した場合と同様。

- pyinstallerにおけるバンドルとは：
  - exeファイルや、必要なデータを一つのディレクトリにまとめることを指す(one-folderモード)
  - 参考：

- 参考：
  - https://pyinstaller.org/en/stable/spec-files.html#using-spec-files
  - https://pyinstaller.org/en/stable/operating-mode.html#bundling-to-one-folder


## specファイル上のパス設定のポイント
- **カレントディレクトリ**を基準として、他のパッケージやデータを相対パスを指定する。
- Github Actionsにおいて、カレントディレクトリはプロジェクトのルートに設定されている。
  - 具体例：
    - パス構成が以下のとき、カレントディレクトリは```myproject```になる
    - config.tomlをexeファイルに組み込むには、specファイルに```datas=[('config.toml', 'config.toml')]```を指定する
  ```
  |-- myproject
  |    |-- src
  |    |   |-- main.py
  |    |-- spec
  |    |   |-- myspec.spec
  |    |-- config.toml
  ```
  - 解説：
    - ```('config.toml', 'config.toml')```の1項目は、**カレントディレクトリを基準**にした相対パスを指定する。
    - 2項目は、基本は1項目と同じでＯＫ。パスを変えたい場合だけ指定する。

- exe化まで極力ミスを減らすためのステップ
  - ステップ1. ローカルのpythonでアプリを実行し、エラーが出ないことを確認する
    - **プロジェクトのルートの位置（例. myproject/）に移動する**
    - pythonコマンドで直接アプリケーションを実行し、エラーがでないことを確認
  - ステップ2. ローカルでpyinstallerを使ってアプリをexe化し、exeを実行してエラーが出ないことを確認
  - ステップ3. github actionsでexe化し、exeを実行してエラーがでないことを確認


## pyproject.tomlからrequiremets.txtを生成する
- [tool.poetry.dependencies]に記述しているもののみ出力させる場合
  - ```poetry export -f requirements.txt -o requirements.txt --without-hashes```
- [tool.poetry.group.dev.dependencies]のものを含める場合
  - ```poetry export -f requirements.txt -o requirements.txt --without-hashes --with dev```
- 参考：https://qiita.com/gabe-ds/items/d45f6c9ed497f40f6f49