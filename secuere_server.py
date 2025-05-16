# secure_server.py
import hmac
import hashlib

SECRET_KEY = b'supersecretkey'  # Still unknown to attacker

def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return mac == expected_mac

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)

    print("=== Secure Server ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")

    # Forged attempt
    forged_message = b"amount=100&to=alice&admin=true"
    forged_mac = mac  # Reuse attacker MAC (invalid now)

    print("\n--- Verifying forged message ---")
    if verify(forged_message, forged_mac):
        print("MAC verified (unexpected).")
    else:
        print("MAC verification failed (as expected).")

if __name__ == "__main__":
    main()
