# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:17:24 2024

@author: ocanh
"""

class DeretAngka:
    def __init__(self, nim):
        self.nim = nim

    def nim_digit (self):
        print("Deret angka dari 1 sampai 50 (kecuali 2 digit terakhir dari NIM anda):")
        for i in range(1, 51):
            if i == self.nim:
                continue
            print(i, end=' ')
        print()

nim = int(input("Masukkan dua digit terakhir NIM anda: "))

deret = DeretAngka(nim)

deret.nim_digit()
