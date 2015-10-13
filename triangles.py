def print_triangle(height):
	ones = 1
	for h in range(0,height):
		line = ""
		for x in range(0,ones):
			line +=  '1'
		for y in range(0,height-ones):
			line += ' '
		ones += 1
		line += ''
		print line
	#return

input = int(raw_input("Enter height:"))
print_triangle(input)