### Description
TextCryptor is a simple and efficient text encryption and decryption tool implemented in Python. This project provides a user-friendly command-line interface for encrypting and decrypting messages using a custom substitution cipher. The tool allows users to specify a key to shift characters within a predefined set of symbols, offering a basic level of security for textual data.

#### Features
- **Encryption**: Convert plain text messages into encrypted text using a user-defined key.
- **Decryption**: Restore encrypted messages back to their original plain text form using the same key.
- **Custom Character Set**: Utilizes a unique set of characters to enhance security and versatility.
- **User-Friendly Interface**: Simple command-line interface for easy interaction and usage.

#### Usage
1. **Encrypt a Message**:
   - Run the script and choose the encryption mode by pressing `1`.
   - Enter a key (recommended range: 1-26).
   - Input the message you want to encrypt.
   - The script will display the original and encrypted messages.

2. **Decrypt a Message**:
   - Run the script and choose the decryption mode by pressing `2`.
   - Enter the key used during encryption.
   - Input the encrypted message.
   - The script will display the encrypted and decrypted messages.

#### Example
```
=======================================================
	Welcome To Text Encrypter And Decrypter
=======================================================
To Encrypt Text, Press 1
To Decrypt Text, Press 2
Enter Your Choice: 1
******	 ENCRYPTION MODE SELECTED	******
Enter Key (1 - 26) [Recommended: 7]: 7
Enter Your Message To Encrypt: Hello, World!
==============================================================
Original Message:  Hello, World!
Encrypted Message: w{..v,du8x]v
==============================================================

To Encrypt Text, Press 1
To Decrypt Text, Press 2
Enter Your Choice: 2
******	 DECRYPTION MODE SELECTED	******
Enter Key (1 - 26) [Recommended: 7]: 7
Enter Your Message To Decrypt: w{..v,du8x]v
==============================================================
Encrypted Message:  w{..v,du8x]v
Decrypted Message:  Hello, World!
==============================================================
```

### Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/itsmtf003/CypherTextCryptor
   ```
2. **Navigate to the Directory**:
   ```sh
   cd TextCryptor
   ```
3. **Run the Script**:
   ```sh
   python textcryptor.py
   ```

### Contribution
Contributions are welcome! Please feel free to submit issues and pull requests to enhance the functionality and features of TextCryptor.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.
