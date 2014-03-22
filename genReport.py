import sys
import os
import re

def main():
	# Initiating variables
	nodesFilename = 'nodes.txt'
	statusFilename = 'status_mail.txt'
	onlyStausFilename = 'only_status.txt'
	nodesStausFilename = 'nodes_status.txt'
	allStatusFilename = "all_status.txt"
	#configFile="Config.ini"
	nodes = []
	statusDict = ()
	results = []
	
	#getConfig(configFile)
	print "\n-----===Automated Report generator for TSM Backup Status===-----"+ "\n"*2
	print '<'*5 + " Copy all node names from Excel file to '%s' file "% nodesFilename +'>'*5
	print '<'*5 + " Copy status mail to '%s' file "% statusFilename+'>'*5
	print '\n' + "Press any key to generate the Report..."
	raw_input()
	
	#Main functions
	nodes = parse_nodes_file(nodesFilename) # get nodes list[1].
	statusDict = parse_status_mail_file(statusFilename) #get nodes dictionary
	results = gen_report(nodes,statusDict) # compare and generate report list[2].
	write_to_file(results,statusDict,onlyStausFilename,nodesStausFilename,allStatusFilename) #Write results to files.
		
	#print nodes
	#print statusDict
	#print results
	print
	print '<'*5 + "  Status of backups ---> Output\%s  "% onlyStausFilename+'>'*5
	print '<'*5 + "  Copy Contents of '%s' to 'Status' column in Excel file "% onlyStausFilename+'>'*5 + "\n" +'<'*1 + "'Check Manually' will be displayed if no status found for specific node!"+'>'*1
  #print '<'*5 + "  Node and Status of backups ---> %s  [Can be used for verification of results]"% nodesStausFilename+'>'*5 
	print "\nPress any key to exit..."
	raw_input()
    
def error_exit():
	print "\nPress any key to terminate the script..."
	raw_input()
	sys.exit()

def unknown_error():
		print "\nUnknown Error occurred!!!\nSend mail to Priyank Thavai [587242] along with the input files."
		error_exit()
	
def print_done():
		print "Done!"		
		
def parse_nodes_file(file):
	print "Parsing file '%s'" % file
	
	result = []
	try:
		myFile=open(file,'rU')	
		for line in myFile:
			#print line,
			if line=='\n':
				result.append('-----')
				continue
			line=line.strip()
			tmp=re.split("[\( \[ \{ \ ]",line)
			line=tmp[0]
			line=line.strip()
			result.append(line)
		myFile.close()
		print_done()
		#print result	
		return result
	except IOError as e:
		print "Error parsing %s [ %s ]" % (file,e.strerror)
		error_exit()
	except:	unknown_error()
		
		
def gen_report(nodes,statusDict):
	print "\nGenerating Report..."
	result=[]
	for mynode in nodes:
		if mynode in statusDict:
			result.append([mynode,statusDict[mynode]])
		elif mynode=="-----":
			result.append([mynode,"-----"])
		else:	
			result.append([mynode,"Check Manually"])
		
	print_done()	
	return result
	
def write_to_file(results,statusDict,f1,f2,f3):
	print "\nWriting report to files..."
	if not os.path.exists('Output'):
		os.makedirs('Output')
	
	if not os.path.exists('Debug'):
		os.makedirs('Debug')
	
	#----------write output files------
	os.chdir('Output')
	only_status_file=open(f1,'w')
	nodes_status_file=open(f2,'w')
	for result in results:
		only_status_file.write(result[1]+'\n')
		nodes_status_file.write(result[0]+" ---> "+result[1]+'\n')
	
	only_status_file.close()
	nodes_status_file.close()	
		
	#-------------Write Debug Info----------------------
	os.chdir('..\Debug')
	all_status=open(f3,'w')
	all_status.write("\n"+"-"*20+"All Nodes_Status Present in Status Mail"+"-"*20+"\n\n")
	n=statusDict.keys()
	s=statusDict.values()
	for i in range(len(n)):
		all_status.write(n[i]+" ----> "+s[i]+'\n')

	print_done()	
		
def parse_status_mail_file(file):
	print "\nParsing file '%s'" % file
	result={}
	n = []
	s = []
	sline=[]
	try:
		myFile=open(file,'rU')
		for line in myFile:
			#sline=line.split()
			sline=re.split('\ \ \ +',line)
			for a in range(len(sline)):
				sline[a]=sline[a].strip()
			sline = [x for x in sline if x != '']
			if len(sline)>3:
				#print sline
				n.append(sline[-2])
				s.append(sline[-1])
		myFile.close()
		nset=set(n)
		nUnique=list(nset)
		#print nUnique
		
		#Initiating blank dictionary
		for i in range(len(nUnique)):
			result[nUnique[i]]=""
		del i
		#convert lists to dictionary
		for i in range(len(n)):
			if result[n[i]]!="":
				result[n[i]]=result[n[i]]+","+s[i]
			else:	result[n[i]]=s[i]
					
		#print result
		print_done()
		return result
		
	except IOError as e:
		print "Error parsing %s [ %s ]" % (file,e.strerror)
		error_exit()
	except:	
		raise
		unknown_error()	
			
			
			
		
#Call main function	
if __name__=='__main__':
		main()