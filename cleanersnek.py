import os
import shutil
# remove file from directory of this script, ending in .cpp
# but not algo.cpp and template.cpp

# get current directory
path = os.getcwd()

# get all files in current directory
files = os.listdir(path)



# remove files ending in .cpp
files = [f for f in files if f.endswith(".cpp") and
f != "algo.cpp" and f != "template.cpp"]

# remove 
files = [f for f in files if f != "algo.cpp" and f != "template.cpp"]
for f in files:
	os.remove(f)
	print("removed " + f)

# copy template.cpp to algo.cpp
shutil.copyfile("template.cpp", "algo.cpp")
print("copied template.cpp to algo.cpp")

# remove all files in .cph directory
path = path + "/.cph"
files += os.listdir(path)
for f in files:
	os.remove(path + "/" + f)
	print("removed " + f)
