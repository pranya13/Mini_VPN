import socket, ssl

# Create SSL context (client mode)
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # skip certificate verification (self-signed)

# Connect to server
with socket.create_connection(("127.0.0.1", 9999)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as ssock:
        print("[*] Connected securely to VPN server")

        # Send message
        ssock.sendall(b"Hello")
        
        # Receive echo
        data = ssock.recv(1024)
        print("[*] Received:", data.decode("utf-8"))
