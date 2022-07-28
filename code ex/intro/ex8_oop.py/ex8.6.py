# Write a string_utilities class that contains two methods:

# is_valid_parenthese: to validate a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order. For example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
# reverse_words: to reverse a string word by word.
# For example:

# Test	
    # print(string_utilities().is_valid_parenthese('{[(])]}'))
    # print(string_utilities().is_valid_parenthese('{[()(({}))]}'))
    # print(string_utilities().reverse_words('Bach khoa Ha Noi'))

# Result
    # False
    # True
    # Noi Ha khoa Bach


class string_utilities:
    def is_valid_parenthese(self, par):
        open_par = ("[", "{", "(")
        closed_par = ("]", "}", ")")
        res = []
        for i in par:
            if i in open_par:
                res.append(i)
            if i in closed_par:
                if open_par[closed_par.index(i)] != res.pop():
                    return False
        return not res 
    def reverse_words(self, str):
        a = str.split()
        b = a[::-1]
        return " ".join(b)
print(string_utilities().is_valid_parenthese('{[(])]}'))
print(string_utilities().is_valid_parenthese('{[()(({}))]}'))
print(string_utilities().reverse_words('Bach khoa Ha Noi'))