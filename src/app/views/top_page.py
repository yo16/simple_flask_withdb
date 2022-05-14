"""
top_page.py

"""
from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import Session, User

top_page_views = Blueprint('top_pv', __name__)

@top_page_views.route('/', methods=['GET','POST'])
def top_page() -> str:
    """トップページ
    
    Returns:
        str: トップページ
    """
    # Select
    with Session() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        print(users)
    
    return render_template(
        'top_page/top1.html',
        users=users
    )


@top_page_views.route('/sample1', methods=['GET'])
def top_page_sample1() -> str:
    """トップへ飛ばすサンプル
    
    Returns:
        str: トップページ
    """
    return redirect(url_for('top_pv.top_page'))


@top_page_views.route('/create_user', methods=['POST'])
def create_user() -> str:
    """ユーザーを作ってトップページを表示する

    Returns:
        str: トップページ
    """
    # ユーザーを作成する
    user_id = request.form['user_id']
    user_name = request.form['user_name']
    user_age = request.form['user_age']
    user_email = request.form['user_email']
    try:
        user_id_i = int(user_id)
    except:
        user_id_i = None
    try:
        user_age_i = int(user_age)
    except:
        user_age_i = None
    # エラーハンドリングはほんとはもっとちゃんとやる！
    
    print(f'user: ({user_id},{user_name},{user_age},{user_email})')
    new_user = User(id=user_id_i, name=user_name, age=user_age_i, email=user_email)
    
    # Insert
    with Session() as session:
        session.add(new_user)
        session.commit()
    
    return redirect(url_for('top_pv.top_page'))