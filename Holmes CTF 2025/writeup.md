I was part of TeamDelta during this event and together we solved all the challanges.
Here you can find parts of solved challanges:

# CARD:
Malware sha-256: 7477c4f5e6d7c8b9a0f1e2d3c4b5a6f7e8d9c0b1a2f3e4d5c6b7a8f9e0d17477 

Found from the indicator--neuralstorm-hash-2025-001

C2 ip: 
74.77.74.77 

Ran the sha-256 through provided website

Banner:
I carry, not to haunt me, but to hold me together - NULLINC REVENGE 

Using the cognet scanner -> services - look through banners



# Watchman:
10.0.69.45

statistics on wireshark showed the relevant ip's, this had a lot of request etc

WATSON-ALPHA-2

sort by ip on wireshark, first packages show



# Tunnel
Portal username: mike.sullivan 

Used the following command: strings memdump.mem | egrep -i "username=|login=|password=|POST /" -n 

Output: username=mike.sullivan&password=Pizzaaa1%21
