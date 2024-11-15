favourite_foods = [] #empty list for foods

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View all favourite foods")

    choice = input("Choose an option: ") # from user input

    if choice == "0":
        print("Thanks for using Favourite Foods Manager")
        break
    elif choice == "1":
        food = input("Enter your favourite food name: ")
        if food not in favourite_foods:
            favourite_foods.append(food)
            print(f"{food} added Successfully")
        else:
            print(f"{food} is already on the list")
    elif choice == "2":
        food = input("Enter your food name which you want to remove: ")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} remove successfully")
        else:
            print(f"{food} does not exists in list")
    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food}")
        else:
            print("List is empty or didn't added to the list. ")
    else:
        print("Invalid choice")


