import glob as glob
s=""
for myfile in sorted(glob.glob("Heats/*.pdf")):
	fname=myfile.split("Heats/")[1]
	print fname
	s+="<li> <a href=" +fname+">" + fname+ "</li>"+"\n"
	
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
