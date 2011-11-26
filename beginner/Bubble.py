import random
class Bubble:

	ma_list=[9,5,1,6,7,12]
	swapped = True
	swapping=0
	def __init__(self,to_sort):
		self.ma_list=to_sort
		print(self.ma_list)
	
	def sort(self):
		while(self.swapped==True):
			i=1
			self.swapped=False
			while(i<len(self.ma_list)):
				self.swap(i-1,i)
				i+=1
	def swap(self,pos1,pos2):
		if(self.ma_list[pos1]>self.ma_list[pos2]):
			temp = self.ma_list[pos2]
			self.ma_list[pos2]=self.ma_list[pos1]
			self.ma_list[pos1]=temp
			self.swapped=True
			self.swapping+=1
		

		

to_sort = []
for i in range(1,10):
	to_sort.append(random.randint(0,1000))
bubble = Bubble(to_sort)
bubble.sort()
print(bubble.ma_list)
print('swapping :',bubble.swapping)
