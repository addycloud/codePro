import time
import random
import requests
import json
import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


def dlog(*s):
    template = '{}'
    for arg in s:
        template = template + ' {}'

    print(template.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *s))
    return


def rsa_encrypt(msg):
    public_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDHdsyxT66pDG4p73yope7jxA92\nc0AT4qIJ/xtbBcHkFPK77upnsfDTJiVEuQDH+MiMeb+XhCLNKZGp0yaUU6GlxZdp\n+nLW8b7Kmijr3iepaDhcbVTsYBWchaWUXauj9Lrhz58/6AE/NF0aMolxIGpsi+ST\n2hSHPu3GSXMdhPCkWQIDAQAB
-----END PUBLIC KEY-----'''
    pub_obj = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(pub_obj)
    msg = cipher.encrypt(msg.encode())
    return base64.b64encode(msg).decode("utf-8")