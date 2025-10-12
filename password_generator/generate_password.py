
import string
import secrets
import random  # only for shuffle we will use SystemRandom

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Secure password generator. Returns a string."""
    if length < 1:
        raise ValueError("length should be at least 1")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # build character pool
    pool = list(lower)
    required = []  # to ensure at least one of each selected type
    if use_upper:
        pool += list(upper)
        required.append(secrets.choice(upper))
    if use_digits:
        pool += list(digits)
        required.append(secrets.choice(digits))
    if use_symbols:
        pool += list(symbols)
        required.append(secrets.choice(symbols))

    # ensure length can contain required chars
    if length < len(required):
        raise ValueError("Length too small for chosen options")

    # fill the rest with secure choices
    password_chars = required[:]
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # shuffle securely
    rng = random.SystemRandom()
    rng.shuffle(password_chars)

    return "".join(password_chars)

# Example use
if __name__ == "__main__":
    print("Example password:", generate_password(12))
    print("Long secure password:", generate_password(20, use_symbols=True))
