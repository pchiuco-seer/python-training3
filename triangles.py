def print_half_triangle(height):
	ones = 1
	for h in xrange(0,height):
		line = ""
		for x in xrange(0,ones):
			line +=  '1'
		for y in xrange(0,height-ones):
			line += ' '
		ones += 1
		line += ''
		print line

def print_pyramid_a(height):
	index = 1
	for h in xrange(0,height):
		line = ""
		for x in xrange(0,(height - (h+1))):
			line += ' '
		for y in xrange(0,index):
			line += '1'
		for z in xrange(0,(height - (h+1))):
			line += ' '
		index += 2
		print line

def print_pyramid_b(height):
	index = 1
	for h in xrange(0,height):
		line = ""
		for x in xrange(0,(height - (h+1))):
			line += ' '
		for y in xrange(0,index):
			if y % 2 == 0:
			    line += '1'
			else:
				line += ' '
		for z in xrange(0,(height - (h+1))):
			line += ' '
		
		index += 2
		print line


input = int(raw_input("Enter height:"))
print_half_triangle(input)
print '\n'
print_pyramid_a(input)
print '\n'
print_pyramid_b(input)