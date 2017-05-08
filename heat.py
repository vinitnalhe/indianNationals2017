import glob as glob
s=""
for myfile in glob.glob("Heats/*.pdf"):
	fname=myfile.split("Heats/")[1]
	print fname
	s+="<li> <a href=" +fname+">" + fname+ "</li>"+"\n"
	
s1="""<html> 
	<head> 
	<title=\"Personal Heats\">
	</head>
	<body>
"""

f1=open("Heats/index.html",'wb')

f1.write(s1)
f1.write(s)
f1.write("""</body> </html>""")
f1.close()
