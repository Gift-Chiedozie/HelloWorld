command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - To start the car
stop  - To stop the car
help  - To see instructions
quit  - To exit the game
        """)
    elif command == "quit":
        print("Game exited")
        break
    else:
        print("Sorry, I don't understand that!")