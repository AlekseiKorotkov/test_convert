numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'CM', 'value': 900},
        {'letter': 'D', 'value': 500},
        {'letter': 'CD', 'value': 400},
        {'letter': 'C', 'value': 100},
        {'letter': 'XC', 'value': 90},
        {'letter': 'L', 'value': 50},
        {'letter': 'XL', 'value': 40},
        {'letter': 'X', 'value': 10},
        {'letter': 'IX', 'value': 9},
        {'letter': 'V', 'value': 5},
        {'letter': 'IV', 'value': 4},
        {'letter': 'I', 'value': 1},

    ]

def arabic_to_roman(number):
    remainder = number
    roman_list = []

    for numeral_index in range(len(numerals)):

        if numerals[numeral_index]['value'] > remainder:
            continue
        q = remainder // numerals[numeral_index]['value']
        if not q:
            continue
        roman_list.append(numerals[numeral_index]['letter'] * q)
        remainder -= (numerals[numeral_index]['value'] * q)
        if not remainder:
            break
    return ''.join(roman_list)


def roman_to_arabic(number):
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result