# Decorator আসলে কী?
# কল্পনা করো তোমার কাছে একটা gift (উপহার) আছে। এখন তুমি সেটাকে সুন্দর কাগজ দিয়ে মুড়ে দিলে (wrap করলে)। ভিতরের gift একই আছে, কিন্তু বাইরে থেকে নতুন কিছু যোগ হলো।
# Decorator ঠিক এভাবেই কাজ করে — একটা function-কে "মুড়ে" দিয়ে তার আগে বা পরে extra কিছু কাজ যোগ করে দেয়।

# def amar_dec(func):
#     def wrapper():
#         print("Work is started........")
#         print("Work Will be finished....")

#         func()
#     return wrapper

# @amar_dec
# def bolo_hello():
#     print("Hello!")

# bolo_hello()

def greet_decorator(func):
    def wrapper(*args):
        print("Welcome! 🙏")
        func(*args)
        print("See you again! 👋")
    return wrapper
@greet_decorator
def amar_naam(namm):
    print(f"My name {namm}")
amar_naam("Shahid")
amar_naam("Akib")