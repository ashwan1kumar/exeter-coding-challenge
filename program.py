import fileinput
import sys
import re
import time
import resource 

time_start = time.perf_counter()
dictonary = {}
csvfile = open("french_dictionary.csv","r+")
words_file = open("find_words.txt","r")
z = set()
for line in words_file:
	tmp = line
	tmp = tmp.rstrip("\n")
	z.add(tmp)

for line in csvfile:
	tmp = line
	tmp = tmp.rstrip("\n")
	ls = tmp.split(",")
	dictonary[ls[0]]=ls[1]
	# break

file = open("t8.shakespeare.txt","r")
freq = {}
for x in dictonary.keys():
	freq[x]=0
# print(freq)
translated_text = open("t8.shakespeare.translated.txt","w")
occurence = set()

for line in file:
	tmp = line
	tmp = tmp.rstrip("\n")
	ls = tmp.split(" ")
	# print(ls)
	nl = []
	for item in ls:
		if (item.lower() in dictonary) and (item.lower() in z):
			occurence.add(item.lower())
			freq[item.lower()]+=1
			nl.append(dictonary[item.lower()])
		else:
			nl.append(item)
	ans=""
	for item in nl:
		ans+=(item)
		ans+=(" ")
	ans.rstrip(" ")
	# print(line)
	ans+=("\n")
	translated_text.write(ans)

oc_copy = list(occurence)
oc_copy.sort()
fhandler = open("frequency.csv","w")
for ele in oc_copy:
	# print(ele)
	ans=""
	ans+=ele
	ans+=","
	ans+=dictonary[ele]
	ans+=","
	ans+=str(freq[ele])
	ans+="\n"
	fhandler.write(ans)


time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%5.1f secs %5.1f MByte" % (time_elapsed,memMb))
print(memMb)