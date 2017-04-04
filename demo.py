from sets import Set
def sum():
	print "Hello"
	s= Set()
	s.add('hey')
	print len(s)
	lists = []
	for i in range(0,150):
		lists.append(0)
	lists[10]=lists[10]+1
	print len(lists)
if __name__ == '__main__':
	sum()