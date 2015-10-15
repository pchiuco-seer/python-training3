def palindrome_list(func):
	def inner(list_input):
		palindrome_list = []
		for x in list_input:
			reverse = x[::-1]
			if x == reverse:
				palindrome_list.append(x)
		return func(palindrome_list)
	return inner
	
@palindrome_list
def unique_chars(input):
	output = [len((set(word))) for word in input]
	return output

@palindrome_list
def same_char_instance(input):
	instances_per_word = []

	for x in xrange(0,len(input)):
		str_buffer = input[x][0]
		curr = input[x][0]
		y = 1
		instances = {}
		while y < len(input[x]):
			print y
			if input[x][y] == curr:
				str_buffer += input[x][y]
				if y == len(input[x])-1:
					if len(str_buffer) == 2:
						if str_buffer in instances.keys():
							instances[str_buffer] += 1
						else:
							instances[str_buffer] = 1
				y += 1
			else:
				curr = input[x][y]
				if len(str_buffer) == 2:
					if str_buffer in instances.keys():
						instances[str_buffer] += 1
					else:
						instances[str_buffer] = 1
				str_buffer = curr
				y += 1
			print str_buffer
		instances_per_word.append(instances)
	return instances_per_word	

list_input = ["aabbccbbaa","apple","bub","dud","string","10010001001"]

print unique_chars(list_input)
print same_char_instance(list_input)
