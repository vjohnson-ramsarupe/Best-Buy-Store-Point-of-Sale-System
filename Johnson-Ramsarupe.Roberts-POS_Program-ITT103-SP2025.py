# Johnson-Ramsarupe_Roberts-POS_Program-ITT103-SP2025
# 20224901
# 20245038
# PROGRAMMING TECHNIQUES
# Jonathan Johnson
# Spring 2025
# Best Buy Retail Store



# -------------- Best Buy Retail Store --------------#
# Function to display main menus
def main():
    checkout = Checkout()

    while True:
        print("  ")
        print("                 WELCOME TO                  ")
        print("=========== BEST BUY RETAIL STORE ===========")
        print("--------------------------------------------")
        print("                MENU SYSTEM                  ")
        print("--------------------------------------------")
        print("1. View cart")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. Checkout and Generate Receipt")
        print("5. Exit")
        print("--------------------------------------------")
        print("  ")

        selection = input("Enter your choice (1-5): ").strip()
        print("  ")

        if selection == "1":
            view_cart()
        elif selection == "2":
            add_to_cart()
        elif selection == "3":
            remove_from_cart()
        elif selection == "4":
            if not cart:
                print("Cart is empty. Add items before checkout.")
                continue
            subtotal, tax, total_amount = checkout.calculate_total()  # Now unpack the tuple
            if Payment.process_payment(total_amount):  # Use the total_amount here
                receipt(total_amount)
                cart.clear()  # Clear cart after successful payment
        elif selection == "5":
            print("--------------------------------------------")
            print("Thank you for shopping with us!")
            print("--------------------------------------------")
            print("Exiting Best Buy Retail Store.")
            break  # Exit the program
        else:
            print("Invalid option. Please try again.")
            print("  ")


# -------------- PRODUCT MANAGEMENT --------------#
# Dictionary for the products catalog
Items = {
    "Milk": {"price": 120, "stock": 10},
    "Bread": {"price": 540, "stock": 8},
    "Rice": {"price": 450, "stock": 15},
    "Eggs": {"price": 60, "stock": 12},
    "Sugar": {"price": 80, "stock": 5},
    "Oil": {"price": 320, "stock": 4},
    "Salt": {"price": 55, "stock": 18},
    "Chicken": {"price": 650, "stock": 9},
    "Pepper": {"price": 40, "stock": 6},
    "Cinnamon": {"price": 150, "stock": 11},
    "Flour": {"price": 180, "stock": 12},
}


# FUNCTION TO DISPLAY STORE STOCK AND QUANTITY
def items_list():
    print("  ")
    print("=========== Best Buy Retail Store ===========")
    print("              STOCK INVENTORY        ")
    print("=============================================")
    print(f"{'Items':<15} {'Qty in Stock':<20} {'Price'}")
    print("--------------------------------------------")
    for product, details in Items.items():
        stock = details["stock"]
        price = details["price"]

        if details["stock"] < 5:
            print(f"WARNING, Low stock for {product}!")
        print(f"{product:<15} {stock:<20} ${price}")
    print("--------------------------------------------")
    print("  ")


# -------------- SHOPPING CART OPERATIONS --------------#
cart = {}


# FUNCTION TO VIEW CART
def view_cart():
    if cart:
        print("You are viewing your cart. . .")
        print("  ")
        print(f"{'Items in Cart':<15} {'Qty':<8} {'Price':<8}{'Amount':<10}")
        print("--------------------------------------------")

        total_cart_price = 0  # variable for total price of items in cart
        for item_name, quantity in cart.items():
            item_price = Items[item_name]['price']
            total_price = quantity * item_price  # calculating total price of individual items by quantity
            print(f"{item_name:<15} {quantity:<8} ${item_price:<5}    ${total_price:<10}")
            total_cart_price += total_price  # calculating subtotal cart
        print("--------------------------------------------")
        print(f"{'Total':<15}{'':>15}{'':<5}${total_cart_price:<10}")
        print("--------------------------------------------")
        print("  ")
    else:
        print("--------------------------------------------")
        print("Your Cart is empty - Add items to cart")
        print("--------------------------------------------")
        print("  ")
        main()


# FUNCTION TO ADD ITEMS TO CART
def add_to_cart():
    items_list()  # showing stock inventory list in real time
    item_name = input("Which item would you like to add to your cart? ").strip().title()
    if item_name in Items:  # checking if items are in stock
        try:
            quantity = int(input(f"How many {item_name} would you like to add to your cart? "))

            if quantity <= Items[item_name]["stock"]:  # checking stock inventory availability
                if item_name in cart:  # updating quantity if item already exists in cart
                    cart[item_name] += quantity  # Fix indentation: Added this part correctly
                    Items[item_name]["stock"] -= quantity
                    print(f"{quantity} {item_name} has been added to your cart")
                else:
                    cart[item_name] = quantity
                    Items[item_name]["stock"] -= quantity
                    print(f"{quantity} {item_name} has been added to your cart")

                # Display the updated cart after adding the item
                print("\nUpdated Cart:")
                view_cart()  # This will show the contents of the cart after adding an item
            else:
                print(f"Only {Items[item_name]['stock']} items of {item_name} are available in stock.")
        except ValueError:
            print("ERROR, Please enter a numeric value for quantity.")
    else:
        print(f"ERROR, this item is not available in store")
        print("--------------------------------------------")
        print("  ")


# FUNCTION TO REMOVE ITEMS FROM CART
def remove_from_cart():
    view_cart()
    item_name = input("Which item would you like to remove from your cart? ").strip().title()
    if item_name in cart:
        try:
            quantity = int(input(f"How many {item_name} would you like to remove from your cart? "))
            if quantity <= cart[item_name]:  # Checking to see if the user has adequate quantity to remove
                cart[item_name] -= quantity
                Items[item_name]["stock"] += quantity
                if cart[item_name] == 0:
                    del cart[item_name]  # removing item from cart completely
                    print(f"{quantity} {item_name} has been removed from your cart")  # removing item from cart
            else:
                print(f"You only have {cart[item_name]} {item_name} in your cart")
        except ValueError:
            print("ERROR, Please enter a numeric value for quantity.")  # validating user input to only be numeric
    else:
        print(f"ERROR, {item_name} is not in your cart")  # alert invalid item to be removed from cart
        print("--------------------------------------------")
        print("  ")


# -------------- CHECKOUT AND PAYMENT PROCESS --------------#
# FUNCTION TO SHOW RECEIPT
def receipt(total_amount):
    # checking if cart is empty
    if not cart:
        print("No items in cart to generate a receipt.")
        return

    # printing receipt header
    print("  ")
    print("=========== Best Buy Retail Store ===========")
    print("              PURCHASE RECEIPT        ")
    print("=============================================")
    print(f"{'Item':<15}{'Qty':<6}{'Unit Price':<12} {'Amount':<15}")
    print("---------------------------------------------")

    total_price = 0
    # loop to calculate cart items and  totals
    for item_name, quantity in cart.items():
        unit_price = Items[item_name]['price']
        amount = unit_price * quantity
        total_price += amount
        print(f"{item_name:<15}{quantity:<6}${unit_price:<12}{amount:<10}")
    print("-------------------------------------------")

    checkout = Checkout()
    subtotal, gct, total = checkout.calculate_total()

    discount = checkout.apply_discount

    print(f"{'Subtotal':<25}{'':<9}${subtotal:<10}")
    print(f"{'GCT 15%':<25}{'':<9}${gct:<10}")
    print(f"{'GRAND TOTAL':<25}{'':<9}${total:<10}")
    print("============================================")
    # thanking the customer for shopping
    print("Thank you for shopping with us!")
    print("  ")


# CLASS FOR CHECKOUT PROCESS
class Checkout:
    def init(self):
        # Initializing cart with the global cart object to be accessed anywhere
        self.cart = cart

    def add_product(self, product_name, quantity):
        # Checking if product is available and if enough stock is available
        if product_name in Items and Items[product_name]['stock'] >= quantity:
            cart[product_name] = cart.get(product_name, 0) + quantity  # Updating cart
            Items[product_name]['stock'] -= quantity  # Decreasing stock whenever an item is added to cart
            print(f"Added {quantity} x {product_name} to cart.")
        else:
            print(f"Not enough stock for {product_name}.")

    def calculate_total(self):
        # Calculating total price of all items in the cart
        subtotal = sum(Items[item]['price'] * qty for item, qty in cart.items())

        # Apply discount if subtotal is over $5000
        subtotal = self.apply_discount(subtotal)

        # Calculate General Consumption tax (15%)
        gct= subtotal * 0.15
        total = subtotal + gct
        return subtotal, gct, total

    def apply_discount(self, total):
        # If total is over $5000, apply a 5% discount
        if total > 5000:
            discount = total * 0.05  # 5% discount
            total -= discount
            print(f"Your total is over $5000")
            print(f"5% discount is applied:{'':<9} -${discount:<10}")
        return total


# CLASS FOR PAYMENT PROCESS
class Payment:
    @staticmethod
    def process_payment(amount):
        while True:
            try:
                # asking user to input payment
                payment = float(input(f"Total amount due: ${amount:.2f}. Enter payment amount: "))
                # checking if the user input a sufficient payment
                if payment >= amount:
                    change = payment - amount  # calculating change
                    print(f"Payment successful! Change: ${change:.2f}")
                    print("  ")
                    return True
                else:
                    # payment is insufficient, prompt to try again
                    print("  ")
                    print("ERROR: Insufficient payment. Try again.")
                    print("  ")
            except ValueError:
                print("ERROR: Enter a valid amount.")
                print("  ")


# Run the program
if __name__ == "__main__":
    main()

