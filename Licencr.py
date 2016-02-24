import urllib,tempfile,shutil
def checkFor(app):
	tmpdir = tempfile.mkdtemp()
	saveto = tmpdir + '\FL'
	wheretocheck = "https://raw.githubusercontent.com/SolomonBicakcic/Licencr/master/" + str(app)
	try:
		urllib.urlretrieve(wheretocheck, saveto)
	except:
		return False
		
	for line in open(saveto, "r"):
		if line[0] == str(1):
			return True
		else:
			return False
	shutil.rmtree(tmpdir)
