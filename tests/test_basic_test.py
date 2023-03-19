import unittest
from typing import Dict

from pydantic_mermaid.mermaid_generator import _get_dependencies


class TestBase(unittest.TestCase):
    def test_str(self):
        assert _get_dependencies(str) == set()

    def test_dict(self):
        assert _get_dependencies(Dict) == set()

    def test_dict_int_str(self):
        assert _get_dependencies(Dict[int, str]) == set()


if __name__ == "__main__":
    unittest.main()
