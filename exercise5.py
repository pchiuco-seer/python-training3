s = ['c','a','t','b']
c = ['c','a','t']

def not_in_c(input,c):
	output = input in c
	return not output

output = [n for n in s if not_in_c(n,c)]
print output


str_in = "Door broom mice."
def in_dups(input, dups):
	if(input in dups):
		return True
	else:
		dups.append(input)
		return False
	

def clear_duplicates(input):
	dups = []
	out = ""
	unique = [x for x in input if not in_dups(x,dups)]
	for i in range(0,len(unique)):
		out += unique[i]
	return out
	"""
	for x in range(0, len(input)):
		if(input[x] in dups):
			continue
		else:
			dups.append(input[x])
	print dups
	for x in range(0,len(dups)):
		out += dups[x]
	return out
	"""

out_put = ""
delimeter = [' ','.','?','!']
buff = ""

for x in range(0,len(str_in)):
	if str_in[x] in delimeter:
		out_put = out_put + clear_duplicates(buff)+str_in[x]
		buff = ""
	else:
		buff += str_in[x]
print out_put


