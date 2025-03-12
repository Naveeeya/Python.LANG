numbers={"1":"one",
         "2":"two",
         "3":"three",
         "4":"four",
         "5":"five",
         "6":"six",
         "7":"seven",
         "8":"eight",
         "9":"nine",
         "0":"zero"
}
phone_num= input("phone_num: ")
result=""
for number in phone_num:
    result= result+ numbers.get(number, "h")+ " "
print(result)
    
    
