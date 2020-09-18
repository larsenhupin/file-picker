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
		self.v.root.mainloop()

	def setup(self):
		pass

	def handle_click(self, event):
		pass

	def bindEvents(self):
		
		self.v.boutonRandom.config(command=self.v.displayProgram)
		#self.v.pathRandomEntryBox.bind("<1>", self.handle_click)
		self.v.sameTypeCheckbox.config(command=self.v.getIsAllCheckbox)
		self.v.pickRandomCheckbox.config(command=self.v.getIsRandomCheckbox)
		self.v.pathRandomButton.config(command=self.v.open_directory_random)
		self.v.destRandomButton.config(command=self.v.open_directory_destRandom)
		self.v.generateRandomButton.config(command=self.GenerateRandom)

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
