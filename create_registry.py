import os
import pooch

pooch.make_registry(os.path.dirname(__file__), "tmp_registry.txt")

with open('tmp_registry.txt', "r") as f, open('registry.txt', 'w') as g:
	for line in f.readlines():
		if "_files/" in line and "README" not in line:
			g.write(line)
			g.flush()

os.remove("tmp_registry.txt")
