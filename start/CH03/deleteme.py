


def send_message():
    for _ in range(10):
        print("yeah it is")
        user.input = input("Is today a good day?")
        if user_input.lower() == "y":
            send_message()
        else:
            print("okay, maybe another day!")