class StringCalculator:
    def add(self, numbers: str) -> int:
        if isinstance(numbers, str):
            if not numbers.strip():
                return 0