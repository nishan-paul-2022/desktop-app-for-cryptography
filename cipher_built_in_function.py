from b_utility import *


def cipher_built_in_function_ende(flag, mykey, myiv):
    paths = filedialog.askopenfilenames(filetypes=[('Text File', '.txt')])
    key = bytes(mykey.get(), 'unicode_escape')
    iv = bytes(myiv.get(), 'unicode_escape')
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    for path in paths:
        fname = generate_name(path, flag, 'cipher_built')
        text = read_file(path)
        text = pad(text, block_size) if len(text) % block_size else text
        message = cipher.encrypt(text) if flag else cipher.decrypt(text)
        write_file(fname, message)