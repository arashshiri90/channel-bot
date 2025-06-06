from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)

@app.route('/')
def index():
    with open("bot/content.json", encoding="utf-8") as f:
        content = json.load(f)
    return render_template("index.html", items=content)

@app.route('/edit/<item_id>', methods=["GET", "POST"])
def edit(item_id):
    with open("bot/content.json", encoding="utf-8") as f:
        content = json.load(f)
    item = next((x for x in content if x["id"] == item_id), None)
    if request.method == "POST":
        item["body"] = request.form.get("body")
        with open("bot/content.json", "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        return redirect("/")
    return render_template("edit.html", item=item)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
