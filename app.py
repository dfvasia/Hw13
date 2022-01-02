from pprint import pprint

from flask import Flask, request, render_template, send_from_directory, abort, url_for
from functions import index_tag, list_tag, load_file, add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
read_method = ["r", "w", "a"]
app = Flask(__name__)

all_posts = load_file(POST_PATH, read_method[0], "utf-8")
index_tag_1 = index_tag(all_posts)


@app.route("/")
def page_index():
    s = list_tag(index_tag_1)
    return render_template("index.html", s=s)


@app.route("/tag/")
def page_tag():
    found_tags = []
    found_tag = request.args.get("tag")
    if not found_tag:
        abort(400)
    for post_list in index_tag_1:
        for post in index_tag_1[post_list]:
            if found_tag == post:
                found_tags.append(all_posts[post_list])
    return render_template("post_by_tag.html", found_tag=found_tag, found_tags=found_tags)


@app.route("/post/", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template("post_form.html")
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        abort(400)
    path = f'{UPLOAD_FOLDER}/{picture.filename}'
    post = {
        'pic': url_for('static_dir', path=picture.filename),
        'content': content
    }
    picture.save(path)
    add_post(all_posts, post, POST_PATH, read_method[1], "utf-8")
    index_tag_1.update(index_tag(load_file(POST_PATH, read_method[0], "utf-8")))
    print(index_tag_1)
    return render_template('post_uploaded.html', post=post)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)


if __name__ == "__main__":
    app.run(debug=True)

