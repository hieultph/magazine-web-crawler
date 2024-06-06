# Magazine Website Crawler Using BeautifulSoup4, Newspaper, Flask, and SQLite3 Database

## About This Project

Hosted on Netlify: (Update later)

This project is a learning tool shared by me. It's not yet a perfect version, but feel free to explore and use it as a reference! The magazine data is crawled from the following sources:
- [DanTri](https://dantri.com.vn/)
- [ThanhNien](https://thanhnien.vn/)
- [TuoiTre](https://tuoitre.vn/)

## How to Use This Project

Follow these instructions to get started:

1. Clone the project using:
    ```sh
    git clone <repository-url>
    ```
2. Create a database in SQLite3.
   
   ![Database Creation](https://github.com/hieultph/magazine-web-crawler/assets/136618059/001513f6-9eef-4f36-b832-72c81b9e9dc0)
   
   Point to the `NewsDB.db` file in the `DATA` folder, or create your own with the `.db` extension.
   
   ![Database Path](https://github.com/hieultph/magazine-web-crawler/assets/136618059/75db24f9-9d8d-4ec6-833c-3bc3c781f8ba)
   
   Create these two tables: `category` and `news`.
   
   ![Tables Creation](https://github.com/hieultph/magazine-web-crawler/assets/136618059/fe6df5e3-d91f-4786-9c87-1dca2278ae80)
   
   In the `category` table, you can open the data tab and add the magazine sources you want to crawl (in this case, DanTri, ThanhNien, TuoiTre).
   
   ![Add Categories](https://github.com/hieultph/magazine-web-crawler/assets/136618059/b26707a5-7485-4c12-9aca-9d609485ee13)
   
   ![Category Data](https://github.com/hieultph/magazine-web-crawler/assets/136618059/58c8964d-4dea-4be9-b77e-798a13461637)

3. Run the `utils.py` file to start crawling data from the sources.
4. Run the `api.py` file to start the website.

That's it! Now you can customize and tweak the project as needed.

## Found a Bug?

If you find an issue or would like to suggest an improvement, please submit an issue using the [Issues](https://github.com/hieultph/magazine-web-crawler/issues) tab. If you would like to submit a pull request with a fix, reference the issue you created.

## Known Issues (Work in Progress)

Currently, there are no known issues. This section may be updated in the future.

## Like This Project?

If you find this project helpful, please give it a star and follow me for more projects in the future!
