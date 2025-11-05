def main():
    print("Hello from cs336!")
    a = 1
    b = 2
    for i in range(70):
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    main()
