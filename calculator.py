class Calculator:
    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second
