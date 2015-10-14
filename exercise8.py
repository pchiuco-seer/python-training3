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
		unique = set(input[x])
		instances = {}
		for z in unique:
			groups = input[x].split(z)
			groups = [i for i in groups if i != '']
			for y in groups:
				if len(y) == 2:
					if y in instances.keys():
						instances[y] += 1
					else:
						instances[y] = 1
		instances_per_word.append(instances)
	return instances_per_word	



list_input = ["apple","bub","dud","string","10010001001"]


print unique_chars(list_input)
print same_char_instance(list_input)