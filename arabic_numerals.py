# Arabic Numerals to Roman numerals
# Function to convert the number
def arabic_to_roman(num):
  # Check if the argument is int
  if not isinstance(num,int):
    return "Wrong Type"
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  result = ""
  i = 0
  # Check if number is in between 0 and 5000
  if num > 0 and num < 5000:
    while num > 0:
      for each in range(num//values[i]):
        result += symbols[i]
        num -= values[i]
      i += 1
  else:
    return "Wrong Input"
  return result
  