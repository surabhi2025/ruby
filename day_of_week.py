import datetime

def is_it_the_weekend(day_name):
    """
    Docstring for is_it_the_weekend
    Input
        :param day_name: Name of the day
    Output: Str

    """

    if day_name == "Saturday" or day_name == "Sunday":
        print("Time to party!")
    else:
        print("Back to school")

    return day_name,
 
today = datetime.datetime.now()   
day_name = today.strftime("%A")  
print("The date today is:", datetime.datetime.now())
weekend = is_it_the_weekend(day_name)
print(weekend)