
import random

from string import ascii_letters
from tokenize import Intnumber

password=""
for password1 in password:
    password2= random.choices(ascii_letters+ Intnumber)
    password+=password2
    print(password2)