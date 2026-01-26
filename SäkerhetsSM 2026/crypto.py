def bits_to_bytes(bits):
    out =bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        out.append(byte)
    return bytes(out)

with open("output.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
num_lines = len(lines)
bit_length = len(lines[0])

recovered_bits = []
for i in range(bit_length):
    ones = sum(int(line[i]) for line in lines)
    recovered_bits.append(1 if ones > num_lines // 2 else 0)
    
flag_bytes = bits_to_bytes(recovered_bits)
print(flag_bytes)
try:
    print(flag_bytes.decode())
except:
    pass