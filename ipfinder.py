import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

print("You are working on" + hostname)
print("Your IP is" + myip)

url = input("Enter the URL to scan >> ")
print("The IP for "+ url +" is ",socket.gethostbyname(url))