'''
Rounding module that rounds a float just like the built in round function lol
'''

# available options:
# 	same_number: the same number passed onto the function
#	error_message: an error message as to why it failed
# 	none: just return None on error
return_format = 'same_number'  # default is same_number

def _return_handler(number, error = None):
	if return_format == 'none':
		return None
	elif return_format == 'error_message':
		return 'An error occured while rounding' if error is None else error
	else:
		return number  # in any other case just return the number


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
	past_decimal = split_number[1]  # number(s) past the decimal as str
	first_numbers = int(split_number[0])  # the whole number as int

	if round_place == 0:
		if int(past_decimal[:1]) >= 5:
			first_numbers += 1
			return first_numbers
		else:
			return first_numbers
	else:  # round past decimal
		if len(past_decimal) < round_place:
			return _return_handler(number, f'Failed to round past available digits. Number: {number}, Round place: {round_place}')

		if int(past_decimal[round_place]) >= 5:
			zero_string = ''  # add a 1 to whatever place needs changed to be 1 higher
			# the for range determines where the number that needs to be changed is

			for i in range(round_place):
				if i + 1 == round_place:
					zero_string += '1'
				else:
					zero_string += '0'
			
			zero_string = '0.' + zero_string
			zero_string = float(zero_string)
			old_past = float('0.' + past_decimal)
			new_past_numbers = str(zero_string + old_past).split('.')[1]  # new numbers past decimal place

			rounded_number = str(first_numbers) + '.' + str(new_past_numbers)[:round_place]
			return float(rounded_number)
		else:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)
