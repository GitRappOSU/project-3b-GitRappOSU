#Anthony Rapp
#GitHubOSU
#1/24/2024
#Assignment 3b, print facotrs of chosen positive integer

pos_int = int(input("Please enter a positive integer: "))
print("The factors of ", pos_int, " are: ")
print(1)
for value in range(2, pos_int):
    if pos_int % value == 0:
        print(value)
print(pos_int)
