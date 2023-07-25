import jwt
from datetime import datetime, timedelta

class JWTAuthentication:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            # Handle expired token
            return None
        except jwt.InvalidTokenError:
            # Handle invalid token
            return None

# Example usage
secret_key = "your_secret_key_here"
jwt_auth = JWTAuthentication(secret_key)
user_id = 123
token = jwt_auth.generate_token(user_id)
decoded_user_id = jwt_auth.decode_token(token)

print(f"Token: {token}")
print(f"Decoded User ID: {decoded_user_id}")