class Parent():
    @staticmethod
    def area():
        pass


class Baby(Parent):
    @staticmethod
    def area():
        print(f"Here is the baby")


my_baby = Baby()

my_baby.area()






