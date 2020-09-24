import os
import random
import util
from collections import Counter
import re

class DirInfo(object):
	def __init__(self, filesInfo):
		self.filesInfo = filesInfo
		self.numberOfFiles = self.getNumberOfFiles()
		self.allExtensions = self.getAllExtensions()
		self.extensions = self.getExtensions()
		self.mostFrequentExtension = self.getMostFrequentExt()
		self.countOfExtension = self.getNumberOfEachFile()

	def getNumberOfFiles(self):
		return len(self.filesInfo)

	def getAllExtensions(self):
		allExtensions = []
		for f in self.filesInfo:
			s = f.extension.lower()
			s = s[1:]
			allExtensions.append(s)
		return allExtensions

	def getExtensions(self):
		exts = set(self.allExtensions)
		return list(exts)

	def getMostFrequentExt(self):
		data = Counter(self.allExtensions)
		return data.most_common(1)[0][0]

	def getNumberOfEachFile(self):
		countOfExtension = {}

		for ext in self.extensions:
			countOfExtension[ext] = 0

		for ext in self.allExtensions:
			countOfExtension[ext] += 1

		countOfExtensionSorted = sorted(countOfExtension.items(), key=lambda x: x[1], reverse=True)
		return countOfExtensionSorted

class FileInfo(object):
	def __init__(self, fileFullname , filepath, filename, extension, size):
		self.fileFullname = fileFullname
		self.filepath = filepath
		self.filename = filename
		self.extension = extension
		self.size = size

class FilePicker(object):
	def __init__(self):
		self.filesInfo = []
		self.filenamesPicked = []
		self.statsInfos = ""
		self.destFolderName = "testData"

	def setSrc(self, src):
		self.src = src

	def setDest(self, dest):
		self.dest = dest

	def setup(self):
		self.getFilesInfos()
		self.dInfos = DirInfo(self.filesInfo)
		self.dInfo.
		self.statsInfos = self.createStatsInfo()

	def setDefaultDest(self, src):
		self.defaultDest = self.getParentDirectory(src)+self.destFolderName

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
		self.filesInfo = util.getFilesInfos(self.src)

	def printFilesInfos(self):
		for f in self.filesInfo:
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