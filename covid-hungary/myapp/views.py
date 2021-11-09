from flask import Blueprint, render_template
from gnews.utils.utils import country_mapping
import requests
from gnews import GNews

pages = Blueprint(url_prefix="/", name="pages", import_name="pages")
news = GNews(language="hu", country="Hungary", period="7d", max_results=30)

@pages.get("/")
def index():
    data_request = requests.get("https://covid2019-api.herokuapp.com/v2/country/hungary", headers={"accept": "application/json"})
    covid_data = data_request.json()

    covid_news = news.get_news(key="koronavírus covid covid19 koronavirus virus magyar")
    return render_template("index.html", covid_data=covid_data, covid_news=covid_news)