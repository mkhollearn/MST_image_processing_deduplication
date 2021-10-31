import numpy as np
import pandas as pd

df = pd.read_csv("input2.csv")

columns = df.columns
print(columns)

sa = set(df['Notes'])
#sa.remove(np.nan)
print("All Notes:",sa)

df['notes2'] = ['delete' if type(v) == str else 'save' for v in df['Notes'].values]

print("Total number of rows",df.shape[0])
print('Number of deletes:',df[df['notes2'] == 'delete'].shape[0])
print('Number of saves  :',df[df['notes2'] == 'save'].shape[0])

df = df[df['notes2'] == 'save']

df['Object'] = [o.lower().strip() for o in df['Object'].values]
df['hash'] = [v[0:3] for v in df['MDT-O '].values]
df['hash'] = df['hash'] + '-' + df['Set #']

print(df.head())

from collections import defaultdict
pair_map = defaultdict(set)

for index, row in df.iterrows():
	pair_map[row['hash']].add(row['Object'])	

possible_image_names = set(df['Object'])


final_selection = []
for image_name in possible_image_names:
	print("Searching for pairs that match:",image_name)
	# 1. get a set of images that match this image name
	found = []
	for hsh, images in pair_map.items():
		if image_name in images:
			print(" -- Found:", hsh, images)
			found.append(hsh)	

	if len(found) == 0:
		continue

	# 2. if that image set only matches 1, then we go ahead and grab this
	# then delete that image 
	if len(found) == 1:
		print(" ---- Found only 1 ...")
		final_selection.append(found[0])
		print(" ---- Deleting:",found[0])
		del pair_map[found[0]]
		continue

	# 3. if there are more than one, then just shuffle the list and grab one
	# and then delete the other ones from possible findings
	final_selection.append(found[0])
	for f in found:
		print("Deleting:",f)
		del pair_map[f]

print(final_selection)

df = df[df['hash'].isin(final_selection)]

df.to_csv('final_output2.csv')

print(df)

hashes = df['hash'].values
from collections import defaultdict
count_dict = defaultdict(int)
for hash_val in hashes:
	count_dict[hash_val] += 1

for key, value in count_dict.items():
	if value != 2:
		print(f"UH OH!: {key} has only {value} images!")



