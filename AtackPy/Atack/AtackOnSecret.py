import jwt
import sys
import itertools

if __name__ == "__main__":
    sample_jwt = str("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNjcwNTA1ODIzLCJleHAiOjE2NzA1OTIyMjN9.cPtNIvP7SR0mnjV0cjmw-VAcWyZdaM8MprDfKgYtgxY")
    min_length = 46
    max_length = 46
    secret_chars = "a"
    for length in range(min_length, max_length+1):
        perms = itertools.product(secret_chars, repeat = length)
        payload = jwt.decode(sample_jwt, options={"verify_signature": False})
        for secret in perms:
            encoded_jwt = jwt.encode(payload, "".join(secret), algorithm="HS256")
            print(secret)
            if encoded_jwt == sample_jwt:
                print(f"Secret found: {''.join(secret)}")
                sys.exit(1)