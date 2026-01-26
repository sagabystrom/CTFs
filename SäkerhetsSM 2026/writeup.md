# Säkerhets-SM 2026
Competed solo\
11 solved challenges and 590 points\
Open bracket with placement 71 (138 overall)

## Intro

### Flags 101
- Easy
- Flag was in the description of the challenge

### Discord 101
- Easy
- Flag was in the description of the channel #säkerhetssm on Discord

### Encoding 101
- Easy
- Using Cyberchef to encode the string, first from Hex then from base64

### DNS 101
- Easy
- Command: nslookup -type=X sakerhetssm.se

### Remote 101
- Easy
- Just using the given command: ncat --ssl remote-101.ctfchall.se 50000

### ELF 101
- Easy
- I had to change the permission on the elf file:
chmod +x elf, then run it: ./elf

## Web

### Follow the flag
- Easy
- The website redirects too fast, you get the second part of flag first, disable javascript and get first part:\
F12, shift+ctrl+p, Disable javascript and press button

## Crypto

### Bitbytaren
- Easy
- From the python file we were given I wrote my own script to solve the encryption:\
crypto.py (linked)

## Reversing 

### Lottery
- Easy
- Had to get the ticket id in order to solve it:\
key = [126, 24, 126, 21, 125, 96, 0, 7, 7, 103, 3, 7, 102, 116, 106, 21]\
target = "MLOMD8S7MVT77GRO"\
ticket_id = "".join([chr(ord(t) ^ k) for t, k in zip(target, key)])\
print(ticket_id)
- Winning ticket_id: 3T1X9XS0J1W0Q38Z


## Misc

### Alias $cmd='exit #'
- Medium
- All commands were aliased to exit, but commands trough /bin worked, looked trough folders and files until I found the /etc folder\
Command: /bin/ls -la /etc/sup3rs3cr3t\
And inside was the flag: /bin/cat /etc/sup3rs3cr3t/flag.txt

### Flaggy Flag
- Hard
- Clocks that refer to semaphore flags, I solved it manually with the help of https://bobbiec.github.io/semaphore-decoder.htmler
