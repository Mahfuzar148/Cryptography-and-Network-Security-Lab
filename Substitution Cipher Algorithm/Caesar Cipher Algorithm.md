# 🔐 Caesar Cipher Implementation

## 📌 Overview

Caesar Cipher is one of the simplest and most well-known encryption techniques in classical cryptography. It is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

This project demonstrates both **encryption** and **decryption** using Caesar Cipher in a clean and easy-to-understand way.

---

## 🧠 How It Works

Each character is converted into its ASCII value, shifted using a key, and then converted back to a character.

### 🔹 Encryption Formula

C = (P + k) % 26

### 🔹 Decryption Formula

P = (C - k + 26) % 26

Where:

* P = Plaintext position (A=0, B=1, ...)
* C = Ciphertext position
* k = Shift value (key)

---

## ⚙️ Algorithm

### 🔐 Encryption Steps

1. Take plaintext input
2. Take shift value (k)
3. For each character:

   * Check if it is uppercase or lowercase
   * Convert character to position (A=0 or a=0)
   * Apply shift
   * Apply modulo 26
   * Convert back to character
4. Return encrypted text

---

### 🔓 Decryption Steps

1. Take ciphertext input
2. Take shift value (k)
3. For each character:

   * Convert to position
   * Subtract shift
   * Add 26 (to avoid negative values)
   * Apply modulo 26
   * Convert back to character
4. Return original plaintext

---

## 🔄 Flow (Concept)

Character → ASCII → Shift → Modulo → Character

---

## 💻 Example

Input:
HELLO
Shift: 3

Output:
Encrypted: KHOOR
Decrypted: HELLO

---

## 🛠️ Features

* Supports both uppercase and lowercase letters
* Keeps spaces, numbers, and symbols unchanged
* Handles large shift values using modulo operation
* Includes both encryption and decryption
* Simple and beginner-friendly implementation

---

## 📁 Project Structure

```
Caesar-Cipher/
│
├── main.cpp        # C++ implementation
├── main.py         # Python implementation
├── README.md       # Project documentation
```

---

## 🚀 How to Run

### ▶️ Python

```bash
python main.py
```

### ▶️ C++

```bash
g++ main.cpp -o cipher
./cipher
```

---

## ⚠️ Limitations

* Not secure for modern cryptographic use
* Vulnerable to brute-force attacks
* Only 25 possible keys
* Can be broken using frequency analysis

---

## 🔐 Security Analysis

Caesar Cipher is considered weak because:

* All possible shifts can be tried easily (brute-force)
* Patterns in text remain visible
* No randomness in encryption

---

## 📚 Use Cases

* Learning cryptography basics
* Academic assignments and projects
* Understanding encryption logic
* Practice for programming and algorithms

---

## 🧠 Key Concepts

* ASCII Conversion (ord / chr)
* Modular Arithmetic
* Character Manipulation
* Encryption & Decryption Logic

---

