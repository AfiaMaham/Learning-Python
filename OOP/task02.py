ListTup = []

class product:
    def addProd(self):
        id = int(input("Enter id of your product: "))
        name = input("Enter name of your product: ")
        price = int(input("Enter price: "))
        prod = (id,name,price)
        ListTup.append(prod)
        print("Product successfully added!!!")
    def searchProd(self):
        name = input("Enter name of product you want to search: ")
        isFound = False
        if ListTup:
            for i in range(len(ListTup)):
                if ListTup[i][1] == name:
                    print(f"Name: {ListTup[i][1]} | Price: {ListTup[i][2]}")
                    isFound = True
                    break
            if isFound == False:
                print("Product not found")
        else:
            print("List is empty")
    def removeProd(self):
        name = input("Enter name of product you want to remove: ")
        isFound = False

        if ListTup:
            for i in range(len(ListTup)):
                if ListTup[i][1] == name:
                    ListTup.remove(ListTup[i])
                    print("Product got removed successfully")
                    isFound = True
                    break
            if isFound == False:
                print("Product not found")
        else:
            print("List is empty")
    
    def display(self):
        if ListTup:
            for i in range(len(ListTup)):
                print(f"Name: {ListTup[i][1]} | Price: {ListTup[i][2]}")
        else:
            print("No product Found")


obj = product()
while True:
    choice = input("""Enter your choice:
                    1- Add product
                    2- Search Product
                    3- Remove product
                    4- Display
                    5- Exit""")
    if choice == '1':
        obj.addProd()
    elif choice == '2':
        obj.searchProd()
    elif choice == '3':
        obj.removeProd()
    elif choice == '4':
        obj.display()
    elif choice == '5':
        break
    else:
        print("""Invalid Input..... 
kindly enter numbers 1, 2, 3, 4 or 5 only as a choice""")












# use tuples to store product
# store multiple product records ina list of tuples
# implement function for each operation
# ensure error handling for invalid input
