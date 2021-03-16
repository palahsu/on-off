#if else elif fun

print("Let's play bike game.")
command = ""
started = False
while True:
    command = input("on or off : ").lower()
    if command == "start":
        if started:
            print("Bike is already started !")
        else:
            started = True
            print("Bike started...")
    elif command == "stop":
        if not started:
            print("Bike is already stopped !")
        else:
            started = False
            print("Bike stopped.")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand everything.")
        continue
        
