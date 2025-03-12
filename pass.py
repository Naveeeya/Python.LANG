import random
import string
password=""


while True:
    passwords= str(random.choice(string.ascii_letters+ string.digits + string.punctuation))
    if len(password)<10:
        password=password+passwords
    
    elif len(password)==10:
        print(f"here's a suggested safe password for you {password}")
        break