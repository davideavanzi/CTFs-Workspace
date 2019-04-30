
import base64
from urllib.parse import unquote


cookie = """MzY5M2NmNDY1MTQ5ZDNiODgyZDMzZDkzYTQzY2IwOTlmOWY3ZmYzYmFiZTQ0OTIxMjdlNWY5N2FlOWU5NDZlMTcxOTgwMjRkNDkyOGFhN2M3NDE3ZTUwNzJkMjIwMGZmNmE2ZjlhNWU3YzYxMmY3Y2Y0YjA3Y2M0ZWViZWU4MzE%3D%3ATzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjU6ImRhZGRhIjtzOjQ6InJvbGUiO3M6NDoidXNlciI7fQ%3D%3D"""

print("[Cookie] %s"%cookie)

url_decoded = unquote(cookie) 

print("[Url Decoded] %s"%url_decoded)

print("#"*30)

parts = url_decoded.split(":")

_hash = base64.b64decode(parts[0])

print("[Hash] %s"%_hash)

decoded = base64.b64decode(parts[1])

print("[Serialized] %s"%decoded)