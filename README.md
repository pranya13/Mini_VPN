
---

## 🟦 2. Mini VPN Implementation  

```markdown
# Mini VPN Implementation

A lightweight VPN prototype built using Python sockets and TLS encryption. It secures communication between client and server while also **tracking bandwidth usage**.

## 🚀 Features
- Secure data transfer with TLS/SSL  
- Client-server architecture for encrypted tunneling  
- Echoes back secure messages  
- **Unique Feature:** Tracks **bandwidth usage per client** and displays data usage on disconnect  

## ⚙️ How It Works
- **Input:** Client sends any text/data to server  
- **Process:** Server encrypts + receives → Decrypts → Logs bandwidth → Echoes back securely  
- **Output:**  
  - Secure message echoed back  
  - Data usage displayed (e.g., `Client 192.168.0.2 transferred 4520 bytes`)  

## ▶️ Run Instructions
1. Generate certificates (self-signed for testing):  
   ```bash
   openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes
