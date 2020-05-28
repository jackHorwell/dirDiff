# Used to manipulate files and folders
import os
import shutil

# User input for file locations and destinations
dirA = input("Enter directory A: ")
dirB = input("Enter directory B: ")
destination = input("Enter location to create output folder: ")

# If the difference file already exists then it is deleted and recreated, else it is just created
newDir = destination + '\\difference'
if not os.path.exists(newDir):
    os.makedirs(newDir)
else:
    shutil.rmtree(newDir)
    os.makedirs(newDir)

# Tracks how many files have been found that match criteria
differentFiles = 0

# Iterates through dirA and checks dirB to see if it exists in both directories
# If it does not then it copies it to the output folder
for file in os.listdir(dirA):
    if file not in os.listdir(dirB):
        print(file)
        differentFiles += 1
        shutil.copy(dirA + '\\' + file, newDir)

print(f"{differentFiles} files found")