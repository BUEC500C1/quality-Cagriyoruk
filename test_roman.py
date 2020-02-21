# Test arabic_numerals
from arabic_numerals import *
import pytest

def test_roman():
  assert arabic_to_roman(1) == "I"
  assert arabic_to_roman(2) == "II"
  assert arabic_to_roman(3) == "III"
  assert arabic_to_roman(4) == "IV"
  assert arabic_to_roman(10) == "X"
  assert arabic_to_roman(50) == "L"
  assert arabic_to_roman(90) == "XC"
  assert arabic_to_roman(500) != "DX"
  assert arabic_to_roman(755) != "IDCCLV"
  assert arabic_to_roman(1000) != "IIII"
  assert arabic_to_roman(19.96) == "Wrong Type"
  assert arabic_to_roman('X') == "Wrong Type"
  assert arabic_to_roman('two') == "Wrong Type"
  assert arabic_to_roman(-100) == "Wrong Input"
  assert arabic_to_roman(50000) == "Wrong Input"
