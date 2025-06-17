def calculate_factorial(n):
    """Вычисляет факториал числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def main():
    number = 5
    result = calculate_factorial(number)
    print(f"Факториал {number} равен {result}")

if __name__ == "__main__":
    main()
