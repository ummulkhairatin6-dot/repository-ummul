class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


pp = PersegiPanjang(10, 5)

print("Panjang:", pp.panjang)
print("Lebar:", pp.lebar)
print("Luas persegi panjang:", pp.hitung_luas())
print("Keliling persegi panjang:", pp.hitung_keliling())