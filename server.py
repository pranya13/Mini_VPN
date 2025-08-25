"""
Mini VPN Prototype
Author: Pranya Gupta
Description:
    - Secure client-server communication using TLS (SSL module)
    - Encrypts all transmitted data
    - Tracks bandwidth usage per client
"""

import socket, ssl, threading

# Bandwidth tracker
bandwidth_usage = {}

def handle_client(conn, addr):
    """Handle secure communication with a client."""
    print(f"[+] Secure connection established with {addr}")
    bandwidth_usage[addr] = 0

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            bandwidth_usage[addr] += len(data)
            print(f"[{addr}] {data.decode('utf-8')}")
            conn.sendall(b"Secure Echo: " + data)
    except Exception as e:
        print(f"[-] Error with {addr}: {e}")
    finally:
        print(f"[!] Connection closed with {addr}, Data transferred: {bandwidth_usage[addr]} bytes")
        conn.close()

def start_server():
    """Start VPN server with TLS encryption."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("[*] VPN Server listening on port 9999...")

    while True:
        client_sock, addr = server.accept()
        secure_conn = context.wrap_socket(client_sock, server_side=True)
        thread = threading.Thread(target=handle_client, args=(secure_conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
