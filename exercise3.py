x = (1,2,3,4,5,6,7,8,9,10)
y = (10,20,30)

even_nums = [n*2 for n in x if n%2 == 0]
even_nums_by_two = [n*2 for n in x if n%2==0]
list_three = [n/m for n in y for m in x ]

print list_three
#print even_nums