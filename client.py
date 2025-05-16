import hashlib
import struct

def perform_attack():
    # YOUR EXACT VALUES
    secret_key = b"supersecretkey"  # 13 bytes
    original_msg = b"amount=100&to=alice"
    original_mac = "614d28d808af46d3702fe35fae67267c"  # Your MAC
    append_data = b"&admin=true"
    
    # 1. MANUAL PADDING CALCULATION
    original_length = len(secret_key) + len(original_msg)
    padding = b'\x80' + b'\x00' * ((56 - (original_length + 1) % 64) % 64)
    padding += struct.pack('<Q', original_length * 8)  # 64-bit length
    
    # 2. BUILD FORGED MESSAGE
    forged_msg = original_msg + padding + append_data
    
    # 3. CALCULATE NEW MAC (requires knowing the key - for demo only!)
    forged_mac = hashlib.md5(secret_key + forged_msg).hexdigest()
    
    print("SUCCESS! Use these in server.py:")
    print("Forged Message:", forged_msg)
    print("Forged MAC:", forged_mac)

perform_attack()
