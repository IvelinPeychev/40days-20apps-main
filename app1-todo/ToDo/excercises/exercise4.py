while True:
    user = input("Where are you from? ")
    if user != "USA":
        user = user.capitalize()

    match user:
        case "USA":
            print("Hello")
        case "India":
            print("Namaste")
        case "Germany":
            print("Hallo")
        case _:
            break

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for item in ingredients:
    print(item.title())