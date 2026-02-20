class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()  
        print("Bark")

dog = Dog()
dog.speak()