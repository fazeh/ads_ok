import requests
from time import sleep


def qasok (assetid):

    sleep(1) 
    url = "https://adobe.noxtools.com/downloadjpej.php"
    payload = "assetId=" + str(assetid)
    headers = {
        "authority": "adobe.noxtools.com",
        "method": "POST",
        "path": "/downloadjpej.php",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "17",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "cf_clearance=i3jp59x_uu1yXt3bvNtbZ_NlTXEjIsyPOhmwZRBr8D4-1722499040-1.0.1.1-g1G9VGtU.PNfcxfkccFTaDcOZCV8CuNPWetVEx4H8fp_XKwjPyR41rv71.Y4Y9Cr.GVy9Z5KwCcjqWlDt7v0ww; PHPSESSID=6ceb616a5fe0357729f44bd977dbb1a0; amember_nr=8ce68469e700d03f3cdb8cf37cda340c",
        "origin": "https://adobe.noxtools.com",
        "priority": "u=1, i",
        "referer": "https://adobe.noxtools.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    response = requests.post(url, data=payload, headers=headers)

    print("request is sent wait for " + '💰🤑')
    print(response.status_code)
    # print(response.content)
    print(response.text)
    type(response.content)
    type(response.text)


qasok(894475621)