def print_binary(num):
    if num >= 1 or num <= 0:
        print("Error")
    
    binary = ["."]
    while num > 0:
        if len(binary) > 32:
            return "Error"
        r = num * 2
        if r >= 1:
            binary.append('1')
            num = r - 1
        else:
            binary.append('0')
            num = r
        
    return "".join(binary)

print_binary(0.125)


