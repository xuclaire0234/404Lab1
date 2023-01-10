
import requests

url = "https://raw.githubusercontent.com/xuclaire0234/404Lab1/main/find.py"
resp = requests.get(url)
with open("find.py", "r") as f:
    exec(f.read())
