import random
import string
import pyDes
from pyDes import CBC, PAD_PKCS5
from os.path import *
from tkinter import *
from tkinter import filedialog
from functools import partial
from time import gmtime, strftime
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


ENCRYPT = 1
DECRYPT = 0
name = {1: 'encrypt', 0: 'decrypt'}
block_size = 8


def read_file(file_name, mode='rb'):
    file = open(file_name, mode)
    text = file.read()
    file.close()
    return text


def write_file(file_name, text, mode='wb'):
    file = open(file_name, mode)
    file.writelines(text) if type(text) is list else file.write(text)
    file.close()


def generate_key_and_iv():
    value = ''.join(random.choice(string.ascii_lowercase) for _ in range(block_size))
    key = bytes(value, 'unicode_escape')
    iv = get_random_bytes(block_size)
    return key, iv


def generate_name(path, flag, func):
    bname = splitext(basename(path))[0]
    ctime = strftime('%Y%m%d%H%M%S', gmtime())
    fname = f"{ctime}_{func}_{name[flag]}_{bname}.txt"
    return fname


def limit_entry(str_var, length):
    def callback(str_var):
        c = str_var.get()[0:length]
        str_var.set(c)
    str_var.trace('w', lambda name, index, mode, str_var=str_var: callback(str_var))


def window_key(frame, title, row, column, func_name, flag, iv=None):
    mykey, myiv = StringVar(), StringVar()
    limit_entry(mykey, block_size), limit_entry(myiv, block_size)
    Label(frame, text=title).grid(row=row, column=column, padx=10, pady=10)
    Entry(frame, textvariable=mykey).grid(row=row, column=column+1, padx=10, pady=10)

    if iv is True:
        Label(frame, text=f'{name[flag]}_iv').grid(row=row+1, column=column, padx=10, pady=10)
        Entry(frame, textvariable=myiv).grid(row=row+1, column=column + 1, padx=10, pady=10)
        Button(frame, text='save', command=partial(func_name, flag, mykey, myiv)).grid(row=row, column=column+2, padx=10, pady=10)  # button
    else:
        Button(frame, text='save', command=partial(func_name, flag, mykey)).grid(row=row, column=column+2, padx=10, pady=10)  # button
