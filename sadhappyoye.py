
def enter_emo(sad,happy):
    message = input("> ")
    for chr in message:
        if message==sad:
            print("you seem :(")
        elif message==happy:
            print("you seem ;)")
        
   
returns=""     
print("yo!")
enter_emo("sad","sad")
returns+= enter_emo.__get__(chr, "chr")
print(returns)