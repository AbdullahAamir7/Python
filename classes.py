class my_class:
    name="Abdullah"
    grade="A+"
    def intro(self):
        print("My name is: ",self.name)
        print("My Grade is : ",self.grade)
    def submit(self):
        print(self.name,". Your form is submitted.")

obj=my_class()
obj.intro()        
obj.submit()