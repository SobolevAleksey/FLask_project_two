from flask import render_template, Blueprint, request, current_app, logging
from main.utils import PostsHandler
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    substr = request.args.get('s')
    logging.info(f"Поиск{substr}")
    post_handler = PostsHandler(current_app.config['POST_PATH'])
    posts = post_handler.search_posts(substr)

    return render_template('post_list.html', posts=posts, substr=substr)
