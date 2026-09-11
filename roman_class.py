class Roman:
    def roman_to_int(self, roman):
        self.txt ="dada is bald"
        values = {
            "I": 1,
            "IV": 4,
            "X": 10,
            "V": 5,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        return values[roman]
    
    def dummy(self, text):
        s = text + " " + self.txt
        

        #print(self.txt)

        return s
       

c = Roman()

roman = input("Enter a Roman numeral: ")
print("Integer:", c.roman_to_int(roman))
text = "dada is popo"

print(c.dummy(text))

