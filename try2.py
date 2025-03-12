import random
import string
pas=""


while True:
    pas1 = str(random.choice(string.ascii_letters + string.digits + string.punctuation))
    if len(pas)<10:
        pas=pas+pas1
        
    elif len(pas)==10:
        print(f"here's a password for you {pas}")
        break
