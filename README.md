# mac-attack
# MAC Forgery Attack Demonstration

This project demonstrates a length extension attack on a vulnerable Message Authentication Code (MAC) implementation (`hash(secret || message)`) and shows how to mitigate this vulnerability using HMAC. This assignment was for the "Data Integrity and Authentication" course.

## Files Included

* `server.py`: The original server with the insecure MAC implementation.
* `client.py`: The attacker script that performs the length extension attack.
* `secure_server.py`: The modified server with the secure MAC implementation using HMAC.
* `README.md`: This file (instructions).

## How to Run

1.  **Navigate to the project directory** in your terminal.
2.  **Run the vulnerable server:**
    ```bash
    python3 server.py
    ```
    Note the outputted MAC for the original message.
3.  **Edit `client.py`:**
    * Replace the `"..."` placeholder for `intercepted_mac` with the MAC obtained from `server.py`.
4.  **Run the attack script:**
    ```bash
    python3 client.py
    ```
    Observe the forged message and MAC. The script attempts to demonstrate that the original server would accept this forged MAC.
5.  **Run the secure server:**
    ```bash
    python3 secure_server.py
    ```
6.  **Run the attack script again:** Observe that the forged MAC should now be rejected by the secure server.

## Demonstration

`client.py` implements a length extension attack to append `&admin=true` to the original message without knowing the secret key. It leverages the properties of the MD5 hash function (or a library like `hashpumpy` if used) to forge a valid MAC for the extended message.

## Mitigation

`secure_server.py` demonstrates the mitigation by using the HMAC (Hash-based Message Authentication Code) construction, which is secure against length extension attacks.

## Team Members

* [Ahmed haitham ]
* [kerelos emad]
* [kerelos nasser]
