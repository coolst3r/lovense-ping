import socket

def vibrate_lovense():
    try:
        # Get the IP address and port number from the user
        ip_address = input("Enter the IP address of the Lovense device: ")
        port = int(input("Enter the port number of the Lovense device: "))

        # Connect to the Lovense device
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))

        # Send the command to vibrate
        command = "AT+Vibrate:1,1"
        s.send(command.encode())

        # Close the connection
        s.close()

        # Return success message
        return "Vibration command sent successfully!"
    
    except Exception as e:
        # Return error message if there's any issue
        return str(e)

# Usage example
result = vibrate_lovense()
print(result)
