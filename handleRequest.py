
from flask import Flask, request, render_template


@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       content = request.form.get("textBox")
       return render_template("index.html", textContent = content)
    return render_template("index.html")