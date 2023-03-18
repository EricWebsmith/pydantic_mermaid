import unittest

from pydantic_mermaid.mermaid_generator import get_dependencies


class TestBase(unittest.TestCase):
    def test_str(self):
        assert get_dependencies(str) == set()

    def test_dict(self):
        assert get_dependencies(dict) == set()

    def test_dict_int_str(self):
        assert get_dependencies(dict[int, str]) == set()


if __name__ == "__main__":
    unittest.main()
