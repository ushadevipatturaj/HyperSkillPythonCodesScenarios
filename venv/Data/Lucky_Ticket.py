# Save the input in this variable
ticket = input()

# Add up the digits for each half
string_ticket = list(ticket)
half1 = int(string_ticket[0]) + int(string_ticket[1]) + int(string_ticket[2])
half2 = int(string_ticket[3]) + int(string_ticket[4]) + int(string_ticket[5])

#Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")