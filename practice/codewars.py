def main():
    # print(digit_root(9))
    print(digit_root(942)) #--> 6
    # print(duplicate_encode("Success")) # ")())())"
    # print(number([[10,0],[3,5],[5,8]])) # ")())())"
    # print(filter_list([1, 2, 'a', 'b']))
    # print(filter_list([1, 2, "aasf", "1", "123", 123]))
    # print(dig_pow(89, 1)) # --> 1
    # print(dig_pow(41, 5)) # --> 25
    # print(dig_pow(89, 1)) # --> 25

    
# def duplicate_encode(word):
#     #your code here
#     word = word.upper()
#     new_word = []
#     for i in word:
#         if word.count(i) <= 1:
#             new_word.append("(")
#         elif word.count(i) > 1:
#             new_word.append(")")
        
#     return "".join(new_word)

# def number(bus_stops):
#     # Good Luck!
#     for bus_stop in bus_stops:
#         passengers = 1
#         new_passengers = bus_stop[0] - bus_stop[1]
#         if new_passengers <= 0:
#             new_passengers = bus_stop[0]
#             break
    
#     return new_passengers

# def dig_pow(n, p):
#     length = len(str(n))
#     powers = []
#     digits = [int(i) for i in str(n)]

#     for j in range(p, p+length):
#         powers.append(j)



#     for i,j in zip(digits, powers):
#         # 4 ** 2 AND 6 ** 1
#         print(i ** j)
    
#     print(digits, powers)


# def digit_root(n):
#     digits = [int(i) for i in str(n)]
#     total = 0
    
    
#     if len(digits) <= 1:
#         return n
    
#     for i in digits:
#         total += i
    
#     return digit_root(total)

def fib_prod(n) # -> int:

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1




# def filter_list(l):
#     'return a new list with the strings filtered out'
#     new_list = []
#     for num in l:
#         if type(num) == int:
#             new_list.append(num)
#     return new_list

main()