import hashlib

SECRET_KEY = b'supersecretkey'  # 13 bytes

def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return mac == generate_mac(message)

def main():
    # Legitimate message
    message = b"amount=100&to=alice"
    mac = generate_mac(message)
    
    print("=== Server ===")
    print(f"Secret Key Length: {len(SECRET_KEY)} bytes")
    print(f"Original Message: {message.decode()}")
    print(f"Original MAC: {mac}\n")
    
    # PASTE YOUR FORGED VALUES HERE (from client.py output)
    forged_message = b'amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x01\x00\x00\x00\x00\x00\x00&admin=true'
    forged_mac = "97312a73075b6e1589117ce55e0a3ca6"
    
    print("=== Verification ===")
    print(f"Forged Message: {forged_message}")
    print(f"Forged MAC: {forged_mac}")
    
    # Verification result
    if verify(forged_message, forged_mac):
        print("\nRESULT: SUCCESS (attack worked - MAC is vulnerable!)")
    else:
        print("\nRESULT: FAILED (MAC is secure)")

if __name__ == "__main__":
    main()
