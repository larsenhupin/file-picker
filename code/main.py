import filepicker as fp
import util

class Controller():
	def __init__(self):
		self.options = sys.argv[1]
		self.fp = fp.FilePicker()

	def setup(self):
		pass

	def handle_click(self, event):
		pass

	def pick(self):
		self.setDestPath()
		choosenExt = self.v.getChoosenExt()
		self.fp.pick_file(choosenExt)

	def setDestPath(self):
		self.fp.destEntryBox = ""

	# ------------------------------------------------------------------------	

	def GenerateRandom(self):
		numberOfFile = None
		self.fp.ext = self.v.extComboBoxRandom.get()
		if(self.v.nombreRandomEntry.get() is not ''):
			numberOfFile = int(self.v.nombreRandomEntry.get())
		elif(self.v.nombreRandomEntry.get() is ''):
			numberOfFile = 0

		self.fp.currentDirectory = self.v.pathRandomEntryBox.get()
		self.fp.destPath = self.v.pathDestEntryBoxRandom.get()
		self.fp.setNumberOfFile(numberOfFile)
		self.fp.main()

	# ------------------------------------------------------------------------

if __name__ == '__main__':
	c = Controller()
