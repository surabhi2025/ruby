word = str(input("Give a word: "))
new = tuple(word)

for i in range(len(new)-1, -1, -1):
    print(i[word])


#if slay == new:
    print("This is a pallendrom!")
#else:
    #print("This is not a pallendrom")
