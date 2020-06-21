principle = int(input())
counter = 0
year = 1
while principle > 50000 and principle < 700000 :
    counter +=1
    principle += (principle * 7.1 * year) / 100
print(counter)