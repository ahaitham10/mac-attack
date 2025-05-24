import hashpumpy
from server import generate_mac, verify

def perform_attack():
    # Original message
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = generate_mac(intercepted_message)
    
    print("\n=== Original Message and MAC ===")
    print(f"Message: {intercepted_message.decode()}")
    print(f"MAC: {intercepted_mac}")
    
    # Data to append
    data_to_append = b"&admin=true"
    
    # Try different key lengths
    for key_length in range(8, 17):
        print(f"\nTrying key length: {key_length}")
        
        # Perform length extension attack using hashpump
        new_mac, new_message = hashpumpy.hashpump(
            intercepted_mac,
            intercepted_message.decode(),
            data_to_append.decode(),
            key_length
        )
        
        print("\n=== Length Extension Attack Results ===")
        print(f"Forged message: {new_message}")
        print(f"Forged MAC: {new_mac}")
        
        # Verify the forged message
        print("\n--- Verifying forged message ---")
        if verify(new_message.encode(), new_mac):
            print("Attack successful! Forged message accepted.")
            print("This demonstrates the vulnerability of the insecure MAC implementation.")
            return
        else:
            print("Attack failed for this key length.")
    
    print("\nAttack failed for all attempted key lengths.")

if __name__ == "__main__":
    perform_attack() 
