from app.operations import Operations


class Calculator:
    OPS = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    @staticmethod
    def parse_line(line: str):
        parts = line.strip().split()
        if len(parts) != 3:
            raise ValueError("Format: <operation> <num1> <num2>")

        op, s1, s2 = parts
        if op not in Calculator.OPS:
            raise ValueError("Invalid operation. Use add/subtract/multiply/divide")

        try:
            a = float(s1)
            b = float(s2)
        except ValueError:
            raise ValueError("Numbers must be valid numeric values")

        return op, a, b

    @staticmethod
    def evaluate(line: str):
        op, a, b = Calculator.parse_line(line)
        return Calculator.OPS[op](a, b)

    def run(self, input_fn=input, output_fn=print):
        output_fn("Welcome to the calculator REPL! Type 'exit' to quit")

        while True:
            line = input_fn(
                "Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: "
            ).strip()

            if line.lower() == "exit":
                output_fn("Goodbye!")
                break

            if not line:
                output_fn("Error: empty input")
                continue

            try:
                result = self.evaluate(line)
                output_fn(f"Result: {result}")
            except ZeroDivisionError:
                output_fn("Error: division by zero")
            except ValueError as e:
                output_fn(f"Error: {e}")
            except Exception:
                output_fn("Error: unexpected failure")
