import os
import shutil
# remove file from directory of this script, ending in .cpp
# but not algo.cpp and template.cpp

# get current directory
path = os.getcwd()

# get all files in current directory
files = os.listdir(path)


#
# 아무 생각 없이 수정하고 실행하면 매우매우매우매우매우매우 위험한 결과가 발생할 수 있음!!!!!!!!!!!!!!!!!!!!!!!!!
#

originalfiles = ["algo.cpp", "template.cpp", "template.py", "cleanersnek.py",
				"snek.py", ".gitignore", "README.md", ".cph", ".git", "bits"]

# remove files ending in .cpp
files = [f for f in files if not f in originalfiles]

for f in files:
	os.remove(f)
	print("removed " + f)

# copy template.cpp to algo.cpp
shutil.copyfile("template.cpp", "algo.cpp")
shutil.copyfile("template.py", "snek.py")
print("template copied")

# remove all files in .cph directory
path = path + "/.cph"

# if .cph directory exists
if os.path.exists(path):
	files = os.listdir(path)
	for f in files:
		os.remove(path + "/" + f)
		print("removed " + f)
else:
	os.mkdir(path)
	print("created .cph directory")