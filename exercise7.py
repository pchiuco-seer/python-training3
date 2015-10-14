def operate(list_input,**kwds):
	def sum_val():
		sum_val = 0
		for x in xrange(0,len(list_input)):
			sum_val += list_input[x]
		return sum_val

	def max_val():
		max_val = 0
		for x in xrange(0,len(list_input)):
			if list_input[x] > max_val:
				max_val = list_input[x]
		return max_val
		
	def min_val():
		min_val = 9999;
		for x in xrange(0,len(list_input)):
			if list_input[x] < min_val:
				min_val = list_input[x]
		return min_val

	def mean():
		mean_sum = sum_val()
		return mean_sum/float(len(list_input))

	def median():
		list_input.sort()
		length = len(list_input)
		return list_input[length/2]

	def mode():
		frequencies = {}
		for x in xrange(0,len(list_input)):
			#print frequencies
			if list_input[x] in frequencies.keys():
				
				frequencies[list_input[x]] += 1
			else:
				frequencies[list_input[x]] = 1

		mode_vals = []
		max_count = 0
		for x in frequencies.keys():
			if frequencies[x] > max_count:
				max_count = frequencies[x]
		for y in frequencies.keys():
			if frequencies[y] == max_count:
				mode_vals.append(y)
		return mode_vals

	output = {}
	output["sum"] = sum_val()
	output["max"] = max_val()
	output["min"] = min_val()
	output["mean"] = mean()
	output["median"] = median()
	output["mode"] = mode()
	
	if(kwds["ops"] in output.keys()):
		print output[str(kwds["ops"])]
	else:
		print "Invalid option"





print operate([1,2,2,1,3,4],ops='median')


"""
mean = ave
mode = most frequent
median = middle
"""