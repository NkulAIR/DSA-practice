def reverseBits(n): # -> int
    reversed = format(n, 'b')[::-1]
    return int(reversed, base=2)


# print(reverseBits(43261596)) # --> 964176192
print(reverseBits(2147483644)) # --> 1073741822



    # print(og_number) # -- > 00111111111111111111111111111110
    # print(reversed) # -- > 00111111111111111111111111111110