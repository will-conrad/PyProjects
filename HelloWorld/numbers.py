numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}
msg = ''
number = input("Enter number: ")
for n in str(number):
    msg += numbers[int(n)] + ' '
print(msg)