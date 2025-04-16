import random
import string
from datetime import datetime


def id_generator(size=10, chars=string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

