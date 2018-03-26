# NetSec-1
First Program for MTU EE4723 Network Security

Requirements

* Python 3.5
* PyCryptodome

Run the program by executing any of the python files

## Nonces
I generated my nonce's using the `getrandbits()` function from `Crypto.Random.random`. The nonce has been generated in lines 55 and 76 of `alice.py` and lines 54 and 80 of `bob.py`


## File
At the end bob will send the contents of `ForAlice.txt` to Alice, This file should preferably be under 256K.
