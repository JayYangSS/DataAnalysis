import sys,os
chunckSize=1000
class FileProcess(object):
	"""docstring for FileProcess"""
	def __init__(self, path):
		super(FileProcess, self).__init__()
		self.path = path

	# split the big file into several small files
	def split(self,outName,chunckSize=chunckSize):
		# if not os.path.exists(todir):
		# 	os.mkdir(todir)
		# else:
		# 	for fname in os.listdir(todir):
		# 		os.remove(os.path.join(todir,fname))

		file=open(self.path)
		readlines=file.readlines()
		count=0
		fileOutputName=outName+str(count+1)+'.json'
		outputFile=open(fileOutputName,'w')


		for line in readlines:
						
			if(count%chunckSize==0 and count!=0):
				outputFile.close()
				fileOutputName=outName+str(int(count/chunckSize)+1)+'.json'
				outputFile=open(fileOutputName,'w')
			count=count+1
			outputFile.write(line)		
		outputFile.close()



if __name__ == '__main__':

	focus_path=r'data\\total_focus.json'
	meeting_path=r'data\\total_meeting.json'
	
	#slpit the focus data
	# fileProcess=FileProcess(focus_path)
	# fileProcess.split('total_focus',1000)


	#split the meeting data
	meetingFile=FileProcess(meeting_path)
	meetingFile.split('total_meeting',1000)



