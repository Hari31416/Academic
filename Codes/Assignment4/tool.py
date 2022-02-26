import os

folders = os.listdir(os.curdir)
folders = filter(lambda x:"." not in x, folders)
for i, folder in enumerate(folders):
	file = os.path.join(folder, "control.in")
	with open(file) as f:
		t = f.read()
		os.remove(file)
		or_text = "output dos -20 20 10000 0.01"
		new_text = "output dos -20 20 10000 0.0"+ str(i)
		t_new = t.replace(or_text, new_text)
	
		with open(file, "w") as f:
			f.write(t_new)
		print("Done folder", folder)
