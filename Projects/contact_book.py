# 2. Contact Book
# Description: Build a contact book to save, search, delete, update and view contact details.

list = []
end = "y"

while(end != "n"):
    print("1- Save\n2- Delete\n3- Update\n4- Search\n5- View")
    choice = int(input("Select: "))
    if(choice == 1):
        name = input("Enter name: ")
        num = input("Enter contact number: ")
        email = input("Enter Email Address: ")
        dict = {'name':name, 'number':num, 'email': email}
        list.append(dict)
        print("     Contact saved successfully....")
       
    elif(choice == 2):
        isfound = False
        contact = input("Enter name you want to delete: ")
        for i in list:
            if(i.get('name') == contact):
                isfound = True
                list.remove(i)
                print("    Contact deleted.....")
                break
        if(isfound == False):
            print("Not Found")
    elif(choice == 3):
        contact = input("Enter name you want to update: ")
        for i in list:
            if(i.get('name') == contact):
                num = input("Enter contact number: ")
                email = input("Enter Email Address: ") 
                i["number"] = num
                i["email"] = email
                print("    Contact updated.....")
    elif(choice == 4):
        isfound = False
        contact = input("Enter name you want to search: ")
        for i in list:
            if(i.get('name') == contact):
                isfound = True
                print(f"name = {i.get('name')}\ncontact num = {i.get('number')}\nemail = {i.get('email')}")
        if(isfound == False):
            print("Not found")
    elif(choice == 5):
        for i in list:
             print(f"name = {i.get('name')}\ncontact num = {i.get('number')}\nemail = {i.get('email')}")
             print("-------------")
    end = input("want to continue (y/n): ")