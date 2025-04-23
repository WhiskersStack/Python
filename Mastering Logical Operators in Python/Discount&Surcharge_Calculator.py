# Discount & Surcharge Calculator

print("\nWelcome to the Discount & Surcharge Calculator!\n")

order_amount = float(input("Enter the order amount: "))
customer_type = input("Enter the customer type (regular, member or vip): ").lower()
coupon_code = input("Enter the coupon code (if any): ").lower()

if order_amount < 50:
    order_amount *= 1.05  # 5% surcharge

if customer_type in ["member", "vip"]:
    order_amount *= 0.90  # 10% discount

if customer_type == "vip" and coupon_code == "SAVE15":
    order_amount *= 0.85  # Additional 15% discount


print(
    f"\nThe final amount after applying discounts and surcharges is: ${order_amount:.2f}"
)
