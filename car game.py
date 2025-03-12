instruction ="my commamnd is:"
started = False
while True:
    instruction = input("my command is: ").lower()
    if instruction == "start":
        if started:
            print("car has already started")
        else:
            started = True
            print("car has started")
    elif instruction == "stop":
        if not started:
            print("car has already stopped")
        else:
         started = False 
         print("car has stopped")
    elif instruction == "help":
        print('''
start- car has started
stop- car has stopped
quit-quit''')
    elif instruction == "quit":
        break
    else:
        print(' i dont understand')
        
        