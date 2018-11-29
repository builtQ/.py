# import os
# root_path = os.getcwd()
# #print(root_path)
# offset = len(root_path.split("\\"))
# for root,files,dirs in os.walk(root_path):
# 	current_dir = root
# 	path_list = current_dir.split("\\")
# 	indent_level = len(path_list) - offset 
# 	print("\t"*indent_level,"\\",path_list[-1])
# 	print(files)
# 	print(dirs)
# 	for f in files:
# 		print(f)
# 	for d in dirs:
# 	 	#print(d)
# 	 	dirs_name = os.path.splitext(d)[0]
# 	 	dirs_path = os.path.join(root,d)
# 	 	print(dirs_path)
file_path = r'C:\Users\Administrator\Desktop\root\dir1\cp4_find_max.c'
	# print(dirs_path)
def line_count(file_path):
 	code_line,blank_line = 0,0
 	with open(file_path,'r') as fp:
 		while True:
 			line = fp.readline()
 			if not line:
 				break
 		
 			code_line += 1
 	print(code_line,"lines")
line_count(file_path)