import os
import glob 	# Global
path_list = ['D:\EPILEPSY_PROJECT\VS SCREENING']

mypath = path_list[0]
print(mypath)

print ("Directory path detected \n")



#read all filenames in the dir

file_list = os.listdir(mypath)
print(file_list)



#collecting the total number of log files in the directory.
for i in file_list:
	print(i)
	num_files = len(glob.glob1(mypath+'\\'+i,"*log*.log"))
	list_log = list(glob.glob1(mypath+'\\'+i,"*log*.log"))
	ef = {}
	with open('output.txt','a+') as data:
		for n in list_log:
			with open(f'{mypath}\\{i}\\{n}') as file:
				temp = file.read().split('\n')
				final = temp[temp.index('-----+------------+----------+----------')+1].split('  ')
				ef.update({f'{final[5]}':f"{n}"})
		keys = list(ef.keys())
		for num in range(0,5):
				# print(keys)
				top = max(keys)
				print(top)
				data.write(f'{i}\t{top}\t{ef.get(top)}\n')
				keys.pop(keys.index(top))
		data.write('\n')

	print('There are',num_files, 'log files in the current directory\n\n')