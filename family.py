my_dict = {'Surabhi': "8/4/2014", 'Ruby':"3/10/2024", 'Sachin': "8/23/1975", 'Ashita':"9/26/1984", 'Baba': "6/12/1949", 'Dadi': "4/13/1954" }

which_one = str(input("Pick a name: "))

if which_one in my_dict:
    print(my_dict[which_one])

else:
    print("Invalid answer")