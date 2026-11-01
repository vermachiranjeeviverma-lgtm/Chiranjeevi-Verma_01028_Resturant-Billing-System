
# Restaurant Billing System
# Project No. 33
# Language: Python 3

# Restaurant Menu
menu = {
    "Dosa": 80,
    "Idli": 40,
    "Thali": 150,
    "Tea": 20
}

# Function to display menu
def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    for item, price in menu.items():
        print(f"{item:<15} Rs. {price}")
    print("=====================================")


# Function to calculate subtotal
def calculate_subtotal(ordered_items):
    subtotal = 0

    for item in ordered_items:
        subtotal += item["price"] * item["quantity"]

    return subtotal


# Function to calculate discount
def calculate_discount(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    else:
        return 0


# Function to calculate GST
def calculate_gst(amount):
    return amount * 0.05


# Function to generate final bill
def generate_bill(ordered_items):

    subtotal = calculate_subtotal(ordered_items)

    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount

    gst = calculate_gst(amount_after_discount)

    grand_total = amount_after_discount + gst

    print("\n\n========== CUSTOMER BILL ==========")

    print(f"{'Item':<15}{'Qty':<8}{'Amount':>10}")
    print("-----------------------------------")

    for item in ordered_items:
        name = item["name"]
        quantity = item["quantity"]
        amount = item["price"] * quantity

        print(f"{name:<15}{quantity:<8}{amount:>10.2f}")

    print("-----------------------------------")
    print(f"{'Subtotal:':<23} Rs. {subtotal:.2f}")
    print(f"{'Discount (10%):':<23} Rs. {discount:.2f}")
    print(f"{'GST (5%):':<23} Rs. {gst:.2f}")
    print("-----------------------------------")
    print(f"{'GRAND TOTAL:':<23} Rs. {grand_total:.2f}")

    print("===================================")
    print("       THANK YOU! VISIT AGAIN")
    print("===================================")


# Main function
def main():

    ordered_items = []

    print("\nWELCOME TO RESTAURANT BILLING SYSTEM")

    display_menu()

    while True:

        item_name = input(
            "\nEnter item name (or 'done' to generate bill): "
        ).strip()

        # Stop ordering
        if item_name.lower() == "done":
            break

        # Validate item name
        matched_item = None

        for item in menu:
            if item.lower() == item_name.lower():
                matched_item = item
                break

        if matched_item is None:
            print("Invalid item! Available items: Dosa, Idli, Thali, Tea")
            continue

        # Validate quantity
        quantity_input = input("Enter quantity: ").strip()

        try:
            quantity = int(quantity_input)

            if quantity < 1:
                print("Quantity must be at least 1.")
                continue

        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        # Add item to ordered list
        ordered_items.append({
            "name": matched_item,
            "price": menu[matched_item],
            "quantity": quantity
        })

        amount = menu[matched_item] * quantity

        print(
            f"{matched_item} x{quantity} added | Amount: {amount}"
        )

    # Generate bill
    if len(ordered_items) > 0:
        generate_bill(ordered_items)
    else:
        print("\nNo items ordered. Bill not generated.")


# Program execution
if __name__ == "__main__":
    main()
