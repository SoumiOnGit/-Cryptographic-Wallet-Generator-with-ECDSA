import json
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

# Generate a private key
private_key = SigningKey.generate(curve=SECP256k1)

# Derive the public key
public_key = private_key.get_verifying_key()

#  Convert keys to hexadecimal
private_key_hex = private_key.to_string().hex()
public_key_hex = public_key.to_string().hex()

# Hash the public key using SHA-256
public_key_bytes = public_key.to_string()
sha256_hash = hashlib.sha256(public_key_bytes).digest()

# Encode the hash using Base58
wallet_address = base58.b58encode(sha256_hash).decode()

#  Save keys and wallet address to wallet.json
wallet_data = {
    "private_key": private_key_hex,
    "public_key": public_key_hex,
    "wallet_address": wallet_address
}

with open("wallet.json", "w") as file:
    json.dump(wallet_data, file, indent=4)

print("Wallet keys and Base58 address generated and saved to 'wallet.json'.")
print(f"Wallet Address: {wallet_address}")
