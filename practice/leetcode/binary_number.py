number = 1234
binary_form = format(number, 'b')
count  = 0

binary_form = [int(i) for i in binary_form]
print(binary_form.count(1))