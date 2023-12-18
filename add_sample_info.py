import sys

data={}
first=True
for line in open(sys.argv[1]):
	content=line.strip().split(";")
	if first:
		header=content[1:]
		first=False
		continue
	data[content[0].split(" ")[0]]=content[1:]

first=True
n_cols=len(header)

for line in open(sys.argv[2]):
	content=line.strip().split(";")
	if first:
		print(line.strip()+";"+";".join(header))
		first=False
		continue

	content[0]="-".join(content[0].replace("MIP","").replace("-Research","").rstrip("-").split("-")[0:2])
	try:
		print(line.strip()+";"+";".join(data[content[0]]))
	except:
		print(line.strip()+";"+";".join(["NA"]*n_cols))

