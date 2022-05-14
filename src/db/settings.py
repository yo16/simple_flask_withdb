import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = None
Session = None

def settings(database_url:str, encoding='utf-8', print_sql:bool=False):
    '''初期設定
    '''
    global Base
    global Session
    
    Base = declarative_base()
    
    # DBの設定
    Engine = create_engine(
        url=database_url,
        encoding=encoding,
        echo=print_sql
    )
    
    # セッションを作成
    Session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=Engine
        )
    )
    
    # DB作成
    Base.metadata.create_all(Engine)


# この場で設定
db_url = os.environ.get('DB_URL', None)
assert(db_url is not None, '環境変数:DB_URLが設定されていません')
print_sql = os.environ.get('PRINT_SQL', False)
settings(db_url, print_sql=print_sql)

