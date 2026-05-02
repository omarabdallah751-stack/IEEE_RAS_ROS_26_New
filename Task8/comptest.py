#A. Your Name
# times = int(input("Enter number of tests: "))

# i = 0

# while i < times:
#     n = input("Enter letters count: ") 
#     word1 = input("Enter first word: ")
#     word2 = input("Enter second word: ")
    
#     if sorted(word1) == sorted(word2):
#         print("YES")
#     else:
#         print("NO")
        
#     i = i + 1




#B.Spy Detected
# times = int(input("Enter number of tests: "))

# while times > 0:
#     n = int(input("Enter numbers count: ")) 
#     list = []
    
#     for i in range(n):
#         num = int(input("Enter number: "))
#         list.append(num)

#     print(list)

#     for i in range(n):
#         if list.count(list[i]) == 1:
#             print(f"the different number is: {list[i]}" )
#             break 
            
#     times -= 1
        
        

#C. Way Too Long Words
# times = int(input("Enter number of words: "))

# i = 0
# while i < times:
#     word = input("Enter word: ")
    
#     length = len(word)
    
#     if length > 10:
#         first_letter = word[0]
#         last_letter = word[-1]
#         middle_count = length - 2
        
#         print(f"{first_letter}{middle_count}{last_letter}")
#     else:
#         print(word)
        
#     i = i + 1





#D. Sum
# times = int(input("Enter number of tests: "))

# i = 0
# while i < times:
#     a = int(input("Enter first number (a): "))
#     b = int(input("Enter second number (b): "))
#     c = int(input("Enter third number (c): "))
    
#     if a + b == c:
#         print("YES")
#     elif a + c == b:
#         print("YES")
#     elif b + c == a:
#         print("YES")
#     else:
#         print("NO")
        
#     i = i + 1





#E. Division
# times = int(input("Enter number of tests: "))

# i = 0
# while i < times:
#     rating = int(input("Enter rating: "))
    
#     if rating >= 1900:
#         print("Division 1")
#     elif 1600 <= rating <= 1899:
#         print("Division 2")
#     elif 1400 <= rating <= 1599:
#         print("Division 3")
#     else:
#         print("Division 4")
        
#     i = i + 1



#F. Team
# n = int(input("Enter number of problems: "))

# solved_count = 0

# i = 0
# while i < n:
#     petya = int(input("Petya: "))
#     vasya = int(input("Vasya: "))
#     tonya = int(input("Tonya: "))
    
#     total = petya + vasya + tonya
    
#     if total >= 2:
#         solved_count = solved_count + 1
        
#     i = i + 1

# print(solved_count)




#G. Tram
# n = int(input("Enter number of stops: "))

# current_passengers = 0  
# max_capacity = 0        

# i = 0
# while i < n:
#     exit_people = int(input("Exit: "))
#     enter_people = int(input("Enter: "))
    
#     current_passengers = current_passengers - exit_people + enter_people
    
#     if current_passengers > max_capacity:
#         max_capacity = current_passengers
        
#     i = i + 1

# print(max_capacity)




#H. Plus One on the Subset






















#I. George and Accommodation
# n = int(input("Enter number of rooms: "))

# available_rooms = 0

# i = 0
# while i < n:
#     p = int(input("People already living there: "))
#     q = int(input("Room capacity: "))
    
#     if (q - p) >= 2:
#         available_rooms += 1
        
#     i = i + 1

# print(available_rooms)




#J. Borze
symbol = input("Enter Borze code: ")

result = ""

i = 0
while i < len(symbol):
    if symbol[i] == ".":
        result += "0"
        i = i + 1
    elif symbol[i] == "-":
        if symbol[i+1] == ".":
            result += "1"
        else:
            result += "2"
        i = i + 2

print(result)