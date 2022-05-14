from flask import Flask

from .views.top_page import top_page_views
from .views.second_page import second_page_views

def create_app() -> Flask:
    app = Flask(__name__)
    
    # view定義
    # /
    app.register_blueprint(top_page_views, url_prefix='/')
    # /sec
    app.register_blueprint(second_page_views, url_prefix='/sec/<string:id1>')
    
    return app
