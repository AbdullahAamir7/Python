class roboat:
    def __init__(self,name):
        self.name=name
        
    def intro(self):
        print("Hello! I am Roboat my name is",self.name)

name=roboat("Jax Bolt")
name.intro()    