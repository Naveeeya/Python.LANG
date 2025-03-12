import random
import string
give= ""

while True:
    given= str(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.punctuation))
    if len(give)<10:
        give += given
    elif len(give)==10:
        print(give)
        break

    
    
    

