# Write your code here
def print_status():
    print("""
    The coffee machine has:
    """, water, """ of water
    """, milk, """ of milk
    """, coffee_beans, """ of coffee beans
    """, disposable_cups, """ of disposable cups
    """, money, """ of money
    """)

def buy_coffee():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_choice = int(input())
    if coffee_choice == 1:
        water -= 250
        coffee_beans -=16
        money += 4
        disposable_cups -=1
    elif coffee_choice == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        disposable_cups -=1
    elif coffee_choice == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        disposable_cups -=1
    print_status()

def fill_machine():
    global water, milk, coffee_beans, disposable_cups, money
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk +=int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans +=int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups +=int(input())
    print_status()

def take_money():
    global money
    print("I gave you $"+str(money))
    money = 0
    print_status()


water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
print_status()
print("Write action (buy, fill, take):")
choice = input()
if choice == 'buy':
    buy_coffee()
elif choice == 'fill':
    fill_machine()
elif choice == 'take':
    take_money()