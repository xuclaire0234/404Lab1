# import requests;
# print(requests.get("https://www.google.com").text)
# print(requests.__version__)

import requests
url = "https://raw.githubusercontent.com/xuclaire0234/404Lab1/main/find.py"
resp = requests.get(url)
print(resp.text)

