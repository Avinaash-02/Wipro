class Contact:
    def __init__(self):
        self.list1 = []

    def add_number(self, no):
        for i in no:
            self.list1.append(i)

    def remove(self, no):
        if no in self.list1:
            self.list1.remove(no)
        else:
            print("No number is there")

    def search(self, no):
        if no in self.list1:
            return self.list1.index(no)
        else:
            return "Number not found"

    def show(self):
        return self.list1


phone_numbers = list(map(int, input("Enter the Phone numbers: ").split()))

contact = Contact()
contact.add_number(phone_numbers)
print("Contact List:", contact.show())
