order = ""
started = False
stopped = False

while True:

    order = input("> ").lower()

    if order == "start":
        if started == True:
            print("the car is already started")
        else:
            print("Car started!")
            started = True
            stopped = False
        
    elif order == "stop":
        if stopped == True:
            print("the car is already stopped")
        else:
            print("Car started!")
            stopped = True
            started = False

    elif order == "help":
        print("""
Start - to start the car
stop - to stop the car
quit - to quit the car
""")
        
    elif order == "quit":
        break

    else:
        print("I don't understand that")