def romanToInt(str):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        str = str.replace("IV", "IIII").replace("IX", "VIIII")
        str = str.replace("XL", "XXXX").replace("XC", "LXXXX")
        str = str.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in str:
            number += translations[char]
        return number

print('Please input roman number:')
romanNo = input()
print(romanToInt(romanNo))