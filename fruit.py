num = int(input("Enter a number: "))
odd_num = []
for i in range(1, num) :
    if i % 2 != 0:
        odd_num.append(i)
    

print(odd_num)


fruits = ['appple', 'bannana', 'orange', 'mango']


for i in range(len(fruits)):
   fruits[i] = fruits[i].capitalize()

print(fruits)