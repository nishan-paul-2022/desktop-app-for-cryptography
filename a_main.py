from b_utility import *
from des_user_defined_function import des_user_defined_function_ende
from des_built_in_function import des_built_in_function_ende
from cipher_built_in_function import cipher_built_in_function_ende


def main():
    window = Tk()
    window.title("opencv")
    frame = Frame(window, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    window_key(frame=frame, title='des_user_encrypt', row=2, column=0, func_name=des_user_defined_function_ende, flag=1)
    window_key(frame=frame, title='des_built_encrypt', row=2, column=10, func_name=des_built_in_function_ende, flag=1, iv=True)
    window_key(frame=frame, title='cipher_built_encrypt', row=2, column=30, func_name=cipher_built_in_function_ende, flag=1, iv=True)
    window_key(frame=frame, title='des_user_decrypt', row=6, column=0, func_name=des_user_defined_function_ende, flag=0)
    window_key(frame=frame, title='des_built_decrypt', row=6, column=10, func_name=des_built_in_function_ende, flag=0, iv=True)
    window_key(frame=frame, title='cipher_built_decrypt', row=6, column=30, func_name=cipher_built_in_function_ende, flag=0, iv=True)

    button7 = Button(frame, text="exit", padx=10, pady=10, bg="gray", fg="white", command=window.destroy)
    button7.grid(row=8, column=10, sticky="nsew", padx=10, pady=10)

    window.mainloop()


main()

