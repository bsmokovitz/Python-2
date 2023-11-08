class Roman_Num:
    def __init__(self, roman):
        self.roman = roman
        temp = self.convert()
        self.dec = temp
    def convert(self):
        rn = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
        temp = 0
        for letter in self.roman:
            temp += rn[letter]
        return temp
    def get_roman(self):
        return self.roman
    def get_dec(self):
        return self.dec
    def set_roman(self, roman):
        self.roman = roman
        temp = self.convert()
        self.dec = temp

r1 = Roman_Num("MMMV")
print(r1.get_roman(), r1.get_dec())

# MMM 3000