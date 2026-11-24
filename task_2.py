
import socket

def check_port(host, port):

    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set connection timeout
        s.settimeout(3)

        # Try connecting to the given host and port
        result = s.connect_ex((host, port))

        # Check port status
        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED or not reachable on {host}")

        # Close socket
        s.close()

    except socket.gaierror:
        print("Invalid hostname or IP address.")

    except socket.error as e:
        print("Network error:", e)


# Main program
host = input("Enter IP address or hostname: ")

try:
    port = int(input("Enter port number: "))

    if 1 <= port <= 65535:
        check_port(host, port)
    else:
        print("Invalid port! Enter a number between 1 and 65535.")

except ValueError:
    print("Please enter a valid port number.")
