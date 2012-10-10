# open twain.txt, "copy" the data into 'text', then close the file.
def words_counted():
	text =''
	f = open('twain.txt')
	for line in f:
		newline = line.strip()
		text += ' '+ newline
	f.close()

	text = text.split(' ') # define 'text' as the file 'text' split by spaces
	word_count = {} # make a dict named 'word_count'
	for words in text: # for words in 'text'
		# strip the extra characters on the ends, then lowercase the words 
		words = words.strip('.",?!\[]#*()1234567890@%&/<>\':; $_-').lower()
		# count equals dict 'word_count'
		# which will then gives us the value of 'words'
		# which is every word in 'text' without symbols and lowercased
		# then give it the value of 0
		count = word_count.setdefault(words, 0)
		# adds the value as it goes down the list
		count +=1
		# sets the new value to each 'words' in dict 'word_count'
		# to 'count', which is the new value
		word_count[words]= count
	
	# We are now making a new list to sort everything in numerical order
	newlist = []
	# for 'keys, value' inside dict 'word_count', go through each item in the list
	for key, value in word_count.iteritems():
		# in 'newlist' add '(value, key)' the the end of the list
		newlist.append((value, key))
	# sort the 'newlist' in numerical order
	newlist.sort()
	newlist.reverse()
	# reverse the list so that the highest valued items are on the top of the list

	alphabetical(newlist)


def alphabetical(ourlist):
	#now we need to sort alphabetically
	count = 0
	sorted_frequency_list =[]
	current_frequency_list =[]
	for value, key in ourlist:
		if count == 0:
			current_frequency_list.append((value,key))
			count += 1
		elif value != ourlist[(count-1)][0] or count == len(ourlist)-1:
			current_frequency_list.sort()
			sorted_frequency_list.extend(current_frequency_list)
			current_frequency_list =[]
			current_frequency_list.append((value,key))
			count += 1

		else:
			current_frequency_list.append((value,key))
			count += 1 
		
		# for the value in 'newlist'
	for value, key in sorted_frequency_list:
		# show the value	
		print value, key	

		




	#orderedlist = [x for x in word_count.iteritems()]
	#print orderedlist.sort(key=lambda x:x[1])
	

words_counted()
