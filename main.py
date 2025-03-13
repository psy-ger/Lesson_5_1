import keyword
import string

test_list = [""]

is_valid = True

for name in test_list:
    if " " in name:
        is_valid = False
        break
    elif not name:
        is_valid = False
        break
    elif name in keyword.kwlist:
        is_valid = False
        break
    elif name.count('_') > 1:
        is_valid = False
        break
    elif name[0].isdigit():
        is_valid = False
        break
    for upper_symbol in name:
        if upper_symbol.isupper():
            is_valid = False
            break
    for punctuation_symbol in name:
        if punctuation_symbol in string.punctuation and punctuation_symbol != "_":
            is_valid = False
            break


print(is_valid)