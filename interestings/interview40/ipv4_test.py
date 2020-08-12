import unittest
from ipv4 import IPV4Parser


class TestIPV4(unittest.TestCase):

    def setUp(self) -> None:
        self.ipv4_parser = IPV4Parser()

    def test_is_valid_part(self):
        self.assertTrue(self.ipv4_parser.is_valid_part('192'))
        self.assertTrue(self.ipv4_parser.is_valid_part('1'))
        self.assertTrue(self.ipv4_parser.is_valid_part('0'))
        self.assertTrue(self.ipv4_parser.is_valid_part('*'))
        self.assertFalse(self.ipv4_parser.is_valid_part('**'))
        self.assertFalse(self.ipv4_parser.is_valid_part('01'))
        self.assertFalse(self.ipv4_parser.is_valid_part('000'))
        self.assertFalse(self.ipv4_parser.is_valid_part('001'))
        self.assertFalse(self.ipv4_parser.is_valid_part('.1'))
        self.assertFalse(self.ipv4_parser.is_valid_part('492'))
        self.assertFalse(self.ipv4_parser.is_valid_part('4 2'))

    def test_is_valid_ipv4(self):
        self.assertTrue(self.ipv4_parser.is_valid_ipv4('192.22.33.4'))
        self.assertTrue(self.ipv4_parser.is_valid_ipv4('1.22.33.4'))
        self.assertTrue(self.ipv4_parser.is_valid_ipv4('0.22.33.4'))
        self.assertTrue(self.ipv4_parser.is_valid_ipv4('0.255.33.4'))
        self.assertFalse(self.ipv4_parser.is_valid_ipv4('0.256.33.4'))
        self.assertFalse(self.ipv4_parser.is_valid_ipv4('0.22.33.x'))
        self.assertFalse(self.ipv4_parser.is_valid_ipv4('192.422.33.4'))

    def test_provide_all_seem_ipv4s(self):
        result = list(self.ipv4_parser.provide_all_seem_ipv4s('129.8.7.634.23.*.23'))
        self.assertEqual('129.8.7.', result[0])
        self.assertEqual('.23.*.23', result[-1])
        self.assertIn('8.7.634.2', result)

    def test_parse_ipv4(self):
        results = list(self.ipv4_parser.parse_ipv4('129.8.7.634.23.*.23'))
        self.assertEqual(len(results), 10)

        results = list(self.ipv4_parser.parse_ipv4('929.801.7.64.323.*.23'))
        self.assertEqual(results, ['1.7.64.3', '1.7.64.32'])
        self.assertEqual(len(results), 2)

        results = list(self.ipv4_parser.parse_ipv4('929..7.64.33.*.23'))
        self.assertEqual(results, ['7.64.33.*', '64.33.*.2', '64.33.*.23', '4.33.*.2', '4.33.*.23'])
        self.assertEqual(len(results), 5)

        results = list(self.ipv4_parser.parse_ipv4('929..7.64.33.*.*'))
        self.assertEqual(results, ['7.64.33.*', '64.33.*.*', '4.33.*.*'])
        self.assertEqual(len(results), 3)

        results = list(self.ipv4_parser.parse_ipv4('929..7.64.33.*.*'))
        self.assertEqual(results, ['7.64.33.*', '64.33.*.*', '4.33.*.*'])
        self.assertEqual(len(results), 3)

        results = list(self.ipv4_parser.parse_ipv4('3.*.*.*.*'))
        self.assertEqual(results, ['3.*.*.*', '*.*.*.*'])
        self.assertEqual(len(results), 2)

        results = list(self.ipv4_parser.parse_ipv4('0.0.0.0'))
        self.assertEqual(len(results), 1)

        results = list(self.ipv4_parser.parse_ipv4('.5.30.0.01'))
        self.assertEqual(results, ['5.30.0.0'])
        self.assertEqual(len(results), 1)

        results = list(self.ipv4_parser.parse_ipv4('.5.30.0.10'))
        self.assertEqual(results, ['5.30.0.1', '5.30.0.10'])
        self.assertEqual(len(results), 2)

    def test_zero_ipv4(self):
        results = list(self.ipv4_parser.parse_ipv4('929.801.7.634.323.*.23'))
        self.assertEqual(len(results), 0)

        results = list(self.ipv4_parser.parse_ipv4('0.00.0.0'))
        self.assertEqual(len(results), 0)

        results = list(self.ipv4_parser.parse_ipv4('.'))
        self.assertEqual(len(results), 0)

        results = list(self.ipv4_parser.parse_ipv4('.5.03.0.0'))
        self.assertEqual(len(results), 0)

        results = list(self.ipv4_parser.parse_ipv4('.'))
        self.assertEqual(len(results), 0)

    def test_has_duplicates(self):
        results = list(self.ipv4_parser.parse_ipv4('1.1.1.1.1.1.1'))
        self.assertEqual(len(results), 1)
        self.assertEqual(results, ['1.1.1.1'])

        results = list(self.ipv4_parser.parse_ipv4('1.1.1.1.2.1.1.1.1'))
        self.assertEqual(results, ['1.1.1.1', '1.1.1.2', '1.1.2.1', '1.2.1.1', '2.1.1.1'])
        self.assertEqual(len(results), 5)
