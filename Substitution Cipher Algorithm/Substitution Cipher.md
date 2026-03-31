
# 🔐 **Substitution Cipher কী?**

**Substitution Cipher** হলো এমন একটি encryption পদ্ধতি
👉 যেখানে প্রতিটি অক্ষরকে অন্য একটি অক্ষর দিয়ে **replace (বদলে দেওয়া)** করা হয়

👉 সহজভাবে:
**“একটা অক্ষরের জায়গায় অন্য অক্ষর বসানো”**


# 🧠 **Basic Idea**

👉 Plain text (মূল লেখা) → Cipher text (encoded লেখা)

উদাহরণ:

* A → D
* B → E
* C → F

👉 তাহলে:

```
HELLO → KHOOR
```

---

# 🔢 **Algorithm (Step-by-Step)**

## 🔹 Step 1: Key define করা

👉 কোন অক্ষর কোন অক্ষরে যাবে তা ঠিক করা

উদাহরণ:

```
Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher: DEFGHIJKLMNOPQRSTUVWXYZABC
```

---

## 🔹 Step 2: Encryption (Encode করা)

👉 প্রতিটি অক্ষর replace করা হয়

### 📌 Example:

Plain text:

```
HELLO
```

👉 Mapping:

* H → K
* E → H
* L → O
* O → R

👉 Cipher text:

```
KHOOR
```

---

## 🔹 Step 3: Decryption (Decode করা)

👉 reverse mapping ব্যবহার করা হয়

```
KHOOR → HELLO
```

---

# 🔑 **Types of Substitution Cipher**

## 1️⃣ **Caesar Cipher**

👉 fixed shift (সব অক্ষর একই সংখ্যায় shift হয়)

উদাহরণ:

* shift = 3
* A → D

---

## 2️⃣ **Monoalphabetic Cipher**

👉 একটাই mapping পুরো text-এর জন্য

👉 কিন্তু Caesar থেকে বেশি complex

---

## 3️⃣ **Polyalphabetic Cipher**

👉 multiple mapping ব্যবহার করে

👉 উদাহরণ:

* Vigenère Cipher

---

# ⚙️ **Mathematical Form (Caesar Cipher)**

[
C = (P + k) \mod 26
]

👉 এখানে:

* (P) = plaintext letter
* (k) = shift
* (C) = ciphertext

---

# 🎯 **Example (Step-by-step)**

Plain:

```
CAT
```

Shift = 2

👉 Mapping:

* C → E
* A → C
* T → V

👉 Result:

```
ECV
```

---

# ⚠️ **Limitations**

❌ সহজে ভাঙা যায় (frequency analysis দিয়ে)
❌ secure না modern cryptography-তে

---

# 🔥 **Advantages**

✅ সহজ
✅ দ্রুত
✅ শেখার জন্য ভালো

---

# 🧠 **Real-Life Use**

👉 Historical encryption
👉 Basic learning of cryptography

---

# 🔑 **Summary**

👉 Substitution Cipher = letter replacement

👉 Types:

* Caesar
* Monoalphabetic
* Polyalphabetic

---

# 🧠 Viva Ready Line

👉
**“Substitution cipher is a method of encryption where each character in the plaintext is replaced by another character according to a fixed rule.”**

---

