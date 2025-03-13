sentence="This is a common interview question"

frequency={}
for char in sentence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char]=1
        
sorted_table= sorted(frequency.items(),key=lambda x:x[1], reverse=True)
print(sorted_table[0][0])


        
