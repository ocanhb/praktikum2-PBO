# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:52:36 2024

@author: ocanh
"""
class Segitiga:
    def hitung_keliling(self, a, b, c):
        return a + b + c

    def hitung_luas(self, a, t):
        return 0.5 * a * t

if __name__ == "__main__":
    segitiga = Segitiga()

    print("Pilihan:")
    print("1. Luas")
    print("2. Keliling")

    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        a = float(input("Masukkan panjang alas (a): "))
        t = float(input("Masukkan tinggi (t): "))
        print("\nLuas segitiga:", segitiga.hitung_luas(a, t))
    elif pilihan == 2:
        a = float(input("Masukkan panjang sisi a: "))
        b = float(input("Masukkan panjang sisi b: "))
        c = float(input("Masukkan panjang sisi c: "))
        print("\nKeliling segitiga:", segitiga.hitung_keliling(a, b, c))
    else:
        print("Pilihan tidak valid.")

    print("Terimakasih telah menggunakan program ini")
