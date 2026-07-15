def menu():
    print("="*5,"Expense Tracker","="*5)
    print("1. Add Expense")
    print("2. View Expense")
    print("3. show total")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. exit")

    choice = int(input("enter your choice: "))

    if choice==1:
        category=input("enter a category: ")
        amount=int(input("enter the amount: "))
        with open ("expenses.txt","a") as file:
            file.write(f"{category},{amount}\n")
        print("expense added successfully\n")

    elif choice==2:
        with open("expenses.txt","r") as file:
            print("category\tAmount")
            print("-"*20)
            for line in file:
                category,amount=line.strip().split(",")
                print (category,"\t\t₹",amount)

    elif choice==3:
        with open("expenses.txt","r") as file:
            total=0
            for line in file:
                category,amount=line.strip().split(",")
                total+=int(amount)
        print("total expense= ₹",total)
    elif choice==4:
        search=input("enter a category to search: ")
        with open("expenses.txt","r") as file:
            for line in file:
                category,amount=line.strip().split(",")
                print("category\tAmount")
                print("-"*20)
                if category==search:
                    print("category\tAmount")
                    print("-"*20)
                    print(category,"\t\t₹",amount)
                else:
                    print("category not found")

    elif choice==5:
        delete=input("enter a category to delete: ")
        new_data=[]
        found=False
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                if category != delete:
                    new_data.append((category, amount))
                else:
                    found=True
        with open("expenses.txt", "w") as file:
            for category, amount in new_data:
                file.write(f"{category},{amount}\n")
        if found:
            print("Expense deleted successfully.")
        else:
            print("Category not found.")
    elif choice==6:
        print("exiting the program...")
        return False
    else:
        print("invalid choice")
    


while True:
    if menu()== False:
        break