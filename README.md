# Cryptographic Wallet Generator with ECDSA

This project is a simple yet powerful **Cryptographic Wallet Generator** built with Python. It uses **Elliptic Curve Digital Signature Algorithm (ECDSA)** to generate secure public-private key pairs and derives a wallet address using **SHA-256** and **Base58 encoding** — similar to how Bitcoin wallets work.

## Features
- **Generate secure key pairs:** Uses ECDSA to create a private and public key.
- **Wallet address generation:** Derives the wallet address by hashing the public key (SHA-256) and encoding it with Base58.
- **Save keys securely:** Stores the private key, public key, and wallet address in a `wallet.json` file.
- **Base58 encoding:** Shortens the wallet address, making it more user-friendly.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/-Cryptographic-Wallet-Generator-with-ECDSA.git
cd -Cryptographic-Wallet-Generator-with-ECDSA
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

To generate a new wallet, run:
```bash
python wallet_generator.py
```

### Example Output
```json
{
    "private_key": "30770201010420e5f....",
    "public_key": "04bfc...",
    "wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
}
```

The keys and wallet address will be saved to a file called `wallet.json`.

## File Structure
```
.
├── wallet_generator.py
├── wallet.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used
- **Python**
- **ECDSA** for key pair generation
- **SHA-256** for hashing
- **Base58** for address formatting

## Future Improvements
- Add error handling for file operations.
- Implement wallet import/export functionality.
- Integrate with a simple blockchain prototype.
- Create a command-line interface (CLI) for ease of use.

## Contributing
Pull requests are welcome! If you'd like to improve the wallet generator, feel free to fork the repository and submit a PR.

