I solved the coding challanges as well as part of the Forensics challanges

# Coding

# The Bone Orchard

Code:
```Python
from collections import Counter
line1 = input().split()
N = int(line1[0])
T = int(line1[1])
line2 = input().split()
bones = [int(x) for x in line2]
counts = Counter(bones)
unique_bones = set(bones)
pairs = []
for x in unique_bones:
    y = T - x
    if y in unique_bones:
        if x < y:
            pairs.append((x, y))
        elif x == y and counts[x] > 1:
            pairs.append((x, y))
pairs.sort()
print(len(pairs))
if pairs:
    print(' '.join(f'({x},{y})' for x, y in pairs))
else:
    print()
```

Flag: HTB{f0rg0tt3n_b0n3s_r3s0n4t3} 

# The woven lights of Langmere:

Code:
```Python
MOD = 1000000007
def count_decodings(S):
    n = len(S)
    dp = [0] * (n + 1)
    dp[0] = 1 
    for i in range(1, n + 1):
        if S[i-1] != '0':
            dp[i] += dp[i-1]
        if i >= 2:
            two_digit = int(S[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        dp[i] %= MOD
    return dp[n]
S = input().strip()
print(count_decodings(S))
```

Flag: HTB{l4nt3rn_w0v3_mult1pl3_m34n1ngs}


# Forensics

# Watchtower of Mists

# LangFlow version:

1.2.0 version 

Found in applications/json http traffic in Wireshark


# CVE assinged to LangFlow:

CVE-2025-3248 

https://nvd.nist.gov/vuln/detail/CVE-2025-3248


# Ip of the attacker:

188.114.96.12 

Found on ipv4 stats in Wireshark


# System machine hostname:

strings capture.pcap | grep HOSTNAME=

Output HOSTNAME=aisrv01


# Postgres password:

strings capture.pcap | grep postgres

Password: LnGFlWPassword2025

