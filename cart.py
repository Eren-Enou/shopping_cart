from IPython.display import clear_output

shopping_cart = {}

def add(item, quantity, price):
    shopping_cart[item] = [quantity,price]
    print(f"{quantity} - {item} @ ${price} each added to the shopping cart.")

def remove(item, quantity):
    if item in shopping_cart and shopping_cart[item][0] - quantity >= 0:
        shopping_cart[item][0] = shopping_cart[item][0] - quantity
        print(f"You now have {shopping_cart[item][0]} {item}s")
    else:
        print(f"You either don't have {item} in your shopping cart, or you don't have enough to remove.")

def show():
    print("Shopping Cart:")
    total_price = 0.0
    for item in shopping_cart:
        print(f"\t{shopping_cart[item][0]} - {item}s ${shopping_cart[item][1]:.2f}")
        total_price += shopping_cart[item][0] * shopping_cart[item][1]
    print(f"Shopping Cart total = ${total_price:.2f}")
def clear():
    shopping_cart.clear()
        
def run():
    shopping = True
    while shopping:
        query = input("Would you like to add, remove, show, clear, or quit? ").capitalize()
        if query == "Add":
            item = input("Enter an item to add: ").capitalize()
            quantity = int(input(f"Enter the number of {item}s to add: "))
            price = float(input(f"Enter the price of {item}s to add: "))
            add(item,quantity, price)
        elif query == "Remove":
            item = input("Enter an item to remove: ").capitalize()
            quantity = int(input(f"Enter the number of {item}s to remove: "))
            remove(item, quantity)
        elif query == "Show":
            show()
        elif query == "Clear":
            clear()
            print("Shopping cart cleared")
        elif query == "Quit":
            shopping = False
            show()
        else:
            clear_output()
            print("Error, please select between add, remove, show, clear, and quit.")
     

    
run()