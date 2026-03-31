
---

# 🔐 **Caesar Cipher Algorithm – Full Documentation**

---

# 📌 1️⃣ **Introduction**

**Caesar Cipher** হলো একটি classical cryptography technique
👉 যেখানে প্রতিটি letter কে একটি fixed সংখ্যক position (shift) সামনে বা পিছনে সরানো হয়

👉 এটি একটি **Substitution Cipher**

---

# 🧠 2️⃣ **Basic Concept**

👉 Plaintext → Ciphertext

👉 প্রতিটি অক্ষর shift করা হয়

### উদাহরণ:

* Shift = 3

```text
A → D  
B → E  
C → F  
```

👉
**HELLO → KHOOR**

---

# 🔢 3️⃣ **Mathematical Representation**

## 🔹 Encryption:

[
C = (P + k) \mod 26
]

## 🔹 Decryption:

[
P = (C - k + 26) \mod 26
]

👉 এখানে:

* (P) = plaintext letter position
* (C) = ciphertext letter position
* (k) = shift key

---

# ⚙️ 4️⃣ **Algorithm Steps**

## 🔹 🔐 Encryption Algorithm

1. Input plaintext
2. Input shift value (k)
3. For each character in text:

   * যদি letter হয়:

     * position বের করো (A=0, B=1…)
     * shift apply করো
     * modulo 26 apply করো
     * আবার character-এ convert করো
   * না হলে unchanged রাখো
4. Output ciphertext

---

## 🔹 🔓 Decryption Algorithm

1. Input ciphertext
2. Input shift value
3. For each character:

   * position বের করো
   * shift subtract করো
   * +26 যোগ করো (negative avoid করতে)
   * modulo apply করো
   * character-এ convert করো
4. Output plaintext

---

# 🔄 5️⃣ **Flow (Conceptual)**

👉
**Character → Number → Shift → Modulo → Character**

---

# 💻 6️⃣ **Pseudo Code**

```text
FOR each character ch in text:
    IF ch is uppercase:
        new_char = (ch - 'A' + shift) % 26 + 'A'
    ELSE IF ch is lowercase:
        new_char = (ch - 'a' + shift) % 26 + 'a'
    ELSE:
        new_char = ch
    ADD new_char to result
```

---

# 🎯 7️⃣ **Example (Step-by-step)**

Plaintext:

```text
CAT
```

Shift = 2

| Letter | Position | +2 | Result |
| ------ | -------- | -- | ------ |
| C      | 2        | 4  | E      |
| A      | 0        | 2  | C      |
| T      | 19       | 21 | V      |

👉 Output:

```text
ECV
```

---

# 🔑 8️⃣ **Key Features**

* Simple substitution method
* Fixed shift value
* Easy to implement
* Uses modulo arithmetic

---

# ⚠️ 9️⃣ **Limitations**

❌ খুব সহজে ভাঙা যায় (Brute force / Frequency analysis)
❌ Secure না modern cryptography-তে

---

# 🔐 🔍 1️⃣0️⃣ Security Analysis

👉 মোট possible key = 25 (0 বাদ দিলে)

👉 attacker সব try করে decode করতে পারে

👉 তাই:

* **Brute-force attack সহজ**

---

# 🌍 1️⃣1️⃣ Applications

* Basic cryptography শেখার জন্য
* Educational purpose
* Puzzle / games

---

# 🆚 1️⃣2️⃣ Comparison (Short)**

| Cipher         | Complexity | Security |
| -------------- | ---------- | -------- |
| Caesar         | Low        | Low      |
| Monoalphabetic | Medium     | Medium   |
| Modern Crypto  | High       | High     |

---

# 🔑 1️⃣3️⃣ Summary

👉 Caesar Cipher = fixed shift substitution

👉 Formula:

* Encrypt → ( (P + k) \mod 26 )
* Decrypt → ( (P - k + 26) \mod 26 )

👉 Easy but insecure

---

# 🧠 **Viva Ready Answer**

👉
**“Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions using modular arithmetic.”**

---

