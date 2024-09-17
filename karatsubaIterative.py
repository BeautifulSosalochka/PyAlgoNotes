class IterativeKaratsubaMultiplication:
    """
    Doctests:
    >>> km = IterativeKaratsubaMultiplication(95514, 36988)
    >>> km.multiply()
    3532871832

    >>> km = IterativeKaratsubaMultiplication(123456789012345678901234567890, 987654321098765432109876543210)
    >>> km.multiply()
    121932631137021795226185032733622923332237463801111263526900
    """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def split_number(number: int) -> tuple[int, int]:
        str_number = str(number)
        mid_index = len(str_number) // 2
        part1 = str_number[:mid_index]
        part2 = str_number[mid_index:]
        return int(part1), int(part2)

    @classmethod
    def split_two_numbers(cls, x: int, y: int) -> tuple[int, int, int, int]:
        a, b = cls.split_number(x)
        c, d = cls.split_number(y)
        return a, b, c, d

    @staticmethod
    def calculate_karatsuba(a: int, b: int, c: int, d: int) -> int:
        ac = a * c
        bd = b * d
        ab_cd = (a + b) * (c + d)
        n = max(len(str(a)), len(str(b)))
        return (ac * 10 ** (2 * n)) + ((ab_cd - bd - ac) * 10 ** n) + bd

    def multiply(self) -> int:
        if len(str(self.x)) > 30 or len(str(self.y)) > 30:
            a, b, c, d = self.split_two_numbers(self.x, self.y)
            return self.calculate_karatsuba(a, b, c, d)
        else:
            return self.x * self.y

def test_multiply_large_numbers() -> None:
    test_cases = [
        (95514, 36988),
        (123456789012345678901234567890, 987654321098765432109876543210),
    ]

    for i, (x, y) in enumerate(test_cases):
        ikm = IterativeKaratsubaMultiplication(x, y)
        result = ikm.multiply()
        print(f"Test case {i + 1}:")
        print(f"  x = {x}")
        print(f"  y = {y}")
        print(f"  Result: {result}")
        print("-" * 40)


def main():
    test_multiply_large_numbers()


if __name__ == '__main__':
    main()
