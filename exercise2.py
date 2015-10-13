vals = []
input = ""
output = {}
while input != 'end':
	input = raw_input("Enter a number:")
	if (input.isdigit()):
		vals.append(int(input))	

output["m"] = map (lambda x: x*0.0254,vals)
output["km"] = output["m"]/1000
output["cm"] = output["m"]*100
output["feet"] = map (lambda x: x*0.08333,vals)
output["yard"] = map (lambda x: x*0.02778,vals)

opt = str(raw_input("Enter an option:"))

if(opt in output.keys()):
	print output[str(opt)]
else:
	print "Invalid option"





