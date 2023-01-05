#!/usr/bin/python3
<<<<<<< HEAD
=======

>>>>>>> edc8180a01b7b7ef997129f70dd2155dad2a96a6
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
