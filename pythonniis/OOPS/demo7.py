class Demo:
	def __show(self): #private method
		print("hi")
	def show(self):
		self.__show()
ob=Demo()
ob.show()