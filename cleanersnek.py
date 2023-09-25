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


# remove files ending in .cpp
files = [f for f in files if (f.endswith(".cpp") or f.endswith(".bin")) and f != "algo.cpp" and f != "template.cpp" != "stdc++.h"]

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
