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
		self.frameRandom = Frame(self.root, width=475, height=250)

	def init(self):
		self.init_window()
		self.init_random_window()

	def init_window(self):
		self.boutonRandom = Button(self.frameMenu, text='Random',width=15,height=3)
		self.boutonRandom.grid(row=10,column=1,  pady=100)

	def init_random_window(self):
		self.pathRandomText = Label(self.frameRandom, text="Source:")
		self.pathRandomText.grid(row=0, column=0, padx=0, sticky='w')
		self.pathRandomEntryBox = Entry(self.frameRandom, textvariable="5", width=50)
		self.pathRandomEntryBox.grid(row=0, column=1, columnspan=2, padx=0, pady=0, sticky='e')
		self.pathRandomEntryBox.configure(state="readonly", readonlybackground="white")
		self.pathRandomButton = Button(self.frameRandom, text='...', width=5, height=1)
		self.pathRandomButton.grid(row=0, column=3, padx=(30,0), sticky='e')
		
		self.pathDestTextRandom = Label(self.frameRandom, text='Destination:')
		self.pathDestTextRandom.grid(row=1, column=0,padx=0, sticky='w')
		self.pathDestEntryBoxRandom = Entry(self.frameRandom, textvariable='6', width=50)
		self.pathDestEntryBoxRandom.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky='w')
		self.pathDestEntryBoxRandom.configure(state="readonly", readonlybackground="white")
		self.destRandomButton = Button(self.frameRandom, text='-->', width=5, height=1)
		self.destRandomButton.grid(row=1, column=3,padx=0, sticky='e')

		# ------------------------------------------------------------------------------------------------

		self.SameTypeLabel = Label(self.frameRandom, text='All of choosen types:')
		self.SameTypeLabel.grid(row=5, column=2, sticky='w')

		self.isAll = IntVar(value=1)
		self.sameTypeCheckbox = Checkbutton(self.frameRandom, variable=self.isAll)
		self.sameTypeCheckbox.grid(row=5, column=3, sticky='e')

		self.PickRandomLabel = Label(self.frameRandom, text='Pick random:')
		self.PickRandomLabel.grid(row=6, column=2, sticky='w')
		
		self.isRandom = IntVar()
		self.pickRandomCheckbox = Checkbutton(self.frameRandom, variable=self.isRandom)
		self.pickRandomCheckbox.grid(row=6, column=3, sticky='e')

		# ------------------------------------------------------------------------------------------------		

		self.nombreRandomText = Label(self.frameRandom, text='Number of files:')
		self.nombreRandomText.grid(row=7, column=2,padx=0,pady=0,sticky='w')
		self.nombreRandomEntry = Entry(self.frameRandom, textvariable="7", width=10,state="disable")
		self.nombreRandomEntry.grid(row=7, column=3,padx=0,pady=0,sticky='e')

		self.extDerouleText = Label(self.frameRandom, text="Extensions :")
		self.extDerouleText.grid(row=8, column=2, sticky='w', padx=0, pady=0)
		self.extComboBoxRandom = ttk.Combobox(self.frameRandom, width=5, state='disable')
		self.extComboBoxRandom.grid(row=8, column=3, sticky='e')

		# ------------------------------------------------------------------------------------------------

		self.infoText = Text(self.frameRandom, width=25, height=10)
		#self.infoText.grid(row=5, column=0, rowspan=6, columnspan=2, sticky='w')
		#self.infoText.configure(bd=1, relief="solid")
		#self.infoText.configure(state='normal')
		#self.infoText.insert(END, "")
		self.infoText.configure(state='disabled')

		self.infoListbox = Listbox(self.frameRandom, width=25, height=10)
		self.infoListbox.grid(row=5, column=0, rowspan=6, columnspan=2, sticky='w')
		self.infoListbox.configure(bd=1, relief="sunken", highlightthickness=0)

		self.generateRandomButton = Button(self.frameRandom,text='Pick', width=10)
		self.generateRandomButton.grid(row=9, column=2, columnspan=2, sticky='e')

	def getIsAllCheckbox(self):
		self.isRandom.set(0)
		self.nombreRandomEntry.configure(state="disable")

	def getIsRandomCheckbox(self):
		self.isAll.set(0)
		if(self.isRandom.get()):
			self.nombreRandomEntry.configure(state="normal")
		else:
			self.nombreRandomEntry.configure(state="disable")

	def updateExtComboBox(self):
		self.extComboBoxRandom.config(state="normal", values=self.c.fp.stats.extensions)
		self.extComboBoxRandom.set(self.c.fp.stats.mostFrequentExtension)

	def afficherMenu(self):
		self.frameMenu.pack()
		self.frameRandom.pack_forget()

	def displayProgram(self):
		self.frameRandom.pack()
		self.frameMenu.pack_forget()

	def open_directory_random(self):
		source = filedialog.askdirectory()
		if(source):
			self.pathRandomEntryBox.config(state='normal')
			self.pathRandomEntryBox.delete(0, END)
			self.pathRandomEntryBox.insert(0, source)
			self.pathRandomEntryBox.config(state="readonly")
			# --------------------------------------------------
			self.c.fp.source = source
			self.c.fp.setup()
			self.updateExtComboBox()

			self.infoListbox.configure(state='normal')
			for s in self.c.fp.statsInfos:	
				self.infoListbox.insert(END, s)

	def open_directory_destRandom(self):
		self.pathRandomDest = filedialog.askdirectory()
		self.pathDestEntryBoxRandom.config(state='normal')
		self.pathDestEntryBoxRandom.delete(0, END)
		self.pathDestEntryBoxRandom.insert(0, self.pathRandomDest)
		self.pathDestEntryBoxRandom.config(state="readonly")