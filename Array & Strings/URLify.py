string = "Mr John Smith    "
new_string = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trulength = 13

space_count = 0

for i in range(trulength):
    if string[i] == ' ':
        space_count += 1
        
index = trulength + space_count * 2

for i in range(trulength - 1, -1, -1):
    print(index)
    if string[i] == ' ':
        new_string[index - 1] = '0'
        new_string[index - 2] = '2'
        new_string[index - 3] = '%'
        index -= 3
    else:
        new_string[index-1] = string[i]
        index -= 1
        
        
print(''.join(new_string))
