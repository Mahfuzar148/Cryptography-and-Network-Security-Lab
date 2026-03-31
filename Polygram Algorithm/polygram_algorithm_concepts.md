The **Polygram Algorithm** (often associated with classical cryptography) refers to encryption methods that operate on **groups of letters (polygrams)** rather than single characters. This makes it more secure than simple substitution ciphers because it hides letter frequency patterns better.

---

## 🔐 What is a Polygram?

A **polygram** is a block of letters treated as a unit:

* **Digram** → 2 letters (e.g., "TH")
* **Trigram** → 3 letters (e.g., "THE")
* And so on…

Instead of encrypting one letter at a time, the algorithm encrypts **multiple letters together**.

---

## ⚙️ How the Polygram Algorithm Works

### 1. Divide the plaintext

Break the message into fixed-size blocks.

Example (digram):

```
HELLO → HE LL OX   (padding added if needed)
```

---

### 2. Apply substitution or transformation

Each block is encrypted using a rule or key:

* Could be a lookup table
* Could use a matrix (like in Hill cipher)
* Could rearrange letters

---

### 3. Produce ciphertext

Each block is replaced with another block.

Example:

```
HE → AB
LL → CD
OX → EF

Ciphertext: ABCDEF
```

---

## 🔑 Common Polygram Algorithms

### 1. Playfair Cipher (Digram-based)

![Image](https://images.openai.com/static-rsc-4/VFVBiyVQM7ChBfYshYaBA_MOdF7KsVA5Bh8plakgWf-yVhseuzKuJ1wmN6HU9vLBmMOQBw_hClCubl9X_CDs6-4-yHn0FFlhZ2vCDUeNeBmBNNJfRCtpNoWAvvkC7Q5K2-FHKtPGZoxHlaS9uazFLiRYcWS-RUaYC4QVyabDmKvyxgsXdlkBo7pjlCOHD_k7?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/rcU6VFEcLVVzg7DDwBw5PgJVH8IlTEIAjTQw3bdKpzuZfsaG9RDtniXZEhWrHuN9z3Z128w6qSLguSfDARNMdRQ-SmMIUiQl3mnQ872wyFA-_CSH33S29_2X4g5S2eMZaxV0HOBRxLZBKnQ0VFsfwNlrP94hknKD2TxzP2XEVxo9HedDvTmVDik7MwJ3q9KD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZQkjtI3GKM3EdP4QoEMnv8dxApnMhWlNpFaottcwatMSx1ciVZEn1nrsonW5-4tbjbgKL-2qg9pMUIYfIG0GuEoBjvx8kBpyU_LNE1MJIUexHmh4DCIVRpzpKTiCOM0_W3PdVF0gYpkVRZGZW5hD7D7s7TCf5KD7S65JN5ehVbmjwyXPdt8IpC5h9OkZyvtz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/jCIKH8oFlp2xB7fghBRqeWGWI2L-KUKjEIQSrIxfdrFkBLWtCfswaM4GOudJmKGHcXijpgyJ2U-bBrhs2z0VLDxo8rchFMVPDJvk9Sb4RdtL4R6dh647HJ1ijnkPai8aVY2QWHRUTTfrz318n_bWME7Vr74XFpOtYj7Bpw-LFzRZGno1CkZBAEESlyfhBIcx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Qr7l3UdSwIBPSugMMkkLdqHc9dZF4i4dSf974UJUqyRqNg3IldpRoRLTy6-0VrLyAsa9ijcy2tP4ApyXpx-Rc2XvCJ9rj6QuU8b9n2s1ZG8i8xE70NVThuQ1XTvMVPjJ638DtKDT9gsG2Ps0wiHRCfgfiAE7gtq9Hq7lQYeb_DnC4wQGiHpS6uqQhfh17P6m?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Dh9qwpdxA8pkBP5Xj0MxSsVsQ0tMWFNKe_DIBZIwzcmNVSyRaK0UM8NG6p0iVB2N3kJlt_u9ouUE-CS8R-hsZ2V7NEwrmWwyRkXmr11Pu9zeQq1gSwcJz5-1C57J8ntap3W2pGrpjN_HrPoSJ0v9WmyrPP8b0rIlhhQ6TsF40na8iUSPkBuBxJHUqGw3rJPh?purpose=fullsize)

* Uses **pairs of letters**
* Based on a 5×5 grid of letters
* Rules depend on position of letters in the grid

---

### 2. Hill Cipher (Matrix-based)

![Image](https://images.openai.com/static-rsc-4/AhdXbZQ6X_fHt2YQNh0sh68cN0sbg-297vpfgqwfAznpGAhPomMn_NmXNYcZAk9HD5s7JvqT6qAbAwn2SQua88Ks-NqGx1opGIKArDwpaZN8kVszOV18FwFQwHh5GkhqblWP7Vh4VDVMqyJrXLQHBE_OVpoA7D3k0qsuPjkRUwO0RzZjhLyCuW9cGRnaKteo?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/292-DOEx7Hzjvp4WZF8_ro9MryyGcaGMyr7IXIPq5Y6P_-s_sXUHev-ikMuokXtZpnP-OCNAY3pLPwxsa2iMYBy0a5Slt01PHuZWsXhuaSjnyGqcqpVkUYKb7edcjrfrEDeyudD_2RfEJjQKyJEp3xvxnIoH2am0dxuN-PU_tTmpwMyaZSmdFNaALNMid_nX?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/IAxMEAvKs_HJ6eURdmCii9z8-eD_XxV3M4ciQY2WTLknx0E8n18492ZljwkiAjbD1hkigCGEOlhS1SaYZGVMiSFN68WunCnk2YJ_xUCQVWCs8iK04tDujoDz6yBOVyNagMdgmytZKIjdNDBxBS7ZZjvjDULtdBJ9k0MgLfWZpgq1ZYbbt9ynl7BVNW5Z02bi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XxRRu3RzvW4T_Fq8zAhCc68MKizzsKkcvT8VtFvNb3DcTGYCzRRhl5g0AhBgw7M0O3y-3Tig2ZQRMScgQ1nJPLUxj09wYe2axtmteVgs0KR6hV_3YIJy2oJtzkSG6TTFcBxULa3mpiIHTvIApLEvUO8KIT_xfomYtLVyKKQJ9g_3Hn54sm6Gl6hIPaZ8zbyk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/59YhRiwbiVPFtEMXzMlgyO9cmLb3tJ18IkM7GNEi-f60IcAFpBy6tIohLyOLo3I7nxyRJZY0kxmf6xOVfakTsFt89MkqbRP31K4E75uyYp2JB55_a4sGKq8fjxmM4J89On9z7Cqq-6A4XVLwRd5jJ0RxdPUvTgdIz_BNbuprkL7e3CuD5uJM95f6erIYO0YF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tLYP-gnd3fh00TOUs9XPwBXhpXtpQLMvEplEMU1ejJTj076D0La5FHEafkh1Y9qG3WBYYnKoUmcTbWbph7ai75RapJ4psdRlQM3f_3oXvCSfJY9SfkKrF90b0IBT6KN_ypewhm0PeDGy6U6vsFtr9s8rA1IbdtZwa-57G1LX8tohKrL52DLyeq1LF3zk1cqZ?purpose=fullsize)

* Uses linear algebra (matrices)
* Converts letters into numbers
* Multiplies blocks by a key matrix

---

## 📊 Why Polygram is Important

Compared to single-letter (monoalphabetic) ciphers:

* ✔ More secure against frequency analysis
* ✔ Hides common patterns like "E" or "TH"
* ✔ Foundation for modern encryption techniques

---

## ⚠️ Limitations

* Still breakable with advanced analysis
* Requires shared key or matrix
* More complex than simple substitution

---

## 🧠 Simple Analogy

Think of it like:

* **Monoalphabetic cipher** → translating word letter-by-letter
* **Polygram cipher** → translating entire syllables or chunks

This makes it harder for attackers to guess patterns.

---

