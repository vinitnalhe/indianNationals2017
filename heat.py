import glob as glob
s=""


def makegoodname(name):
	A=[]
	for j in range(len(name)):
		if not name[j].islower():
			A.append(j)
	A1=[]
	for j in range(len(A)-1):
		A1.append(name[A[j]:A[j+1]])
	A1.append(name[A[-1]:])
	return " ".join(A1)


for myfile in sorted(glob.glob("Heats/*.pdf")):
	fname=myfile.split("Heats/")[1]
	pname=fname[:-4]
	gname=makegoodname(pname)
	s+="<li> <a href=" +fname+">" + gname+ "</li>"+"\n"
	
s1="""<html> 
	<head> 
	<title="Personal Heats">
	</head>
	<body>
	<h1> Personal Heats - Indian Nationals 2017 </h1>
"""

f1=open("Heats/index.html",'wb')

f1.write(s1)
f1.write(s)
f1.write("""</body> </html>""")
f1.close()
