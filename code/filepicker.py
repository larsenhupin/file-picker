import os
import random
import util
from collections import Counter
import re

class FileInfo(object):
	def __init__(self, fileFullname , filepath, filename, extension, size):
		self.fileFullname = fileFullname
		self.filepath = filepath
		self.filename = filename
		self.extension = extension
		self.size = size

class DirInfo(object):
	def __init__(self):
		self.fInfos = []
		self.countOfExtension = 0
		self.numberOfFiles = 0
		self.allExtensions = []
		self.extensions = []
		self.mostFrequentExtension = ""
		self.statsInfo = ""

	def init(self, fInfos):
		self.fInfos = fInfos
		self.getNumberOfFiles()
		self.getAllExtensions()
		self.getExtensions()
		self.getMostFrequentExt()
		self.getNumberOfEachFile()
		self.createStatsInfo()

	def createStatsInfo(self):
		s = []
		s.append("all: " + str(self.numberOfFiles))
		for k, v in self.countOfExtension:
			s.append("" + k + ": " + str(v))
		self.statsInfo = s

	def getNumberOfFiles(self):
		self.numberOfFiles = len(self.fInfos)

	def getAllExtensions(self):
		allExtensions = []
		for f in self.fInfos:
			s = f.extension.lower()
			s = s[1:]
			allExtensions.append(s)
		self.allExtensions = allExtensions

	def getExtensions(self):
		exts = set(self.allExtensions)
		self.extensions = list(exts)

	def getMostFrequentExt(self):
		data = Counter(self.allExtensions)
		self.mostFrequentExtension = data.most_common(1)[0][0]

	def getNumberOfEachFile(self):
		countOfExtension = {}
		for ext in self.extensions:
			countOfExtension[ext] = 0

		for ext in self.allExtensions:
			countOfExtension[ext] += 1

		countOfExtensionSorted = sorted(countOfExtension.items(), key=lambda x: x[1], reverse=True)
		self.countOfExtension = countOfExtensionSorted

class FilePicker(object):
	def __init__(self):
		self.src = ""
		self.dest = ""
		self.ext = ""
		self.dInfos = None

		self.backup = []

		self.defaultFolderName = "_file"
		self.defaultPath = ""
		self.destfolderName = ""
		self.destEntryBox = ""

		self.fInfoPicked = []
		self.pathFileToCopy = []

	def setup(self):
		self.dInfos = DirInfo()
		fInfos = self.getFilesInfos()
		self.dInfos.init(fInfos)

	def pick_file(self, ext):
		self.ext = ext
		self.setFolderName(self.ext)
		self.setFinalDest()
		util.makeDir(self.dest)



		if not self.fInfoPicked:
			self.pickFilesInfo()
		else:
			self.fInfoPicked.clear()
			self.pickFilesInfo()

		if not self.pathFileToCopy:
			self.generatePathFileToCopy()
		else:
			self.pushToBackup("copyTree")
			self.generatePathFileToCopy()

		util.copy_files(self.pathFileToCopy)
	
	def pickFilesInfo(self):
		for f in self.dInfos.fInfos:
			if(f.extension == "."+self.ext):
				self.fInfoPicked.append(f)

	def generatePathFileToCopy(self):
		for f in self.fInfoPicked:
			self.pathFileToCopy.append((f.fileFullname, self.dest+"/"+f.filename+f.extension))

		print(self.pathFileToCopy)

	def setFinalDest(self):


		print(self.destEntryBox)

		if(self.destEntryBox == "/"):
			print("PATATE")
			folderDest = self.getParentDirectory(self.src)
			print(folderDest)
			self.dest = folderDest+self.destFolderName
		else:
			self.dest = self.destEntryBox+self.destFolderName

	def setFolderName(self, ext):
		self.destFolderName = ext+self.defaultFolderName

	def pushToBackup(self, tag):
		if(tag == "dInfo"):
			self.backup.append(self.dInfos)
		if(tag == "copyTree"):
			self.backup.append(self.pathFileToCopy)
			self.pathFileToCopy.clear()

	def setDefaultDest(self, src):
		return self.getParentDirectory(src)

	def setSrc(self, src):
		self.src = src

	def setDest(self, dest):
		self.dest = dest

	def getParentDirectory(self, s):
		i = 0
		for c in reversed(s):
			i+=1
			if(c == '/'):
				return s[:len(s)-i+1]

	def generateRandomFile(self):
		self.filenamesPicked  = random.sample(self.listFilenames, self.numberOfFiles)
		self.printfilename(self.filenamesPicked)

		for item in self.filenamesPicked:
			filename = os.path.basename(item)
			copyfile(item, os.path.join(self.destPath, filename))

	def getFilesInfos(self):
		return util.getFilesInfos(self.src)

	def printFilesInfos(self, filesInfo):
		for f in filesInfo:
			print("{0}{1}{2} -> {3}".format(f.filepath,f.filename,f.extension, f.size))

	def createStatsInfo(self):
		s = []
		s.append("all: " + str(self.dInfos.numberOfFiles))
		for k, v in self.dInfos.countOfExtension:
			s.append("" + k + ": " + str(v))

		return s

	def getCurrentDirectory(self):
		path = os.getcwd()
		return path