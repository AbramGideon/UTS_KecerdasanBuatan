import re
import random

menyapa = ["Halo juga", "Apa kabar", "Hai"]

while True:
    x = input("User\t: ")
    if re.findall(r'halo|hai|hi', x):
        print("Bot\t:", random.choice(menyapa))
    else:
        print("Bot\t: Perintah Tidak Diketahui!")
