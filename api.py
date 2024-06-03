from flask import Flask, jsonify, render_template, request
import utils
import render_templates
import json

app = Flask(__name__)

ITEMS_PER_PAGE = 10

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/category', methods=['GET'])
def get_categories():
    rows = utils.get_all("SELECT * FROM category")
    data = []
    for r in rows:
        data.append(
            { 'id': r[0], 
             'name': r[1], 
             'url': r[2]
            }
        )
    with open("json_file/category.json", "w", encoding="utf8") as f:
        json.dump(data, f)

    return render_template("category.html", data=data)

@app.route('/news', methods=['GET'])
def render_news():
    kw = request.args.get("keywords", None)
    page = int(request.args.get("page", 1))
    data, total_pages = render_templates.read_news(kw, page, ITEMS_PER_PAGE)
    return render_template('news.html', data=data, page=page, total_pages=total_pages, keywords=kw)

if __name__ == '__main__':
    app.run(debug=True)
