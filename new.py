import jwt  # Make sure to install PyJWT via `pip install PyJWT`

# Define your payload
payload = {
    "req": [
        {
            "MerReffNo": "TRANSC206500",
            "AccountID": "403403403"
        }
    ]
}

# Insert your plain (non-base64) secret key here
secret_key = "4c8d6e9a2b4c1d2e8f7a3b1c9d4f0e1b2d3c4a5f6e7b8a1c3d2e4f5b6a7c8d9"  # Replace this with your actual secret

# Encode the payload using HS256 algorithm
token = jwt.encode(payload, secret_key, algorithm="HS256")

print("JWT Token:")
print(token)
