# Arabic Numerals to Roman numerals
# Function to convert the number
def arabic_to_roman(num):
  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  result = ""
  i = 0
  if num < 5000:
    while num > 0:
      for each in range(num//values[i]):
        result += symbols[i]
        num -= values[i]
      i += 1
  else:
    return "Wrong Input"
  return result
