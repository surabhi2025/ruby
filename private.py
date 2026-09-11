class myClass:

    __privateVar = 27


    def _privMeth(self):
        print("I'm inside myClass")

    
    def hello(self):
        print("Private Varible Value: ", myClass.__privateVar)



foo = myClass()
foo.hello()
foo._privMeth


