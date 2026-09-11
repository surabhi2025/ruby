class reverse:

    def __init__(self, s = ""):
        self.s = s
       


    def reversed_string(self):
        return self.s[::-1]


word = str(input("Enter a word: "))

obj = reverse(word)

print(obj.reversed_string())

