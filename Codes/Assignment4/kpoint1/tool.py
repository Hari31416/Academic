import os

folders = os.listdir(os.curdir)
folders = filter(lambda x:"." not in x, folders)
for i, folder in enumerate(folders):
	file = os.path.join(folder, "control.in")
	with open(file) as f:
		t = f.read()
		os.remove(file)
		or_text = "harikesh"
		new_text = str(i+1)
		t_new = t.replace(or_text, new_text)
	
		with open(file, "w") as f:
			f.write(t_new)
		print("Done folder", folder)
