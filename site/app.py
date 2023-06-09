from curlify2 import curlify
from flask import Flask, render_template, request, redirect, flash, url_for
import httpx

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"


@app.get("/")
def index():
    return render_template("index.html", command="")


@app.post("/convert_to_curl")
def convert_to_curl():
    url = request.form.get("url", "https://google.com")

    if not url:
        flash("You need to pass the url in the field")
        return redirect(url_for(".index"))

    response = httpx.get(url)
    command = curlify.to_curl(response.request)

    return render_template("index.html", command=command)


app.run(debug=True)
