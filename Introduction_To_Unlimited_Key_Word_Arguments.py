# Introduction to Unlimited Key Word Arguments
# kwargs are of type Dictionary and can allow the function to
# pass unlimited number of key-word arguments
def calculate(n, **kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Class example with the constructor made out of kwargs
class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # We can use the get method for the dictionary to get the value of a key
        # if the key does not exist in the dictionary, the returned value is None
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
