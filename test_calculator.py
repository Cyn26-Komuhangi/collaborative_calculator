"""
unit tests for calculator2 functions
"""

import pytest
from calculator2 import get_numbers
from unittest.mock import patch

@patch('builtins.input', side_effect=['5', '10','done'])

def test_get_numbers_valid_input(mock_input): 

    """Test get_numbers with valid input from user """
    result= get_numbers()
    assert result == [5.0, 10.0]

@patch('builtins.input', side_effect=['5', '10','done','abc'])
def test_get_numbers_invalid_input(mock_input):
    """Test get_numbers with invalid input from user """
    result = get_numbers()
    assert result == [5.0,10.0]


