class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("blu",10)
woo=parrot("Woo",8)

print("Blu is a {}.".format(blu.species))
print("Woo is a {}.".format(woo.species))

print("{} is {} year old.".format(blu.name,blu.age))
print("{} is {} year old.".format(woo.name,woo.age))