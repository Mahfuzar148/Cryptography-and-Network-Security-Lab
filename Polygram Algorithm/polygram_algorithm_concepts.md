
---

# 📘 Polygram Substitution Algorithm (Full Documentation)

---

## 🔰 1. Introduction

The **Polygram Substitution Algorithm** is a cryptographic technique where multiple characters (groups) are encrypted together instead of encrypting single characters individually.

In this system:

* 3-letter groups → replaced by another unique 3-letter group
* 2-letter groups → replaced by another unique 2-letter group
* 1-letter → replaced by another unique character

This ensures stronger security compared to monoalphabetic substitution.

---

## 🎯 2. Objective

* To encrypt plaintext using group-based substitution
* To avoid frequency analysis by using polygrams
* To ensure **unique mapping** (no conflict between groups)

---

## 🔤 3. Alphabet Set

We use:

```text
A–Z (26 English uppercase letters)
```

---

## 🔢 4. Total Possible Combinations

### ✅ 4.1 Three-letter combinations

[
26^3 = 17576
]

Examples:

```text
AAA, AAB, AAC, ..., ZZZ
```

---

### ✅ 4.2 Two-letter combinations

[
26^2 = 676
]

Examples:

```text
AA, AB, AC, ..., ZZ
```

---

### ✅ 4.3 Single-letter combinations

[
26
]

Examples:

```text
A, B, C, ..., Z
```

---

## 📁 5. Mapping Table Creation

We create three mapping tables:

### 🔹 5.1 Three-letter mapping

Each 3-letter group is mapped to a **unique** 3-letter group.

Example:

```text
AAA → QWE
AAB → RTY
AAC → UIO
...
```

---

### 🔹 5.2 Two-letter mapping

```text
AA → QW
AB → ER
AC → TY
...
```

---

### 🔹 5.3 One-letter mapping

```text
A → Q
B → W
C → E
...
```

---

## ⚠️ Important Rule (Uniqueness)

* No two inputs can map to the same output
* Mapping must be **one-to-one (bijective)**
* Otherwise conflict will occur during decryption

---

## ⚙️ 6. Encryption Algorithm

### Step 1: Input plaintext

```text
Plaintext = P
```

---

### Step 2: Calculate length

```text
n = length(P)
```

---

### Step 3: Compute remainder

```text
r = n % 3
```

---

### Step 4: Apply rules

#### 🔸 Case 1: r = 0

* Divide entire text into 3-letter groups
* Apply 3-letter mapping

---

#### 🔸 Case 2: r = 2

* First (n-2) characters → 3-letter groups
* Last 2 characters → 2-letter mapping

---

#### 🔸 Case 3: r = 1

* First (n-3) characters → 3-letter groups
* Next 2 characters → 2-letter mapping
* Last 1 character → 1-letter mapping

---

### Step 5: Generate ciphertext

Concatenate all mapped outputs.

---

## 🔁 7. Pseudo Code

```text
Input: Plaintext P

1. n = length(P)
2. r = n % 3
3. i = 0

4. while i < n:
    if (n - i) > 3:
        take 3 letters → apply 3-letter mapping
        i = i + 3

    else if (n - i) == 3:
        apply 3-letter mapping
        break

    else if (n - i) == 2:
        apply 2-letter mapping
        break

    else if (n - i) == 1:
        apply 1-letter mapping
        break

Output: Ciphertext
```

---

## 🧩 8. Example

### 🔹 Example 1

```text
Input: HELLOW
Length = 6 → r = 0
```

Grouping:

```text
HEL LOW
```

Encryption:

```text
HEL → XYZ
LOW → ABC
```

Output:

```text
XYZABC
```

---

### 🔹 Example 2

```text
Input: HELLO
Length = 5 → r = 2
```

Grouping:

```text
HEL LO
```

Encryption:

```text
HEL → QWE
LO → RT
```

Output:

```text
QWERT
```

---

### 🔹 Example 3

```text
Input: HELLOX
Length = 6 → r = 0
```

Grouping:

```text
HEL LOX
```

---

## 🔐 9. Advantages

* More secure than monoalphabetic cipher
* Reduces frequency pattern detection
* Flexible grouping system

---

## ⚠️ 10. Limitations

* Large mapping table required
* Complex to implement manually
* Storage of mappings needed

---

## 🧠 11. Conclusion

The Polygram Substitution Algorithm enhances encryption security by processing multiple characters at once. By using **3-letter primary grouping** and handling remainders with 2-letter and 1-letter mappings, it ensures both efficiency and uniqueness in encryption.

---

