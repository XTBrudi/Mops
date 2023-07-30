import socket
import subprocess
import requests

def start_control_file():
    host = 'localhost'  # Change this to the IP address of the computer where the Console is running
    port = 35531  # Change this to the same port number you used in the Console script

    try:
        control_file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        control_file_socket.bind((host, port))
        control_file_socket.listen(1)
        print(f"ControlFile is listening on {host}:{port}")

        console, addr = control_file_socket.accept()
        print(f"Console connected from {addr}")

        while True:
            command = console.recv(4096).decode()
            if command.lower() == 'exit':
                break
            result = execute_command(command)
            print("Result:", result)
            console.send(result.encode())

        console.close()
        print("Console disconnected.")
    except KeyboardInterrupt:
        print("ControlFile closed.")

def execute_command(command):
    if command.lower() == 'hello':
        return "!HELLO!"
    return "Invalid command."

if __name__ == "__main__":
    start_control_file()