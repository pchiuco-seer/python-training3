vals = []
input = ""
while input != 'end':
	input = raw_input("Enter a number:")
	if (input.isdigit()):
		vals.append(int(input))	
	

opt = raw_input("Enter an option:")

if opt == "km":
	converted_vals = map (lambda x: x*0.0000254,vals)
elif opt == "m":
	converted_vals = map (lambda x: x*0.0254,vals)
elif opt == "cm":
	converted_vals = map (lambda x: x*2.54,vals)
elif opt == "feet":
	converted_vals = map (lambda x: x*0.08333,vals)
elif opt == "yard":
	converted_vals = map (lambda x: x*0.02778,vals)
else:
	print "Invalid option"

print converted_vals



