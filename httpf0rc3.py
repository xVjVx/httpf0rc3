"""
    Programmer......: (C) xVjVx
    Date............: 17/03/2023
    Version.........: V1.1.0
    About...........: HTTPF0RC3
"""

# Import libraries
import socket
import sys

# Execution
if len(sys.argv) != 3:
    print("[!] Correct execution: python3 httpf0rc3.py HOST PORT")
    sys.exit(0)

print(r"""
  _    _ _______ _______ _____  ______ ___  _____   _____ ____  
 | |  | |__   __|__   __|  __ \|  ____/ _ \|  __ \ / ____|___ \ 
 | |__| |  | |     | |  | |__) | |__ | | | | |__) | |      __) |
 |  __  |  | |     | |  |  ___/|  __|| | | |  _  /| |     |__ < 
 | |  | |  | |     | |  | |    | |   | |_| | | \ \| |____ ___) |
 |_|  |_|  |_|     |_|  |_|    |_|    \___/|_|  \_\\_____|____/ 
""")

# Constant variables
HOST = str(sys.argv[1])
PORT = int(sys.argv[2])

def httpRequest(HOST, PORT):

    lines = []

    print("[+] Request (Press enter two times to continue):")
    while True:
        requestInput = input()
        if requestInput:
            lines.append(requestInput)
        else:
            break

    requestText = '\n'.join(lines)
    request = bytes(requestText, 'utf-8')

    if len(request) == 0:
            print("[!] The request is empty")
            sys.exit(0)

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[-] Connecting to " + HOST + " ...")
        client.connect((HOST, PORT))
        client.send(request)
        response = client.recv(2048)
        print("\n[-] Response: \n\n",response.decode())
        lines = []
    except OSError:
        print("[!] Something went wrong")
        sys.exit(0)

def main():

    httpRequest(HOST, PORT)
    
    while True:

        a = input("[+] Do you want to make another request? (Yes or No): ")

        if a == "yes" or a == "Yes":
            httpRequest(HOST, PORT)
        else:
            print("[-] Session closed")
            sys.exit(0)

if __name__ == '__main__':
    main()