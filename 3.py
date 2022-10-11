import inspect
import unittest


operators = {
    "plus": "+",
    "minus": "-",
    "multiply": "*",
    "divide": "/"
}

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5"
}

_digits = {str(i) for i in range(1, 6)}


class FunctionFactory:
    def __init__(self, out: str) -> None:
        self.out = out

    def f(self):
        def _f(inner: str = ""):
            frame = inspect.stack()[1]
            code = frame.code_context[0]
            expression = code.split("=")[-1].strip()
            if not expression[-1] == "(":
                operands = expression.split("(")
                _res = ""
                for operand in operands:
                    _op = (digits | operators).get(operand)
                    if _op:
                        _res += _op
                return eval(_res)
            if ("=" in frame.code_context[0]):
                return eval(self.out + inner)
            if inner is None:
                return int(self.out)
            if self.out in _digits:
                return self.out + inner
            return self.out + str(inner)
        return _f


ops = digits | operators

for op in ops:
    exec(f'{op} = FunctionFactory("{ops[op]}").f()')


class TestCalc(unittest.TestCase):
    def test_digit(self):
        inp = four()
        res = 4
        self.assertEqual(inp, res)

    def test_plus(self):
        inp = four(plus(four()))
        res = 8
        self.assertEqual(inp, res)

    def test_minus(self):
        inp = four(minus(three()))
        res = 1
        self.assertEqual(inp, res)

    def test_multiply(self):
        inp = four(multiply(three()))
        res = 12
        self.assertEqual(inp, res)

    def test_divide(self):
        inp = five(divide(two()))
        res = 2.5
        self.assertEqual(inp, res)

    def test_case_1(self):
        inp = two(plus(four()))
        res = 6
        self.assertEqual(inp, res)

    def test_case_2(self):
        inp = two(plus(four(minus(three(multiply(two()))))))
        res = 0
        self.assertEqual(inp, res)

    def test_case_3(self):
        inp = one(divide(two()))
        res = 0.5
        self.assertEqual(inp, res)

    def test_case_4(self):
        inp = two(multiply(two(plus(two()))))
        res = 6
        self.assertEqual(inp, res)

    def test_case_5(self):
        inp = two(
            multiply(
                two(
                    plus(
                        two()
                    )
                )
            )
        )
        res = 6
        self.assertEqual(inp, res)

    def test_case_6(self):
        inp = two(
            plus(
                four(
                    minus(
                        three(
                            multiply(
                                two()
                            )
                        )
                    )
                )
            )
        )
        res = 0
        self.assertEqual(inp, res)


if __name__ == "__main__":
    unittest.main()
