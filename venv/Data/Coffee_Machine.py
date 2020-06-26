# Write your code here
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input())
print("Write how many cups of coffee you will need:")
cups_of_coffee = int(input())

coffee_available = min(water // 200, coffee // 15, milk // 50)

if cups_of_coffee == coffee_available:
    print("Yes, I can make that amount of coffee")
elif cups_of_coffee < coffee_available:
    print("Yes, I can make that amount of coffee (and even ", (coffee_available - cups_of_coffee) ," more than that)")
else:
    print("No, I can make only ",coffee_available ," cups of coffee")
