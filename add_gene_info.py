import sys
data={}

first=True
for line in open(sys.argv[2]):
	content=line.strip().split(";")
	if first:
		first=False
		header=";".join(content[1:])
		continue

	data[content[0]]=content[1:]

first=True
for line in open(sys.argv[1]):
	if first:
		print(line.strip()+";"+header)
		first=False
		continue
	content=line.strip().split(";")

	try:
		print( line.strip()+";"+";".join(data[content[4]]) )
	except:
		print(line.strip()+";"+";".join(["NA"]*5 ))
