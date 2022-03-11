from b_utility import *


def des_built_in_function_ende(flag, mykey, myiv):
    paths = filedialog.askopenfilenames(filetypes=[('Text File', '.txt')])
    key = bytes(mykey.get(), 'unicode_escape')
    iv = bytes(myiv.get(), 'unicode_escape')
    cipher = pyDes.des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

    for path in paths:
        text = read_file(path)
        message = cipher.encrypt(text) if flag else cipher.decrypt(text)
        fname = generate_name(path, flag, 'des_built')
        write_file(fname, message)
