def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_price = price * (discount_percent / 100)
        final_price = price - discount_price
        return final_price
    else:
        return price
    
# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
print(f"Final price: ZAR{final_price:.2f}")