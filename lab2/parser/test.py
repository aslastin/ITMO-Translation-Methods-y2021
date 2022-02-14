import unittest
from parser import Parser, ParseException


class ParserTestCase(unittest.TestCase):
    def _parse_str(self, input_str, modification=False):
        return str(self.parser.parse(input_str, modification))

    def _assert_inputs(self, inputs, modification=False):
        for input_str in inputs:
            self.assertEqual(input_str, self._parse_str(input_str, modification))

    def setUp(self):
        self.parser = Parser()

    # Проверяем, что при корректном вводе str класса tree совпадает с вводом
    def test_tree_str(self):
        inputs = [
            "((abc*b|a)*ab(aa|b*)b)*",
            "((a|a|acb))*acf|m",
            "((b|c)*a(b|c)*)((b|c)*a(b|c)*)((b|c)*a(b|c)*)",
            "ba(c)",
            "a|b*",
            "((b|c)*a*(b|c)*)a|b*"
        ]
        self._assert_inputs(inputs)

    def test_s(self):
        self.assertEqual(self._parse_str("    "), "")
        self.assertEqual(self._parse_str(""), "")

    def test_or(self):
        self._assert_inputs([
            "a*|ab|(fm*)*da",
            "abc",
            "a|b*c",
            "a|b|(md)",
            "a|b*",
            "ab",
            "a*b(c)"
        ])

    def test_and(self):
        self._assert_inputs(["a*b*", "(c)"])

    def test_st(self):
        self._assert_inputs(["ab(c)(a)", "a(b**)", "a**bd|c"])

    def test_c(self):
        self._assert_inputs(["c", "(c)****", "(a|bc*(d***s***))"])

    def test_bad(self):
        bad_inputs = [
            "()",
            "(abc",
            "(ab41c|s",
            "*(ac",
            "(a||d)",
            ")()()",
        ]
        for bad_input in bad_inputs:
            with self.assertRaises(ParseException):
                self._parse_str(bad_input)

    def test_modification_ok(self):
        self._assert_inputs(["a*|ab|(fm*)*da", "a|b*|(md*)*", "(a|bc*(ds*)*)"], modification=True)

    def test_modification_throw(self):
        with self.assertRaises(ParseException):
            self._assert_inputs(["c**", "a|b**|(m**d)", "(a|bc*(ds***)***)"], modification=True)


if __name__ == '__main__':
    unittest.main()
