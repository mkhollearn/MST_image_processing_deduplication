import pandas as pd


df = pd.read_csv('input.csv')


extract = {}

from collections import defaultdict

difficulty_map = defaultdict(dict)

def read_map(file_name, set_num):
	with open(file_name, 'r') as f:
		for line in f:
			line = line.strip()
			obj_num = line.split()[0].strip()
			diff = line.split()[1].strip()
			difficulty_map[set_num][obj_num] = diff

def get_difficulty(name, set_num: int):
	set_num = str(set_num).lower()
	if '_' in name:
		obj_num = str(int(name.split("_")[0].strip("a").strip("b")))
	else:
		obj_num = str(int(name.split(".")[0].strip("a").strip("b")))
	
	print(set_num, obj_num)
	return difficulty_map[set_num][obj_num]

read_map('set1.txt','1')
read_map('set2.txt','2')
read_map('set3.txt','3')
read_map('set4.txt','4')
read_map('set5.txt','5')
read_map('set6.txt','6')
read_map('setc.txt','c')
read_map('setd.txt','d')
read_map('sete.txt','e')
read_map('setf.txt','f')


print(df.columns)
df['Lure Rating'] = df.apply(lambda row: get_difficulty(row['MDT-O '], row['Set #']), axis=1)
print(df.head())

df.to_csv('input_with_lure_ratings.csv')
