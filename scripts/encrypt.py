import base64
import os, sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-d', '--decrypt', action='store_true',
                help='Decrypt input file.')
parser.add_argument('encryptionkey', type=str,
                help='Passkey for encryption.')
parser.add_argument('inputfile', type=Path, help='Input file name')

args = parser.parse_args()

encryptionkey_provided = args.encryptionkey
encryptionkey = encryptionkey_provided.encode() # Convert to type bytes
salt = b'he\xfdT(LL\xbc6V\xa8T\xf3\x1b\xf7\x13' # from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(encryptionkey)) # Can only use kdf once

input_file = args.inputfile

if args.decrypt:

    if input_file.suffix != '.encrypted':
        print('Suffix of for file for descryption must be .encrypted')
        sys.exit()

    output_file = input_file.with_suffix('')

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    try:
        encrypted = fernet.decrypt(data)
    except InvalidToken:
        print("Wrong encryption key")
        sys.exit()

    with open(output_file, 'wb') as f:
        f.write(encrypted)
else:
    output_file = input_file.with_suffix(input_file.suffix + '.encrypted')
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
