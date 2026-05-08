data = open("file.thc", "r", encoding="utf-8", errors="ignore").read()

bits = []
for c in data:
    if c == "👍":
        bits.append("1")
    elif c == "👎":
        bits.append("0")

bitstring = "".join(bits)

img_bytes = bytes(int(bitstring[i:i+8], 2)
                  for i in range(0, len(bitstring) - 7, 8))

with open("out.png", "wb") as f:
    f.write(img_bytes)

print("[+] wrote out.png")
