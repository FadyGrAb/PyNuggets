import secrets
import string
import collections

# Generating an "URL safe" token for password resets
reset_token = secrets.token_urlsafe(32)
reset_url = "https://mywebsite.com/passwordreset?token=" + reset_token
print("Reset URL: ", reset_url)

# Generate a 10 characters alpha-numeric password
characters_set = string.ascii_letters + string.digits
pass_list = [secrets.choice(characters_set) for _ in range(10)]
password = "".join(pass_list)
print("10 characters alpha-numeric password: ", password)

# Generate a 10 characters password with:
#   - At least one caplital letter.
#   - At least one small letter.
#   - At least 3 digits.
#   - Exactly one special character.
#   - No repeated characters (case sensitive).
characters_set = string.ascii_letters + string.digits + string.punctuation
while True:
    pass_list = [secrets.choice(characters_set) for _ in range(10)]
    password = "".join(pass_list)
    if any([c.islower() for c in password]) \
            and any([c.isupper() for c in password]) \
            and (sum([c.isdigit() for c in password]) >= 3) \
            and (sum([c in string.punctuation for c in password]) == 1) \
            and all([c == 1 for c in collections.Counter(password).values()]):
        break
print("More conditions password: ", password)
