# 元となるdockerイメージを指定
FROM python:3.7-alpine

#プロジェクトの管理者を記載
LABEL maintainer = "Keita Ide <keita.ide78dev@gmail.com>"

# 標準出力に出力されるバッファを無効化
ENV PYTHONUNBUFFERED 1

# txtファイルをイメージ側のappディレクトリに配置
COPY ./requirements.txt /requirements.txt

# ローカルのapp配下のファイルをイメージ側のapp配下にコピー
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# "user"ユーザを作成し実行ユーザを変更する
RUN adduser -D user
USER user