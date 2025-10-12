def add(a, b):
    total = a + b
    return total

def main():
    x = int(input("x = "))
    y = int(input("y = "))
    result = add(x, y)   # <-- এখানে breakpoint বসাবেন
    print("Result:", result)

if __name__ == "__main__":
    main()
    