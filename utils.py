import sqlite3
import newspaper
from newspaper import Article

def get_all(query):
    conn = sqlite3.connect('DATA/NewsDB.db')
    data = conn.execute(query).fetchall()
    conn.close()
    return data

def add_news(conn, url, cat_id):
    query = """
        INSERT INTO news (tieude, noidung, hinhanh, linkgoc, cat_id)
        VALUES (?, ?, ?, ?, ?)
    """

    article = Article(url)
    article.download()
    article.parse()

    conn.execute(query, (article.title, article.text, article.top_image, article.url, cat_id))
    conn.commit()

def get_news_url():
    cats = get_all("SELECT * FROM category")
    conn = sqlite3.connect('DATA/NewsDB.db')
    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        papers = newspaper.build(url)
        for article in papers.articles:
            try:
                print("========", article.url)
                add_news(conn, article.url, cat_id)
            except Exception as ex:
                print("ERROR" + str(ex))
                pass
    conn.close()

if __name__ == '__main__':
    get_news_url()