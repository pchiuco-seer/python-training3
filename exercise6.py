"""def create_fib(input):
	fib_array = [1,1]	
	if input == 0:
		return [1]
	elif input == 1:
		return fib_array
	else:
		for i in xrange(2,input):
			fib_array.append(fib_array[i-1] + fib_array[i-2])
		for j in xrange(0,len(fib_array)):
			yield fib_array[j]"""

def fib(input):
	fib_array = [1,1]	
	if input == 0 or input == 1:
		return 1
	else:
		for i in xrange(2,input):
			fib_array.append(fib_array[i-1] + fib_array[i-2])
		return fib_array

number = int(raw_input("Enter number:"))
print fib(number)