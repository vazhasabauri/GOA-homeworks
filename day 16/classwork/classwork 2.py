correct_pin = "1234"
user_pin = input("Enter PIN code: ")

while user_pin != correct_pin:
    print("Incorrect PIN. Please try again.")
    user_pin = input("Enter PIN code: ")

print("PIN is correct. Welcome!")


