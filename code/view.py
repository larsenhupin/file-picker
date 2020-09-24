from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import filepicker as fp
import util

class View():
	def __init__(self,c):
		self.c=c
		self.root = Tk()
		self.root.title("File picker")
		self.root.resizable(width=False,height=False)
		self.root.geometry("475x250+550+250")
		self.root.iconbitmap("../assets/eye.ico")
		self.frameMenu = Frame(self.root)
		self.frameProgram = Frame(self.root, width=475, height=250)

	def init(self):
		self.init_menu_window()
		self.init_program_window()

	def init_menu_window(self):
		self.programButton = Button(self.frameMenu, text='File Picker',width=15,height=3)
		self.programButton.grid(row=10,column=1, pady=100)

	def init_program_window(self):
		self.pathSrcText = Label(self.frameProgram, text="Source:")
		self.pathSrcText.grid(row=0, column=0, padx=0, sticky='w')
		self.pathSrcEntryBox = Entry(self.frameProgram, textvariable="5", width=50)
		self.pathSrcEntryBox.grid(row=0, column=1, columnspan=2, padx=0, pady=0, sticky='e')
		self.pathSrcEntryBox.configure(state="readonly", readonlybackground="white")
		self.pathSrcButton = Button(self.frameProgram, text='...', width=5, height=1)
		self.pathSrcButton.grid(row=0, column=3, padx=(30,0), sticky='e')
		
		self.pathDestText = Label(self.frameProgram, text='Destination:')
		self.pathDestText.grid(row=1, column=0,padx=0, sticky='w')
		self.pathDestEntryBox = Entry(self.frameProgram, textvariable='6', width=50)
		self.pathDestEntryBox.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky='w')
		self.pathDestEntryBox.configure(state="readonly", readonlybackground="white")
		self.pathDestButton = Button(self.frameProgram, text='-->', width=5, height=1, state="disable")
		self.pathDestButton.grid(row=1, column=3,padx=0, sticky='e')

		# ------------------------------------------------------------------------------------------------
		# Radio Button
		self.sameTypeLabel = Label(self.frameProgram, text='All of choosen types:')
		self.sameTypeLabel.grid(row=5, column=2, sticky='w')

		self.isAll = IntVar(value=1)
		self.sameTypeCheckbox = Checkbutton(self.frameProgram, variable=self.isAll)
		self.sameTypeCheckbox.grid(row=5, column=3, sticky='e')

		self.PickRandomLabel = Label(self.frameProgram, text='Pick random:')
		self.PickRandomLabel.grid(row=6, column=2, sticky='w')
		
		self.isRandom = IntVar()
		self.pickRandomCheckbox = Checkbutton(self.frameProgram, variable=self.isRandom)
		self.pickRandomCheckbox.grid(row=6, column=3, sticky='e')

		# ------------------------------------------------------------------------------------------------

		self.numberRandomText = Label(self.frameProgram, text='Number of files:')
		self.numberRandomText.grid(row=7, column=2,padx=0,pady=0,sticky='w')
		self.numberRandomEntry = Entry(self.frameProgram, textvariable="7", width=10, state="disable")
		self.numberRandomEntry.grid(row=7, column=3,padx=0,pady=0,sticky='e')

		self.extDerouleText = Label(self.frameProgram, text="Extensions :")
		self.extDerouleText.grid(row=8, column=2, sticky='w', padx=0, pady=0)

		self.extComboBox = ttk.Combobox(self.frameProgram, width=5, state='disable')
		self.extComboBox.grid(row=8, column=3, sticky='e')

		# ------------------------------------------------------------------------------------------------

		self.infoText = Text(self.frameProgram, width=25, height=10)
		self.infoText.configure(state='disable')

		self.infoListbox = Listbox(self.frameProgram, width=25, height=10)
		self.infoListbox.grid(row=5, column=0, rowspan=6, columnspan=2, sticky='w')
		self.infoListbox.configure(bd=1, relief="sunken", highlightthickness=0, selectbackground="white", selectforeground="black", activestyle ="none")

		self.pickButton = Button(self.frameProgram,text='Pick', width=10)
		self.pickButton.grid(row=9, column=2, columnspan=2, sticky='e')

	def getIsAllCheckbox(self):
		self.isRandom.set(0)
		self.numberRandomEntry.configure(state="disable")

	def getIsRandomCheckbox(self):
		self.isAll.set(0)
		if(self.isRandom.get()):
			self.numberRandomEntry.configure(state="normal")
		else:
			self.numberRandomEntry.configure(state="disable")

	def updateExtComboBox(self):
		self.extComboBox.config(state="readonly", values=self.c.fp.stats.extensions)
		self.extComboBox.set(self.c.fp.stats.mostFrequentExtension)

	def afficherMenu(self):
		self.frameMenu.pack()
		self.frameProgram.pack_forget()

	def displayProgram(self):
		self.frameProgram.pack()
		self.frameMenu.pack_forget()


	# Here's lies the problem -------------------------------------
	def open_directory_src(self):
		source = filedialog.askdirectory()
		if(source):

			self.pathDestButton.config(state="normal")
			self.pathSrcEntryBox.config(state='normal')
			self.pathSrcEntryBox.delete(0, END)
			self.pathSrcEntryBox.insert(0, source)
			self.pathSrcEntryBox.config(state="readonly")
			# --------------------------------------------------
			self.c.fp.source = source
			self.c.fp.dest = self.c.fp.getParentDirectory(source)
			
			self.pathDestEntryBox.config(state='normal')
			self.pathDestEntryBox.delete(0, END)
			self.pathDestEntryBox.insert(0, self.c.fp.dest)
			self.pathDestEntryBox.config(state="readonly")
			
			
			self.c.fp.setup()
			self.updateExtComboBox()

			self.infoListbox.configure(state='normal')
			for s in self.c.fp.statsInfos:	
				self.infoListbox.insert(END, s)

	# ------------------------------------------------------------

	def open_directory_dest(self):
		self.pathDest = filedialog.askdirectory()
		self.pathDestEntryBox.config(state='normal')
		self.pathDestEntryBox.delete(0, END)
		self.pathDestEntryBox.insert(0, self.pathDest)
		self.pathDestEntryBox.config(state="readonly")