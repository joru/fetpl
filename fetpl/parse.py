def parseIndent(f):
	"""
	parse indented file into tree
	
	skip empty lines or starting with ' (comments)
	"""
	tops=[]#('',nonwhtite,children)#lines without indentation
	pfxs=[]#(white,nonwhite,children)
	for line in f:
		nonwhite=line.lstrip()
		white=line[:len(line)-len(nonwhite)]
		nonwhite=nonwhite.strip()
		if not nonwhite or nonwhite[0]=='\'':
			continue
		mynode=(white,nonwhite,[])
		while pfxs:
			if white.startswith(pfxs[-1][0]) and white!=pfxs[-1][0]:
				#it is children of last in pfxs
				pfxs[-1][2].append(mynode)
				pfxs.append(mynode)
				break
			else:
				pfxs.pop()#it's not our parent
		if not pfxs:
			tops.append(mynode)
			pfxs.append(mynode)
	return tops
def _unparseIndent(fo,tops,plus='\t',acc=''):
	"sanity check for `parseIndent`"
	for w,n,c in tops:
		fo.write(acc+n+'\n')
		_unparseIndent(fo,c,plus,acc+plus)
