import bisect
import json
import random


def get_url(send_url):
    from browser import ajax

    req = ajax.Ajax()
    req.open("GET", send_url, False)
    req.set_header("content-type", "application/x-www-form-urlencoded")
    req.send()
    return req


res = get_url("/api/hotWords")
titles = json.loads(res.text)
