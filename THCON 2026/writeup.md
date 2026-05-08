# Writeup from some of the challenges from THCON 2026
- Played toegether with Dunderptrullen

- 29th place with 2008 points

# PNG is a lie (Steganography)

The challenge provided a .thc file containing a large text stream composed mainly of two symbols representing binary data, mixed with noise characters. The goal was to recover the hidden flag.

The symbols were interpreted as binary:
- thumbs up represents 1
- thumbs down represents 0
All other characters were ignored.

The extracted bitstream was converted into bytes and then interpreted as a binary file.

Decoding Process
1. Extract symbol stream from file
2. Convert to binary string
3. Group into 8-bit bytes
4. Convert to raw bytes
5. Save as PNG file

Result: The output was a valid PNG image containing the flag.

See solve.py script

Flag: THC{PNG3D}


# Min Max (Crypto)

This challenge involved a custom encryption scheme based on min operations over matrix multiplication-like structure. The goal was to reverse or analyze the transformation to recover the flag.

The structure of the cipher revealed a deterministic transformation that allowed reconstruction of the original message.

In order to solve this I needed the k and ct value from the instance, after that I could make a script to solve the recovered plaintext and submit that to the netcat connection, that gave me the flag.

See minmax.py

Flag: THC{fl0yd_w4rsh4ll_m33ts_crypt0gr4phy_1n_th3_tr0p1cs}


# P4t4t0rz at the library (Crypto / Logic)

The challenge referenced a large pdf with text and provided coordinate-like strings: 30:7/260:22/27:5

The first number indicated the page and the second number indicated the word

- page : word-number

Flag: Knowledge is relative


# Exponope (Crypto)

This RSA-like challenge used an unusually small exponent, making it vulnerable to standard low-exponent attacks.

You got a file containing: N and cyphertext

I followed the standard RSA encryption and if e is very small and the plaintext m is also small enough then modular reduction never happens, meaning: c=m^e

So instead of needing to factor N, you can just compute the integer e-th root of the ciphertext.

Because the exponent was too small, the ciphertext could be solved without full modular inversion techniques.

e = 5 gave the answer: 5th root of c

Decoding that integer as ASCII gave me the flag

Flag: THC{un3eD@_bett3r_eXp0neNT}
