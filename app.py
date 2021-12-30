from pprint import pprint

from flask import Flask, request, render_template, send_from_directory
import functions

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
read_method = ["r", "w", "a"]
app = Flask(__name__)

app_json = functions.load_file(POST_PATH, read_method[0], "utf-8")





@app.route("/")
def page_index():
    s = functions.index_tag(app_json)

    return render_template("index.html")


@app.route("/tag")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

