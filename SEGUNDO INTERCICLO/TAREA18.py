larguest_so_far=-1
print('Before', larguest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > larguest_so_far:
        larguest_so_far = the_num
    print(larguest_so_far, the_num)
print('After', larguest_so_far)