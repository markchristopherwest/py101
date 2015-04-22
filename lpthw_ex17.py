__author__ = 'mwest'
from sys import argv
from os.path import exists
script , from_file, to_file = argv
print "Copying from %s to %s " % (from_file,to_file)

#we could do thees two on one line twoo how?
in_file = open(from_file)
indata = in_file.read()

print "The input fil eis % d bytes long" % long(indata)

print "Does the output file really exist? %r" exists(to_file)

print "Ready, hit RETURN, to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

