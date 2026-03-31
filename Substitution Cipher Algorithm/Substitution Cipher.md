
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


# 🧠 🔐 **Substitution Cipher Implementation Logic**

👉 মূল ধারণা:
**প্রতিটি character কে একটি fixed rule (shift/key) অনুযায়ী replace করা**

---

# ⚙️ **Algorithm (Step-by-Step)**

## 🔹 **Step 1: Input নেওয়া**

👉 User থেকে:

* একটি **plaintext (string)**
* একটি **key / shift value (integer)**

---

## 🔹 **Step 2: Key normalize করা**

👉 কারণ:

* shift > 26 হতে পারে

👉 তাই:
[
shift = shift \mod 26
]

---

## 🔹 **Step 3: প্রতিটি character loop করা**

👉 string-এর প্রতিটি character এক এক করে process করতে হবে

---

## 🔹 **Step 4: Character type check করা**

প্রতিটি character-এর জন্য:

### ✔️ Case 1: Uppercase (A–Z)

👉 ASCII range: 65–90

### ✔️ Case 2: Lowercase (a–z)

👉 ASCII range: 97–122

### ✔️ Case 3: Other (space, number, symbol)

👉 unchanged থাকবে

---

## 🔹 **Step 5: Character → Number conversion**

👉 Alphabet position বের করা:

### Uppercase:


P = ch - 'A'


### Lowercase:


P = ch - 'a'


---

## 🔹 **Step 6: Encryption formula apply করা**


C = (P + shift) \mod 26


👉 এখানে:

* P = original position
* C = new position

---

## 🔹 **Step 7: Number → Character conversion**

### Uppercase:


char = C + 'A'


### Lowercase:


char = C + 'a'


---

## 🔹 **Step 8: Result string তৈরি করা**

👉 প্রতিটি নতুন character append করে final ciphertext তৈরি করা

---

## 🔹 **Step 9: Output print করা**

👉 encrypted text print করা

---

# 🔄 **Decryption Algorithm**

👉 Reverse process:


P = (C - shift + 26) \mod 26


👉 কেন +26?
👉 negative avoid করার জন্য

---

# 🔍 **Complete Flow (Conceptual)**

1️⃣ Input text + shift

2️⃣ Normalize shift

3️⃣ Loop through each character

4️⃣ Check type (upper/lower/other)

5️⃣ Convert to number

6️⃣ Apply formula

7️⃣ Convert back to character

8️⃣ Append to result

9️⃣ Print output

---

# 🧠 **Example (Step-by-step thinking)**

Text: **CAT**
Shift: 2

👉 C → (2 + 2 = 4) → E
👉 A → (0 + 2 = 2) → C
👉 T → (19 + 2 = 21) → V

👉 Result: **ECV**

---

# ⚠️ **Important Logic Points**

* `% 26` ব্যবহার করতে হবে (wrap-around এর জন্য)
* case sensitivity handle করতে হবে
* non-letter character change করা যাবে না

---

# 🔑 **Final Summary (Strong)**

👉
**Substitution Cipher Algorithm = Loop + Shift + Modulo + Replace**

---

# 🧠 Viva Ready Answer

👉
**“The algorithm iterates through each character, converts it to a numerical value, applies a shift using modulo arithmetic, and converts it back to a character.”**

---
