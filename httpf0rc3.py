"""
    Programmer......: (C) xVjVx
    Date............: 02/03/2023
    Version.........: V1.0.0
    Major Changes...: None
    About...........: HTTPF0RC3
"""

# Import libraries
import socket

# Constant variables
HOST = str(input("[+] Host: "))
PORT = int(input("[+] Port: "))

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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Connecting to " + HOST + " ...")
client.connect((HOST, PORT))
client.send(request)
response = client.recv(2048)
print("\n[-] Response: \n\n",response.decode())