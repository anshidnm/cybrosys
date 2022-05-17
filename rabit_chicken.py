leg = int(input("Enter Total Number Of Legs : "))
head = int(input("Enter Total Number Of heads : "))

r = 0
while r <= head:
    c = head - r
    if r * 4 + c * 2 == leg:
        print(r, "rabbit and", c, "chicken")
    r = r + 1
