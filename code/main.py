import filepicker as fp
import util
import view

class Controller():
	def __init__(self):
		self.fp = fp.FilePicker()
		self.v = view.View(self)
		self.v.init()
		self.bindEvents()
		self.v.displayProgram()
		# Temporary
		self.v.afficherMenu()
		# ---------
		self.v.root.mainloop()

	def setup(self):
		pass

	def handle_click(self, event):
		pass

	def bindEvents(self):
		self.v.programButton.config(command=self.v.displayProgram)
		self.v.sameTypeCheckbox.config(command=self.v.getIsAllCheckbox)
		self.v.pickRandomCheckbox.config(command=self.v.getIsRandomCheckbox)
		self.v.pathSrcButton.config(command=self.v.open_directory_src)
		
		self.v.pathDestButton.config(command=self.v.open_directory_dest)

		#self.v.pickButton.config(command=self.GenerateRandom)
		#self.v.pathRandomEntryBox.bind("<1>", self.handle_click)

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
