import json

import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route("/hotWords", methods=["GET"])
def hot_words():
    url = "https://trendinsight.oceanengine.com/arithmetic-index?source=oceanengine"
    resp = requests.get(url)
    # print(resp.content)
    # return
    soup = BeautifulSoup(resp.content, features="html.parser")
    # print(soup)
    # return
    wordList = []
    for script in soup.find_all("script"):
        text = str(script.get_text())
        if "window._SSR_DATA" in text:
            j = json.loads(text[len("window._SSR_DATA = ") :])
            key = ""
            for item in j["data"]["loadersData"]:
                if item != "":
                    key = item
            for item in j["data"]["loadersData"][key]["data"]["current"]:
                # print(item)
                wordList.append(item)

    return wordList
