# NetSec-1
First Program for MTU EE4723 Network Security

Requirements

* Python 3.5
* PyCryptodome

Run the program by executing any of the python files

## Notes
After spending ~6 hours trying to send the encrypted nonce as ASCII I gave up and just sent two messages one withe the encrypted nonce, and one with the tag.

## Nonces
I generated my nonces using the `getrandbits()` function from `Crypto.Random.random`
