import codecs
import sys
''' Run it from a command line 
   python stat_f.py file_name

'''

if __name__ == '__main__':
	fdata = codecs.open(sys.argv[1],'r','utf-8')
   	cont = fdata.read()
	fdata.close()
	print '********************** Stat Information ******************************'
	print '	Name of the file %s '% (sys.argv[1])
	print '	Sentence/line count %d ' % len(cont.splitlines())
	print '	Token count %d  ' % len(cont.split()) 
	print '	Word types count %d  ' % len(set(cont.split()))
	print '********************** ******************************** **************'
