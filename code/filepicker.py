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
		self.dInfos = None
		self.dInfosControl = []
		self.defaultFolderName = "_file"
		self.destfolderName = ""
		self.defaultDestination = ""
		self.destEntryBox = ""
		self.ext = ""
		self.fInfoPicked = []
		self.pathFileToCopy = []
		self.pathFileCopied = []

	def setup(self):
		self.dInfos = DirInfo()
		fInfos = self.getFilesInfos()
		self.dInfos.init(fInfos)

	def pick(self, ext):
		self.ext = ext
		self.generateFolderName(self.ext)
		self.generateFinalDest()
		util.makeDir(self.dest)

		if not self.fInfoPicked:
			self.pickFilesInfo()
		else:
			self.fInfoPicked.clear()
			self.pickFilesInfo()

		if not self.pathFileToCopy:
			self.generatePathFileToCopy()
		else:
			self.pushCopiedFile()
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

	def generateFinalDest(self):
		if(self.destEntryBox == ""):
			folderDest = self.setDefaultDest(self.src)
			self.dest = folderDest+self.destFolderName
		else:
			self.dest = self.destEntryBox+self.destFolderName

	def generateFolderName(self, ext):
		self.destFolderName = ext+self.defaultFolderName

	def pushCopiedFile(self):
		self.pathFileCopied.append(self.pathFileToCopy)
		self.pathFileToCopy.clear()

	def pushDirInfo(self):
		 self.dInfosControl.append(self.dInfos)

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