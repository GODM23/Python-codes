import jwt
import json
from collections import OrderedDict

# Step 1: Create header manually to preserve field order
header = {
    "alg": "HS256",
    "typ": "JWT"
}

# Step 2: Define your payload as OrderedDict to maintain key order
payload = OrderedDict({
    "req": [
        OrderedDict({
            "MerReffNo": "TRANSC206500",
            "AccountID": "403403403"
        })
    ]
})

# Step 3: Use your exact secret (not base64)
secret_key = "4c8d6e9a2b4c1d2e8f7a3b1c9d4f0e1b2d3c4a5f6e7b8a1c3d2e4f5b6a7c8d9"  # Replace this

# Step 4: Convert header & payload to compact JSON (no spaces)
header_json = json.dumps(header, separators=(",", ":"))
payload_json = json.dumps(payload, separators=(",", ":"))

# Step 5: Encode manually
token = jwt.encode(
    payload=json.loads(payload_json),
    key=secret_key,
    algorithm="HS256",
    headers=json.loads(header_json)
)

# PyJWT returns different types depending on version
# In PyJWT >= 2.0, it returns a string; before that, it returns bytes
if isinstance(token, bytes):
    token = token.decode('utf-8')

print("Exact JWT Token:")
print(token)
print("This file has been updated just now")
print("AGAIN UPDATED v2");
