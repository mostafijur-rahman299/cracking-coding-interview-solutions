
# This is my solution to the problem
def permutation_of_palindrome(string):
    dict_data = {}
    string_len = 0

    for c in string:
        if c != " ":
            string_len += 1
            dict_data[c] = dict_data[c] + 1 if dict_data.get(c) else 1

    odd_count = 0
    for c_count in dict_data.values():
        if c_count % 2 != 0:
            odd_count += 1

    if string_len % 2 == 0 and not odd_count:
        print("This is a permutations of palindrome.")
        return
    elif string_len % 2 != 0 and odd_count == 1:
        print("This is a permutations of palindrome.")
        return
    
    print(dict_data)
    print("This is not permutations of palindrome.")
    return

permutation_of_palindrome("tact coa")




