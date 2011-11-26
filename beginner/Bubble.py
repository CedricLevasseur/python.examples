import random, logging

class Bubble:
	""" this is a bubble sort"""
	ma_list=[]
	swapped = True
	swapping=0
	iter=1
	def __init__(self,to_sort):
		#logging config
		logging.basicConfig(level=logging.DEBUG)
		self.ma_list=to_sort
		logging.debug(self.ma_list)
	
	def sort(self):
		while(self.swapped==True):
			i,self.swapped = 0, False
			while(i<len(self.ma_list)-1):
				self.swap(i,i+1)
				logging.debug(self.ma_list)
				i+=1
			logging.debug('----iter : %s-------',self.iter)
			self.iter+=1
	def swap(self,pos1,pos2):
		if(self.ma_list[pos1]>self.ma_list[pos2]):
			temp = self.ma_list[pos2]
			self.ma_list[pos2]=self.ma_list[pos1]
			self.ma_list[pos1]=temp
			self.swapped=True
			self.swapping+=1
		


# initialisation d'un tableau aleatoire
to_sort = []
for i in range(1,10):
	to_sort.append(random.randint(0,1000))

# tri	
bubble = Bubble(to_sort)
bubble.sort()

#affichage du resultat
print(bubble.ma_list)
print('swapping :',bubble.swapping)
