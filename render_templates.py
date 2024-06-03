import utils
import json
import math

def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append(
            {
                "id": r[0],
                "tieude": r[1],
                "noidung": r[2],
                "hinhanh": r[3],
                "linkgoc": r[4],
                "cat_id": r[5]
            }
        )
    with open("json_file/news.json", "w", encoding="utf8") as f:
        json.dump(data, f)

def read_news(keywords=None, page=1, items_per_page=10):
    get_news()
    with open("json_file/news.json", encoding="utf8") as f:
        news = json.load(f)
    
    if keywords is not None:
        news = [n for n in news if keywords.lower() in n["tieude"].lower()]
    
    total_items = len(news)
    total_pages = math.ceil(total_items / items_per_page)
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_news = news[start:end]
    
    return paginated_news, total_pages
