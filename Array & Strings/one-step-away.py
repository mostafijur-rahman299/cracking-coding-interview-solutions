def one_edit_away(string1, string2):
    if len(string1) == len(string2):
        one_edit_replace(string1, string2)
    if len(string1) + 1 == len(string2):
        one_edit_insert(string1, string2)
    if len(string1) - 1 == len(string2):
        one_edit_insert(string2, string1)
        
        
def one_edit_replace(string1, string2):
    find_difference = False
    for i in range(string1):
        if string1[i] == string2[i]:
            if find_difference:
                return False
            find_difference = True
    return True


def one_edit_insert(string1, string2):
    index1 = 0
    index2 = 0
    
    while index2 < len(string2) and index1 < len(string2):
        if(string1[index1] != string2[index2]):
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    return True
