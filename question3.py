# Multiplication Pattern Analyzer

n = int(input("Enter number: "))

even_count = 0
odd_count = 0

print("\n----- Multiplication Table -----")

for i in range(1, 11):
    result = n * i

    if result % 2 == 0:
        print(n, "x", i, "=", result, "- Even")
        even_count += 1
    else:
        print(n, "x", i, "=", result, "- Odd")
        odd_count += 1

print("\nEven Results:", even_count)
print("Odd Results:", odd_count)