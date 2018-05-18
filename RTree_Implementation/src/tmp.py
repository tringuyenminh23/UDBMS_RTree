def load_text_file(file_path):
	"""Summary
	Load text file by lines
	Args:
	    file_path (String): 
	
	Returns:
	    list [String]: 
	"""
	with open(file_path) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	return content


file_path = "../data/xiye_test_1/Orderline_id.dat" 
xd = load_text_file(file_path)
print(len(xd))

new_path = "../data/xiye_test_1/Orderline_v.dat" 
with open(new_path, 'a') as f:
	for i in range(len(xd)):
		f.write(str(i) + "\n")
f.close()
