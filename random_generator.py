import secrets
import random
import string

def generator_random_string():
  characters = string.ascii_letters + string.digits
  random_string = ''.join(random.choice(characters) for i in range(10))
  return random_string

def generate_flask_secret_key():
  secret_key = secrets.token_hex(32)
  return secret_key

# with open('secret.key', 'w') as f:
#   f.write(generate_flask_secret_key())

# print(generator_random_string())