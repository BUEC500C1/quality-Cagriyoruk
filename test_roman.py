# Test arabic_numerals
from arabic_numerals import *

def test_roman():
  assert arabic_to_roman(1) == "I"
  assert arabic_to_roman(2) == "II"
  assert arabic_to_roman(3) == "III"
  assert arabic_to_roman(4) == "IV"
  assert arabic_to_roman(10) == "X"
  assert arabic_to_roman(50) == "L"
  assert arabic_to_roman(90) == "XC"
  assert arabic_to_roman(500) == "D"
  assert arabic_to_roman(755) == "DCCLV"

