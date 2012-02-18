
listOfOperateurs = ['+','-','*','/']
listOfChiffres = [1,2,3,4,5,6]

def main():
	for chiffre in listOfChiffres:
		print(chiffre)
	#recurse(listOfChiffres)
	result=construct([],listOfChiffres)
	print(result)

def recurse(alist):
	print(alist)
	last=alist.pop()
	if(len(alist)<1):
		print("==>",last)
	else:
		recurse(alist)


def construct(result, alist):
	print('result=',result,' list=',alist)
	if(len(alist)>0):
		result.append(alist.pop()) 
		if(len(alist)>0):
			result.append('+')
		return construct(result,alist)
	else:
		return result
		




if __name__ == '__main__':
    main();

