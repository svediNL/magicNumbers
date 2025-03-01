import math
from operator import itemgetter

from alphabet import *


def calcBaseNumber_Pythagoras(summing_elements = [], break_master_nmbr = False, verbose = True):
# Calculate base number from summing elements
	first_sum = -1
	calc_error = False
	tmp_sum = summing_elements
	while True:
	# Sum elements & print result
		result = 0
		for n in range(len(tmp_sum)):
			result = result + tmp_sum[n]

		if verbose:
			printSummingResult(tmp_sum, result)

		
		if first_sum == -1:
		# store initial value for later reference	
			first_sum = result

	# Check if end is reached
		if result < 10:
		# break on single digit
			break

		check_master_nmbr = checkMasterNumber(result)
		if check_master_nmbr & break_master_nmbr:
			break

		# generate new summing elements list for next loop
		tmp_sum = []
		for k in str(result):
			tmp_sum.append(int(k))

		if verbose:
			print('...')

	# Return result
	if not calc_error:
		return result, first_sum
	else:
		return -1, -1
	
def calcBaseNumber_SumEach(summing_elements = [], break_master_nmbr = False,  verbose = True):
# Calculate base number from sum all single digit values
	first_sum = -1
	calc_error = False
	tmp_sum = []
	for n in range(len(summing_elements)):
		for k in str(summing_elements[n]):
			tmp_sum.append(int(k))

	while True:
	# Sum elements & print result
		result = 0
		for n in range(len(tmp_sum)):
			result = result + tmp_sum[n]

		if verbose:
			printSummingResult(tmp_sum, result)

		
		if first_sum == -1:
		# store initial value for later reference	
			first_sum = result

	# Check if end is reached
		if result < 10:
		# break on single digit
			break

		check_master_nmbr = checkMasterNumber(result)
		if check_master_nmbr & break_master_nmbr:
			if verbose:
				print('Master number detected!')
			break

		# generate new summing elements list for next loop
		tmp_sum = []
		for k in str(result):
			tmp_sum.append(int(k))
		if verbose:
			print('...')

	# Return result
	if not calc_error:
		return result, first_sum
	else:
		return -1, -1

def checkMasterNumber(value):
# Check if value has only repeating numbers
	tmp_list = []
	for k in str(value):
		tmp_list.append(int(k))

	master_number = True
	for n in range(len(tmp_list)):
		master_number = master_number and tmp_list[0] == tmp_list[n] # set master_number false when char[n] <> char[0]	

	return master_number
	
def printSummingResult(summing_elements =[], result = -1):
	tmp_str = str(result)
	tmp_str += '\t= '
	for n in range(len(summing_elements)):
		tmp_str += str(summing_elements[n])
		if (n<len(summing_elements)-1):
			tmp_str += ' + '
	print(tmp_str)
	#print('\n\rSum of \n\r', input_list, '\n\r = ', result)

def CharsToValues(input_string = [], input_alphabet = [[]]):
	tmp_mapping = []
	for n in range(len(input_string)):
		# CYCLE THOUGH CHARS
			try:
			# CHECK IF CHAR IS ALREADY A NUMBER
				int(input_string[n])
			except:
			# CHAR IS NOT A NUMBER
				# CHECK IF CHAR IS IN ALPHABET
				for m in range(len(input_alphabet)):
					if input_string[n] == input_alphabet[m][0]:
					# CHAR FOUND
						# ADD VALUE TO SUMMING BUFFER
						tmp_mapping.append(int(input_alphabet[m][1]))
						break
					elif m == len(input_alphabet)-1:
					# CHAR NOT FOUND, ADD 0
						tmp_mapping.append(0)
			else:
			# CHAR IS NUMBER
				tmp_mapping.append(int(input_string[n])) # CONVERT CHAR TO INT & ADD TO BUFFER


	return tmp_mapping

def reverseCalculation(baseNumber = 1, depth = 3, verbose = True):
	#build test_array
	test_string = []
	test_index = []
	for n in range(depth):
		test_string.append('')
		test_index.append(-1)
	
	test_array = CharsToValues(test_string, alphabet_set_sorted)
	test_sum = 0
	result_array = []
	result_array_str =[]
	tmp_dot = 1

	end_reached = False
	while not end_reached:
		# CALCUATE SUM
		#test_sum = 0
		#for n in range(depth):
		#	test_sum += test_array[n]
		test_sum, intial_sum = calcBaseNumber_Pythagoras(test_array, False, verbose)

		#print('')
		#print('test index: ', test_index)
		#print('test string: ', test_string)
		#print('test sum: ', test_array)
		#print('test sum result: ', test_sum)

		if 	test_sum == baseNumber:
		# match found
			result_array.append(test_array)
			tmp_str = ''
			for n in test_string:
				tmp_str += n
			result_array_str.append(tmp_str)

			if verbose:
				print(result_array_str)
				print('...')
		
	# try new number
		# increment index counter(s)
		tmp_inc = depth-1
		test_index[tmp_inc] += 1
		while tmp_inc > 0:
		# CHECK INCREMENT
			if test_index[tmp_inc] > len(alphabet_set_sorted)-1:
				# LSB REACHED MAX INDEX
					if tmp_inc > 0:
					# INCREMENT NEXT MSB
						test_index[tmp_inc-1] += 1
						test_index[tmp_inc] = 0
						
			if alphabet_set_sorted[n][0]

			if test_index[0] > len(alphabet_set_sorted)-1:
			# MSB REACHED MAX INDEX
				end_reached = True
				break

			tmp_inc -= 1

		if not end_reached:
		# set new string / number combination
			test_string = []
			for n in test_index:
				if n >= 0:
					test_string.append(alphabet_set_sorted[n][0])
				else:
					test_string.append('')

			test_array = CharsToValues(test_string, alphabet_set_sorted)

		if not verbose:
			tmp_dot += 1
			if tmp_dot > 1000:
				tmp_dot = 1
				print('.', end='', flush=True)
	return result_array_str
	

config_string = ''	# String for printing the result configuration		
config_reset = True

print(' \n\r Start Loop...\n\r')
while True:
# SET CALCULATION CONFIGURATION
	if config_reset:
		config_string = ''	# String for printing the result configuration	
		config_reset = False	

		try:
			config_direction = input("Select direction: \n\r [1] Phrase to base number \n\r [2] Base number to phrase \n\r -> ")
			(int(config_direction) <0)
		except:
			config_direction = 1

		try:
			config_alphabet	= input("Select alphabet: \n\r [1] Latin \n\r [2] Greek \n\r [3] Latin Classic (no J & U) \n\r -> ")
			(int(config_alphabet) <0)
		except:
			config_alphabet = 1

		try:
			config_nmbr_mapping	= input("Select counting system: \n\r [1] Latin (1..9) \n\r [2] Greek (1..9, 10..90, ...)\n\r [3] Incremental (1, 2, 3, ..., n) \n\r [4] Chaldean \n\r -> ")
			int(config_nmbr_mapping)
		except:
			config_nmbr_mapping = 1

		if config_direction:
			try:
				input_calc_method	= input("Select method: \n\r [1] Pythagorean \n\r [2] Pythagorean with Master Numbers \n\r [3] Sum individual numbers (eg. 2+34 => 2+3+4) \n\r -> ")
				config_calc_method = int(input_calc_method)
			except:
				config_calc_method = 1
		else:
			config_calc_method = 1

		# SET / GENERATE ALPHABET
		if int(config_alphabet) == 1:
			alphabet_set = LATIN_SET
			config_string += 'Latin characters, '
		elif int(config_alphabet) == 2:
			alphabet_set = GREEK_SET
			config_string += 'Greek characters, '
		elif int(config_alphabet) == 3:	
			alphabet_set = LATIN_CLASSIC_SET
			config_string += 'Classic latin characters, '
		else:
		# SET DEFAULT LATIN CHARACTERS (& COUNTING)
			alphabet_set = LATIN_SET
			config_string += 'Latin characters, '	

		if config_calc_method == 1:
			config_string += 'Pythagorean method'
		elif config_calc_method == 2:
			config_string += 'Pythagorean method (break on master nmbr)'
		elif config_calc_method == 3:
			config_string += 'Single digit summing method'
		else:
			config_calc_method = 1
			config_string += 'Pythagorean method'

# GENERATE CHARACTER TO NUMBER MAPPING
		if int(config_nmbr_mapping) == 1:
			config_string += 'Latin counting, '
			for n in range( len(alphabet_set) ):
				alphabet_set[n][1] = (n%9)+1

		elif int(config_nmbr_mapping) == 2:	
			config_string += 'Greek counting, '
			for n in range( len(alphabet_set) ):
				alphabet_set[n][1] = ((n%9)+1) * pow(10,(math.floor((n)/9)))

		elif int(config_nmbr_mapping) == 3:
			config_string += 'Incremental counting, '
			for n in range( len(alphabet_set) ):
				alphabet_set[n][1] = n+1

		elif int(config_nmbr_mapping) == 4:	
		# SET LATIN CHALDEAN COUNTING
			config_string += 'Chaldean counting, '
			alphabet_set = LATIN_CHALDEAN_SET

		else:
			alphabet_set = LATIN_SET
			config_string += 'Incremental counting, '

		alphabet_set_sorted = sorted(alphabet_set, key=itemgetter(1))

# RETURN CHARACTER TO NUMBER MAPPING
	print('\n\r\n\r')
	# print('#---------------------------------------------------#')
	print('=====================================================')
	print('Alphabet Set: \n\r')
	#print('alphabet_set, '\n\r')	

	tmp_str = ''
	for m in range(len(alphabet_set)):
		tmp_str += alphabet_set[m][0]
		tmp_str += ' = '
		tmp_str += str(alphabet_set[m][1])
		tmp_str += ',\t'
		if (( (m+1) % 4) == 0 and m>0) or (m==len(alphabet_set)-1):
			print(tmp_str)
			tmp_str = ''

	#print('#---------------------------------------------------#')
	print('\n\r')

# GET INPUT STRING
	my_input = input("Enter string: ")


	try:
		config_depth = input("Enter max number of characters in string (larger values lead to exponentially longer calculation time: \n\r -> ")
		(int(config_depth) <0)
	except:
		config_depth = 1
	else:
		config_depth = abs(int(config_depth))

	input_converted = '' # STRING OF CHARACTERS THAT ARE VALID
	input_mapped = [] # ARRAY OF VALUES TO CALCULATE BASE NUMBER
	try:
	# CHECK IF STRING IS VALID
		my_input = my_input.upper()	# CONVERT INPUT TO UPPERCASE
		input_string = my_input		# Store input for printing in result

		for n in range(len(my_input)):
		# CYCLE THOUGH CHARS
			try:
			# CHECK IF CHAR IS ALREADY A NUMBER
				int(my_input[n])
			except:
			# CHAR IS NOT A NUMBER
				# CHECK IF CHAR IS IN ALPHABET
				for m in range(len(alphabet_set)):
					if my_input[n] == alphabet_set[m][0]:
					# CHAR FOUND
						# ADD VALUE TO SUMMING BUFFER
						input_converted += alphabet_set[m][0]
						input_mapped.append(int(alphabet_set[m][1]))
						break
			else:
			# CHAR IS NUMBER
				input_converted += my_input[n]
				input_mapped.append(int(my_input[n])) # CONVERT CHAR TO INT & ADD TO BUFFER
	except:
	# RAISE ERROR, TRY AGAIN
		print('... String Error')

	else:
# PRINT INITIAL INPUT CONVERSION
		#print('#---------------------------------------------------#')
		print('\n\r')
		print(' -> Input string: ', my_input)

	# print input & values aligned
		#print(' -> Valid string', input_converted)
		#print(' -> Mapped numbers', input_mapped)
		print(' -> Input mapping:')
		fb_str_input =''
		fb_str_map =''
		for n in range(len(input_mapped)):
		# CYCLE THROUGH MAPPED INPUT
			# ADD CHARACTER VALUE TO PRINT BUFFER
			fb_str_map += str(input_mapped[n])
			fb_str_map += ','
			fb_str_map += ' '

			# ADD CHARACTER TO PRINT BUFFER
			fb_str_input += str(input_converted[n])
			fb_str_input += ','
			for m in range(len( str(input_mapped[n]) )):
				# PAD WITH SPACES IF VALUE HAS MORE CHARACTERS
				fb_str_input += ' '
			
			if ( (n+1)==len(input_mapped) ):
			# end reached
				print('   ', fb_str_input)
				print('   ',fb_str_map)
				print('')
			elif ( ((n+1)%20) == 0 ):
			# start new line
				print('   ', fb_str_input, '...')
				print('   ',fb_str_map, '...')
				print('')
				fb_str_input =''
				fb_str_map =''

				
		print('#---------------------------------------------------#')

# CALCULATE FINAL VALUE
		print('\n\r')
		print('================= C A L C U L A T E =================')
		if int(config_direction) == 2:
			final_word_list = reverseCalculation(int(my_input), depth = config_depth, verbose = False)
		else:
			if int(config_calc_method) == 1:
			# Classic Pythagorean method
				final_sum, intial_sum = calcBaseNumber_Pythagoras(input_mapped, False, True)
			elif int(config_calc_method) == 2:
			# Pythagorean method with Master Numbers
				final_sum, intial_sum = calcBaseNumber_Pythagoras(input_mapped, True, True)
			elif int(config_calc_method) == 3:
			# Sum each number individually
				final_sum, intial_sum = calcBaseNumber_SumEach(input_mapped, False, True)



# PRINT RESULTS
		print('\n\r\n\r=================== R E S U L T S ===================')
		print('')
		if int(config_direction) == 2:
			print(final_word_list)
		else:
			print('Input:\t\t', input_string)
			print('Initial sum:\t', intial_sum)
			print('Final value:\t', final_sum)
			print('')
			print('using:\t', config_string)
		print('')
		print('=====================================================\n\r\n\r')
		any_key = input('\tEnter Z to reset the alpabet & numbering configuration\n\r\tEnter Q to exit program loop\n\r\tEnter any other key to try again\n\r\t-> ')
		if any_key.upper() == 'Z':
			config_reset = True
		elif any_key.upper() == 'Q':
			break
quit()

