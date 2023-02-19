#EDITED
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.membership = False
        self.points = 0
    
    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
        
        return self

    def enroll(self):
        if self.membership == False:
            self.membership = True
            self.points += 200
            print(f'enroll points: {self.points}')
        else:
            print("You are already a member!")

        return self

    def pend_points(self, amount):
        self.points -= amount
        print(f'pend points: {self.points}')

        return self
    

amir = User("Amir", "Khayat", 21)

amir.display_info().enroll().pend_points(50)



