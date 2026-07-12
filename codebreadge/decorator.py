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