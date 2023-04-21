import os
import pooch

pooch.make_registry(os.path.dirname(__file__), "tmp_registry.txt")
f = open('tmp_registry.txt')
g = open('registry.txt', 'w')
for line in f.readlines():
    if "_files/" in line:
            g.write(line)

g.flush()
g.close()

os.remove("tmp_registry.txt")
