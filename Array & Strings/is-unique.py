
def is_unique(string):
    uniq_str = ""
    for chr in string:
        if chr in uniq_str:
            return "This is not an unique string"
        uniq_str += chr
    return "This is an unique string"


def is_unique2(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return "This is not a unique string"
        checker |= (1 << val)
    return "This is a unique string"

