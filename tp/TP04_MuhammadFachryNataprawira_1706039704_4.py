from tkinter import *
from math import *

try:
	#it can be done on windows, but not on linux
	from idlelib.tooltip import *
except:
	pass

class SuperCalculator(object):

	#initializing supercalculator constructor
	def __init__(self, master):
	
		#initialize window
		self.master = master

		#giving title
		master.title('Supercalculator by: Muhammad Fachry Nataprawira')

		#main variable for all function
		self.startOfNextOperand = True 	#flag
		self.expr = ''					#expression
		self.memory = ''				#memory
		#list of buttons
		buttons = [[	'Clr',	'MC',	'M+',	'M-',	'MR'	],
				  [		'd',	'e',	'f',	'+',	'-'		],
				  [		'a',	'b',	'c',	'/',	'*'		],
				  [		'7',	'8',	'9',	'**',	'√'		],
				  [		'4',	'5',	'6',	'sin',	'cos'	],
				  [		'1',	'2',	'3',	'tan',	'ln'	],
				  [		'0',	'.',	'+/-',	'~',	'2C'	],
				  [		'x',	'o',	'^',	'|',	'&'		],
				  [		'π',	'int',	'rad',	'//',	'exp'	],
				  [		'bin',	'hex',	'oct',	'%',	'='		]]

		#list of tooltips
		tooltips =	[[	'clear',	'clear memory',	'add to memory','subtract from memory',	'recall from memory'],
				 	[	'letter d',	'letter e',		'letter f',		'add',					'subtract'			],
				  	[	'letter a',	'letter b',		'letter c',		'divide',				'multiply'			],
				  	[	'digit 7',	'digit 8',		'digit 9',		'power',				'akar'				],
				  	[	'digit 4',	'digit 5',		'digit 6',		'sin',					'cos'				],
				  	[	'digit 1',	'digit 2',		'digit 3',		'tan',					'ln'				],
				  	[	'digit 0',	'dec point',	'togle +- sign','bitwise complement',	"2's complement"	],
				  	[	'letter x',	'letter o',		'bitwise xor',	'bitwise or',			'bitwise and'		],
				  	[	'PI num',	'float to int',	'degrees to rad','int divide',			'exp'				],
				  	[	'int to bin','hex to bin',	'oct to bin',	'mod',					'compute to dec'	]]

		#create the entry box and grid it.
		self.entry = Entry(master, 
							relief 		= RAISED, 
							borderwidth = 3,
							width		= 35, 
							bg 			= 'white', 
							font		= 'helvetica 20')
		self.entry.grid(row=0, column=0, columnspan=5)

		#for loop for creating button and make functions
		#r for row, and c for column, b for button
		for r in range(10):
			for c in range(5):
				#create a function and will take default argument about
				#button row and column index
				def cmd(x = buttons[r][c]):
					self.click(x)
				#create button objects and grid it base on r&c index
				b = Button(master, 
					text 		= buttons[r][c],
					width 		= 8,
					height		= 2,
					relief 		= RAISED,
					command 	= cmd,
					bg 			= 'mediumseagreen',
					font 		= 'helvetica 16',
					fg 			= 'white')
				b.grid(row = r + 1, column = c)

				#for linux, dont make the tooltips
				try:
					ToolTip(b, tooltips[r][c])
				except:
					pass

	#here is where the logic of every operations happen
	def click(self, key):
		#for equal operation
		if key == '=':
			#giving error if there's no operation yet
			try:
				result = eval(self.expr + self.entry.get())
				self.entry.delete(0, END)
				self.entry.insert(END, result)
				self.expr = ''
			except:
				self.entry.delete(0, END)
				self.entry.insert(END, 'Error')
				self.startOfNextOperand = True

		#digit buttons
		elif key in '1234567890abcdefox':
			if self.startOfNextOperand:
				self.entry.delete(0, END)
				self.startOfNextOperand = False
			self.entry.insert(END, key)

		#for pi and euler 
		elif key in ['π', 'exp']:
			if key == 'π' : key = eval('pi')
			if key == 'exp': key = 'e'
			if self.startOfNextOperand:
				self.entry.delete(0, END)
				self.startOfNextOperand = False
			self.entry.insert(END, key)

		#operators buttons
		elif key in ['+', '-', '*', '/', 
					'//', '**', '%', 
					'&', '|', '^']:
			#storing key(operation) to expr var
			self.expr += self.entry.get()
			self.expr += key

			#after clicking operation set startofnextoperan = T
			self.startOfNextOperand = True

		#togling plus and minus
		elif key == '+/-':
			#swtich + to -, and vice versa
			#if the entry is empty, do nothing
			try:
				if self.entry.get()[0] == '-':
					self.entry.delete(0)
				else:
					self.entry.insert(0, '-')
			except IndexError:
				pass

		#memory operation goes here
		elif key in ['M+', 'M-', 'MR', 'MC']:
				try:
					if key == 'M+':
						self.memory = eval('{}+{}'.format(self.memory, 
							self.entry.get()))
						self.entry.delete(0, END)
					elif key == 'M-':
						self.memory = eval('{}-{}'.format(self.memory, 
							self.entry.get()))
						self.entry.delete(0, END)
					elif key == 'MR':
						self.entry.delete(0, END)
						self.entry.insert(0, self.memory)
					elif key == 'MC':
						self.memory = ''
						self.entry.delete(0, END)
				except:
					self.entry.delete(0, END)
					self.entry.insert(0, 'Error')
					self.startOfNextOperand = True

		#converting to int, hex, bin, oct here
		elif key in ['int', 'hex', 'bin', 'oct', 
					'rad', 'ln', '√']:
			#for different situation symbols
			if key == 'rad'	: key = 'radians'
			if key == 'ln' 	: key = 'log'
			if key == '√' 	: key = 'sqrt'
			#getting entry input
			num = self.entry.get()
			try:
				cnv = eval('{}({})'.format(key, num))
				self.entry.delete(0, END)
				self.entry.insert(0, cnv)
			except:
				self.entry.delete(0, END)
				self.entry.insert(END, 'Error')
				self.startOfNextOperand = True

		#for . operation
		elif key == '.':
			#if there is already . on number, just pass
			if '.' in self.entry.get():
				pass
			else:
				self.entry.insert(END, '.')

		#for operation that use radians
		elif key in ['sin', 'cos', 'tan']:
			num = self.entry.get()
			#radians({})
			try:
				cnv = eval('{}({})'.format(key, num))
				self.entry.delete(0, END)
				self.entry.insert(0, cnv)
			except:
				self.entry.delete(0, END)
				self.entry.insert(0, 'Error')
				self.startOfNextOperand = True

		#getting 32 bit representation
		elif key == '2C':
			num = self.entry.get()
			cnv = eval('int({})'.format(num))	#make all the input to int so it can be string formatted
			self.entry.delete(0, END)
			try:
				#check this problem again
				if -2**32 <= cnv < 2**32:
					if '-' in num:
						num_int = 2**32 + cnv
						bin32rep = '0b{0:032b}'.format(num_int)
					else:
						bin32rep = '0b{0:032b}'.format(cnv)
					self.entry.insert(0, bin32rep)
				else:
					self.entry.insert(0, 'Error')
					self.startOfNextOperand = True
			except:
				self.entry.insert(0, 'Error')
				self.startOfNextOperand = True

		#bitwise complement
		elif key == '~':
			num = self.entry.get()
			try:
				result = eval('~{}'.format(num))
				self.entry.delete(0, END)
				self.entry.insert(0, result)
			except:
				self.entry.delete(0, END)
				self.entry.insert(0, 'Error')
				self.startOfNextOperand = True

		#clear the entry
		elif key == 'Clr':
			self.entry.delete(0, END)
			self.expr = ''

if __name__ == '__main__':
	#for create and start the program
	root = Tk()
	myCal = SuperCalculator(root)
	root.mainloop()
