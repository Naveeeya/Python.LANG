for number in range(0, 10, 2):
    print(number, number * '*')

print("We have 4 even numbers")

--------------------------------------------

for number in range(1, 10):
    if number % 2 == 0:
        print(number)

print("we have 4 even numbers")

---------------------------------------------

count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
        
print(f"we have {count} even numbers.")