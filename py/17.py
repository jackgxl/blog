from sys import argv
from os.path import exists
script,from_file,to_file = argv
print "Coping form %s to %s " % (from_file,to_file)

input = open(from_file)
indata = input.read()

print " The input file is %d bytes log" % len(indata)

print "Does the output file exit ? %r" % exists(to_file)
print "Ready, hit RETURN to continue,CTRL-C to abort."
#raw_input()
print "Writing data now ~~~~~~~"

output = open(to_file,'w')
output.write(indata)

print "ALLright,all done."

output.close()
input.close()
