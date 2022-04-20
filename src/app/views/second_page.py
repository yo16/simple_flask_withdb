"""
second_page.py

"""
from flask import Blueprint, render_template, redirect, url_for


second_page_views = Blueprint('second_pv', __name__)

@second_page_views.route('/', methods=['GET'])
def second_page(id1:str=None) -> str:
    """secondページ
    
    Returns:
        str: secondページ
    """
    return render_template(
        'second_page/top2.html',
        id1=id1
    )

