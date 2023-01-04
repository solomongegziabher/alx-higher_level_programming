#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> d2365ef3206d6e0ebe2d8d839df77b6054712782
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
