'''
Rounding module that rounds a float just like the built in round function lol
'''

__version__ = '1.3.0'

# available options:
# 	same_number: the same number passed onto the function
#	error_message: an error message as to why it failed
# 	none: just return None on error
return_format = 'same_number'  # default is same_number

def _return_handler(number, error = None):
	if return_format == 'none':
		return None
	elif return_format == 'error_message':  # could also raise an error for easier debugging?
		return 'An error occured while rounding' if error is None else '[Rounder] ' + error
	else:
		return number  # in any other case just return the number


def _round_past_decimal(round_place, first_numbers, past_decimal):
	'''
	rounds past the decimal point and returns the full number when done
	'''
	zero_string = ''  # add a 1 to whatever place needs changed to be 1 higher
	# the for range determines where the number that needs to be changed is

	for i in range(round_place):
		if i + 1 == round_place:
			zero_string += '1'
		else:
			zero_string += '0'
	
	zero_string = '0.' + zero_string
	zero_string = float(zero_string)
	old_past = float('0.' + past_decimal)  # old past decimal numbers
	new_past_numbers = str(zero_string + old_past).split('.')  # new past decimal numbers
	if int(new_past_numbers[0]) >= 1:
		first_numbers += int(new_past_numbers[0])

	rounded_number = str(first_numbers) + '.' + new_past_numbers[1][:round_place]
	return float(rounded_number)


def _search_number(round_place, first_numbers, past_decimal):
	for i in past_decimal[round_place:]:
		if int(i) >= 5:
			return _round_past_decimal(1 if round_place == 0 else round_place, first_numbers, past_decimal)
		elif int(i) == 4:  # basic check out of the way
			continue
		else:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)

	# if it goes through a whole number of 4s and can't round up
	if round_place == 0:
		return first_numbers

	rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
	return float(rounded_number)


def round(number: float, round_place: int = 0):
	'''
	Rounds a float just like the built in round function lol
	Made by Aethese :)

	Parameters
	----------
	number : float
		number that needs to be rounded
	round_place : int
		place after decimal to be rounded. if not passed defaults to whole number
	
	Returns
	-------
	number : any except float
		if a float isn't passed then the same value passed will be returned
	first_number : int
		if number is being rounded to a whole number than it will return rounded for whole number.
		ex: 4.5 is returned as 5 or 4.4 is returned as 4
	rounded_number : float
		the actual rounded number that the user wants
	'''
	is_float = isinstance(number, float)
	if not is_float:
		return _return_handler(number, f'{number} is a {type(number).__name__}, not a float')

	number_to_str = str(number)
	split_number = number_to_str.split('.')
	first_numbers = int(split_number[0])  # the whole number as int
	past_decimal = split_number[1]  # number(s) past the decimal as str
	# additional check to make sure there's only 15 digits past decimal
	if len(past_decimal) > 15:
		past_decimal = past_decimal[:15]
		print('[Rounder] Warning: Limited digits past decimal place to just 15 digits')

	if first_numbers < 0:
		negative_number = True
	else:
		negative_number = False

	if round_place == 0:
		if int(past_decimal[:1]) >= 5:
			if negative_number:
				first_numbers -= 1
			else:
				first_numbers += 1
			return first_numbers
		elif int(past_decimal[:1]) == 4:
			search = _search_number(round_place, first_numbers, past_decimal)
			# if the number doesn't need rounded up just return original first number(s)
			if isinstance(search, int):
				return search

			search_split = str(search).split('.')
			if int(search_split[1][:1]) >= 5:
				if negative_number:
					first_numbers -= 1
				else:
					first_numbers += 1
				return first_numbers
			else:
				return search
		else:  # numbers past decimal don't need rounding
			return first_numbers
	else:  # round past decimal
		if len(past_decimal) <= round_place or len(past_decimal) == 1:
			return _return_handler(number, f'Failed to round past available digits. Number: {number}, Round place: {round_place}')

		if int(past_decimal[round_place]) >= 5:
			return _round_past_decimal(round_place, first_numbers, past_decimal)
		elif int(past_decimal[round_place]) == 4:
			return _search_number(round_place, first_numbers, past_decimal)
		else:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)
