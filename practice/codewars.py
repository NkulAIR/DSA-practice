def main():
    # print(duplicate_encode("Success")) # ")())())"
    print(number([[10,0],[3,5],[5,8]])) # ")())())"

    
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

def number(bus_stops):
    # Good Luck!
    for bus_stop in bus_stops:
        passengers = 1
        new_passengers = bus_stop[0] - bus_stop[1]
        if new_passengers <= 0:
            new_passengers = bus_stop[0]
            break
    
    return new_passengers


main()