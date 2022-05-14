# simple_flask_withdb
FlaskとSQLiteを使った基礎のFlaskApp

# DB
- sqliteを使用
- [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)でアクセス
  - [SQLAlchemyのSession生成方法](https://qiita.com/tosizo/items/86d3c60a4bb70eb1656e)
- HTTPアプリと機能を独立させるために、別モジュールとした
- 環境変数の設定が必要
  - $env:DB_URL = "sqlite:///sample_db.sqlite3"
