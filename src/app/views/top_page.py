"""
top_page.py

"""
from flask import Blueprint, render_template, redirect, url_for


top_page_views = Blueprint('top_pv', __name__)

@top_page_views.route('/', methods=['GET'])
def top_page() -> str:
    """トップページ
    
    Returns:
        str: トップページ
    """
    return render_template(
        'top_page/top1.html'
    )


@top_page_views.route('/sample1', methods=['GET'])
def top_page_sample1() -> str:
    """トップへ飛ばすサンプル
    
    Returns:
        str: トップページ
    """
    return redirect(url_for('top_pv.top_page'))
