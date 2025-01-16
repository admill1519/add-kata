class StringCalculator:
    def add(self, numbers: str) -> int:
        if isinstance(numbers, str):
            if not numbers.strip():
                return 0
            elif len(numbers.strip()) == 1 and numbers.strip().isnumeric():
                return int(numbers)