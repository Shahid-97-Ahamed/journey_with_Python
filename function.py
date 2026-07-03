# Normal Function

# A normal function in Python is a function that you define using the def keyword. It is used to group code so you can call it whenever you need.

# def show_welcome():
#     """Display the hospital's welcome message on the kiosk."""
#     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#     print("  Welcome to City General Hospital")
#     print("  Open 24 hours · Emergency: 108")
#     print("  Please collect your token below.")
#     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# show_welcome()

# def print_daily_special():
#     special=[
#          ("Mango Cold Brew", 180),
#         ("Avocado Toast",   220),
#         ("Blueberry Muffin",  90),
#     ]

#     print("\n🌟 TODAY'S SPECIALS 🌟")
#     for item,price in special:
#         print(f" {item:20} ¥{price}")
# print_daily_special()

# def calculate_fare(distance_km, rate_per_km):
#     """
#     Calculate taxi fare.
#     Args:
#         distance_km  : trip distance in kilometres
#         rate_per_km  : charge per kilometre (¥)
#     """

#     base_fare =30 # ¥30 minimum flag-fall
#     fare =base_fare + (distance_km *rate_per_km)
#     print(f"Distance : {distance_km} km")
#     print(f"Rate      : {rate_per_km}/ km")
#     print(f"Total     : {fare:.2f}")

# calculate_fare(12,15)

# calculate_fare(35,20)

# def print_receipt(item_name, quantity, unit_price):
#     """Print a line-item receipt for one product."""
#     total = quantity * unit_price
#     print(f"Item     : {item_name}")
#     print(f"Qty      : {quantity}")
#     print(f"Price    : ¥{unit_price:.2f} each")
#     print(f"Subtotal : ¥{total:.2f}")
#     print("─" * 28)

# print_receipt("Basmati Rice 5kg", 2, 320.00)
# print_receipt("Olive Oil 1L",    1, 450.00)

# Default Params

# def send_welcome_email(name, role="Junior Associate", department="General"):
#     """
#     Generate a welcome email.
#     Default role and department suit 80% of new hires;
#     senior or specialist hires override as needed.
#     """
#     print(f"To      : {name}")
#     print(f"Role    : {role}")
#     print(f"Dept    : {department}")
#     print(f"Message : Welcome aboard, {name}! "f"You join us as {role} in {department}.")
#     print("─" * 90)

# # Standard hire — only name needed
# send_welcome_email("Riya Sharma")

# # Senior hire — override role
# send_welcome_email("Arjun Mehta", role="Senior Engineer")

# # Specialist — override both
# send_welcome_email("Priya Patel", role="Lead Data Scientist",
#                    department="Analytics")

# def prescription_days(medicine, tablets_per_day=2, total_tablets=30):
#     """Calculate how many days a prescription will last."""
#     days = total_tablets // tablets_per_day
#     print(f"Medicine        : {medicine}")
#     print(f"Dose            : {tablets_per_day} tablet(s)/day")
#     print(f"Total tablets   : {total_tablets}")
#     print(f"Duration        : {days} days")
#     print()

# # Standard prescription
# prescription_days("Metformin 500mg")

# # 3 times a day, 60-tablet pack
# prescription_days("Amoxicillin 250mg", tablets_per_day=3, total_tablets=60)

# *args

# *args ব্যবহার করা হয় যখন তুমি জানো না কতগুলো argument function-এ পাঠানো হবে।

# "যতগুলো positional argument আসবে, সবগুলোকে একটি tuple-এ নিয়ে নাও।"

# def calculate_bill(*dish_prices):
#     print("── Order Summary ──")
#     for i, price in enumerate(dish_prices, 1):
#         print(f"  Item {i}: ¥{price}")
#     subtotal = sum(dish_prices)
#     gst      = round(subtotal * 0.05, 2)   # 5% Tax on food
#     total    = round(subtotal + gst, 2)
#     print(f"  Subtotal : ¥{subtotal}")
#     print(f"  Tax (5%) : ¥{gst}")
#     print(f"  TOTAL    : ¥{total}")

# calculate_bill(250,180,120)

# print()

# calculate_bill(350, 200, 150, 90, 400, 60)

# Multi-Package Shipping Weight


# def shipping_cost(*weights_kg):
#     """Calculate shipping cost for any number of packages."""
#     total_weight = sum(weights_kg)
#     rate = 60 if total_weight <= 5 else 50   # bulk discount
#     cost = total_weight * rate
#     print(f"Packages    : {len(weights_kg)}")
#     print(f"Total weight: {total_weight} kg")
#     print(f"Rate        : ¥{rate}/kg")
#     print(f"Shipping    : ¥{cost}")

# shipping_cost(1.5, 2.0)            # 2 packages
# print()
# shipping_cost(3.0, 1.5, 2.5, 1.0)   # 4 packages, bulk rate


# kwargs

# **kwargs ব্যবহার করা হয় যখন তুমি জানো না কতগুলো keyword argument function-এ আসবে।

def book_room(guest_name, room_type, **extras):
    print(f"╔══ Booking Confirmation ══╗")
    print(f"  Guest     : {guest_name}")
    print(f"  Room Type : {room_type}")
    if extras:
        print("  Extras:")
        for key, value in extras.items():
            print(f"    • {key.replace('_',' ').title()}: {value}")
    print(f"╚═════════════════════════╝")
    print()

# Simple booking
book_room("Anjali Singh", "Deluxe Double")

# Booking with extras
book_room(
    "Raj Kapoor", "Suite",
    meal_plan="Full Board",
    sea_view=True,
    early_check_in="10:00 AM",
    spa_package="Couple Massage"
)

#  Return Values

# Return Value হলো একটি function তার কাজ শেষ করে যে ফলাফল caller-এর কাছে ফেরত পাঠায়।

def simple_interest(principal, rate, years):
    return round(principal * rate * years / 100,2)

def compound_interest(principal, rate, years, n=12):
    amount = principal * (1 + rate / (100 * n)) ** (n * years)
    return round(amount - principal, 2)

def compare_interest(principal, rate, years):
    si = simple_interest(principal, rate, years)     # ← uses return
    ci = compound_interest(principal, rate, years)    # ← uses return
    print(f"Principal        : ¥{principal:,}")
    print(f"Rate             : {rate}% p.a.  | Years: {years}")
    print(f"Simple Interest  : ¥{si:,}")
    print(f"Compound Interest: ¥{ci:,}")
    print(f"Difference       : ¥{round(ci-si,2):,} more with compounding")
compare_interest(100_000, 8, 5)

# Return Multiple Values — Exam Result Card

# def evaluate_result(marks_obtained, total_marks=100):
#     """
#     Returns:
#         percentage  : float
#         grade       : str  (A+, A, B, C, D, F)
#         status      : str  (Pass / Fail)
#     """
#     pct = round((marks_obtained / total_marks) * 100, 2)

#     if   pct >= 90: grade = "A+"
#     elif pct >= 80: grade = "A"
#     elif pct >= 70: grade = "B"
#     elif pct >= 60: grade = "C"
#     elif pct >= 40: grade = "D"
#     else:          grade = "F"

#     status = "Pass" if pct >= 40 else "Fail"
#     return pct, grade, status    # ← returns a tuple of 3 values

# # Unpack the 3 returned values
# percentage, grade, status = evaluate_result(82, 100)
# print(f"Marks: 82/100 | {percentage}% | Grade: {grade} | {status}")

# # The returned values can be used in further logic
# if status == "Pass" and grade in ("A+", "A"):
#     print("🏅 Eligible for merit scholarship!")


# --------------------------Homework Problems------------------------------------

# Problem 01 · Normal Function

# Traffic Light Instruction Board

def show_traffic_rules():
    print(" TRAFFIC SIGNAL RULES")
    print(" Red → Stop")
    print(" Yellow → Slow Down")
    print(" Green → Go")


show_traffic_rules()

# Problem 02 · Positional Parameters

# Water Bill Calculator

def water_bill(units_consumed, rate_per_unit):
    total = units_consumed * rate_per_unit
    print(f"Units Used : {units_consumed}")
    print(f"Rate : {rate_per_unit}/unit")
    print(f"Total Bill : {total}")

# Test Calls
water_bill(120, 5)
print("──────────────────")
water_bill(300, 5)

# Problem 03 · Default Parameters

# Fast Food Order System

def place_order(item, size="Medium", extra_sauce=False):
    sauce_status = "Yes" if extra_sauce else "No"
    print(f"Order: {item} | Size: {size} | Sauce: {sauce_status}")


place_order("Burger")
place_order("Fries", size="Large")
place_order("Wrap", "Small", True)


# Problem 04 · *args

# Gym Attendance Tracker

# def gym_attendance(*members):
#     total_attendance = len(members)
#     member_list = ", ".join(members)
#     status = "Full" if total_attendance >= 10 else "Available"
    
#     print(f"Today's Attendance: {total_attendance}")
#     print(f"Members: {member_list}")
#     print(f"Status: {status}")

# # Test Calls
# gym_attendance("Riya", "Arjun", "Priya", "Karan")
# print("──────────────────────────────")
# gym_attendance("A","B","C","D","E","F","G","H","I","J","K")

# Problem 05 · kwargs

# Online Product Listing


def list_product(product_name, price, **specs):
    print(f" {product_name} — {price:,}")
    for key, value in specs.items():
        print(f"  {key.title()} : {value}")

# Test Calls
list_product("Laptop", 65000, brand="Dell", ram="16GB", storage="512GB SSD")
print("──────────────────────")
list_product("T-Shirt", 799, colour="Navy", size="L", material="Cotton")


# Problem 06 · Return Values

# Electricity Bill — Slab System

def electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 3
    elif units <= 300:
        bill = (100 * 3) + ((units - 100) * 5)
    else:
        bill = (100 * 3) + (200 * 5) + ((units - 300) * 7)
    return bill

#  Call function
bill = electricity_bill(80)
print(f"Bill: {bill}")

bill = electricity_bill(200)
print(f"Bill: {bill}")

bill = electricity_bill(450)
print(f"Bill: {bill}")


# Problem 07 · Mixed Concepts — Bonus Challenge

# Mini Supermarket Billing System

def supermarket_bill(customer_name, *items, discount=0, **extras):
    print(f"Customer : {customer_name}")
    print("── Items ──")
    
    subtotal = 0
    for name, price in items:
        print(f"  {name} {price}")
        subtotal += price
        
    print(f"Subtotal : {subtotal}")
    
    discount_amt = int(subtotal * (discount / 100))
    print(f"Discount ({discount}%): -{discount_amt}")
    
    total = subtotal - discount_amt
    
    if 'loyalty_points' in extras:
        lp = extras['loyalty_points']
        print(f"Loyalty pts {lp}: -{lp}")
        total -= lp
        
    if extras.get('gift_wrap') is True:
        print("Gift wrap : +50")
        total += 50
        
    print("──────────────────")
    return total

total = supermarket_bill(
    "Meena",
    ("Milk 1L", 65),
    ("Bread", 45),
    ("Eggs 12pk", 90),
    discount=10,
    loyalty_points=20,
    gift_wrap=True
)
print(f"You pay: {total}")
