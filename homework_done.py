def homework_done(done):
    if done:
        print("Great job, you finsihed your homework")
    else:
        print("keep on working please")
    return done
    

done = input("Is your homework done?: ")
done = str(done)due.py


if done == "yes":
    done = True
else:
    done = False

homework = homework_done(done)
print(homework)
    



