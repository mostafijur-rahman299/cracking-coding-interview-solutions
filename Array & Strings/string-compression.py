
string = "aabcccccaaa"
expected_answer = "a2b1c5a3"

compressed_str = ""
consecutive = 0

for index in range(len(string)):
    consecutive += 1
    
    if index + 1 >= len(string) or string[index] != string[index+1]:
        compressed_str = compressed_str + string[index] + str(consecutive)
        consecutive = 0
    
print(compressed_str)