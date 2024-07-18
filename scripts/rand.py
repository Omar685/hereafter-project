import secrets
import string

def generate_16bit_code(length):
  alphabet = string.ascii_letters + string.digits
  code = ''.join(secrets.choice(alphabet) for _ in range(length))
  return code

def generate_flask_secret_key():
  secret_key = secrets.token_hex(32)
  return secret_key

# with open('secret.key', 'w') as f:
#   f.write(generate_flask_secret_key())
# print(generate_16bit_code(16))