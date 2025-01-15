# parent class
class Bird:

    def  __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# chils class
class Penguin(Bird):

    def __init__(self):
        # call super()function
        super().__init__()
        print("Penguin is ready")

    def whoisTHis(self):
        print("Penguin")
        
    def run(self):
        print("Run faster")


# Object creation
peggy = Penguin()
peggy.whoisTHis()
peggy.swim()
peggy.run()