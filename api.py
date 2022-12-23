import requests

api_token = #your_token
url = "https://openai35.p.rapidapi.com/createImage"


def get_pic(req):
    payload = {"prompt": req}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_token,
        "X-RapidAPI-Host": "openai35.p.rapidapi.com"
    }
    res = requests.request("POST", url, json=payload, headers=headers)
    return res.text