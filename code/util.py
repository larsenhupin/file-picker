import os
from distutils.dir_util import copy_tree
import shutil
import filepicker as fp

def getCurrentDirectory():
		cd = os.getcwd()
		return cd

def getFilesInfos(source):
	filesInfos = []

	for dirpath, dirnames, fnames in os.walk(source):
		for f in fnames:
			fileFullname = os.path.join(dirpath, f)
			filename, ext = os.path.splitext(f)
			size = os.path.getsize(fileFullname)
			filesInfos.append(fp.FileInfo(fileFullname, dirpath, filename, ext, size))

	return filesInfos

def copy_files(source, destination):
	filesname = copy_tree(source, destination, 1, 1, 1, 1)

def retrievefilename(source):
	return os.listdir(source)

def printfilename(source):
	for filename in os.listdir(source):
		print(filename[1])
	return

def changeDir(path):
	os.chdir(path)

def makeDir(dirname):
	i=0
	while True:
		try:
			if(i == 0):
				
				os.mkdir(dirname+"/")
			else:
				os.mkdir(dirname + " ("+str(i)+")/")
			break
		except FileExistsError:
			i+=1

def hashNumeral(self, value):
	twoDigits = []
	for i in range(1, value):
		if(i < 10):
			twoDigits.append("0"+str(i))
		else:
			twoDigits.append(str(i))
	return twoDigits