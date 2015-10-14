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
		instances = {}
		for y in xrange(0,len(input[x])-1):
			if y < len(input[x])-2:
				if input[x][y] == input[x][y+1] and input[x][y+1] !=  input[x][y+2]:
					key = input[x][y:y+2]
					if key in instances.keys():
						instances[key] += 1
					else:
						instances[key] = 1
			else:
				if input[x][y] == input[x][y+1]:
					key = input[x][y]+input[x][y+1]
					if key in instances.keys():
						instances[key] += 1
					else:
						instances[key] = 1
		instances_per_word.append(instances)
	return instances_per_word	



list_input = ["apple","bub","dud","string"]
print unique_chars(list_input)
print same_char_instance(list_input)