'''
Rounding module that rounds a float just like the built-in round function

Rounder options
---------------
disable_warnings : bool
	able to choose if warnings are disabled or not
return_format : str
	able to choose how errors are returned. default is 'same_number'
	available options (all changed as string):
		same_number: the same number passed onto the function
		error_message: an error message as to why it failed
		raise_error: will raise an error when an error does occur
		none: just return None on error
		anything else: just return same number passed
'''

__version__ = '1.4.2'
disable_warnings = False

# available options can be seen at top of file
return_format = 'same_number'

def _return_handler(number, error = None, exception_type = None):
	if return_format == 'none':
		return None
	elif return_format == 'error_message':
		return 'An unknown error occured while rounding' if error is None else '[Rounder] ' + error
	elif return_format == 'raise_error':
		if exception_type != None:  # if custom raise error
			raise exception_type('[Rounder] ' + error)
		raise Exception('An unknown error occured while rounding' if error is None else '[Rounder] ' + error)
	else:  # in any other case just return the number
		return number


def _round_past_decimal(round_place, first_numbers, past_decimal):
	'''
	rounds past the decimal point and returns the full number when done
	'''

	zero_string = ''  # add a 1 to whatever place needs changed to be 1 higher
	# the for range determines where the number that needs to be changed is
	for i in range(round_place):
		if i + 1 == round_place:
			zero_string += '1'
			break
		else:
			zero_string += '0'
	
	zero_string = float('0.' + zero_string)
	old_past = float('0.' + past_decimal)  # old past decimal numbers
	new_past_numbers = str(zero_string + old_past).split('.')  # new past decimal numbers

	# this will only happen if rounding by whole number (i think)
	if int(new_past_numbers[0]) >= 1:
		first_numbers += int(new_past_numbers[0])
		return first_numbers
	elif int(new_past_numbers[0]) <= -1:
		first_numbers -= int(new_past_numbers[0])
		return first_numbers

	rounded_number = str(first_numbers) + '.' + new_past_numbers[1][:round_place]
	return float(rounded_number)


def _search_number(round_place, first_numbers, past_decimal):
	for i in past_decimal[round_place:]:
		if int(i) >= 5:
			return _round_past_decimal(1 if round_place == 0 else round_place, first_numbers, past_decimal)
		elif int(i) <= 3:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)

	# if it goes through a whole number of 4s and can't round up
	rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
	return float(rounded_number)


def round(number: float, round_place: int = 0):
	'''
	Rounds a float just like the built in round function, except with more advanced rounding

	Rounder uses artificial intelligence to round beyond the point you want rounded for more precise
	rounding. So `3.45` rounded by the whole number using Rounder is `4`, but if you used the built-in
	round function it'd be `3`

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
		ex: `4.5` is returned as `5` or `4.4` is returned as `4`
	rounded_number : float
		the actual rounded number that the user wants
	_return_handler : None, str, any
		depends on what the developer specified, but it can return None, an error string or raise an error,
		or whatever number was inputted as the options
	'''

	if not isinstance(number, float):  # if it's not a float, just return whatever they pased
		return _return_handler(number, f'{number} is a {type(number).__name__}, not a float', ValueError)

	if round_place > 15:  # since rounder doesn't currently support more than 15 digits past decimal
		round_place = 15
		if not disable_warnings:
			print(f'[Rounder] Warning: Automatically set round place to 15 digits')
	elif round_place < 0:  # negative round place just messes things up in annoying ways
		round_place = 0
		if not disable_warnings:
			print(f'[Rounder] Warning: Automatically set round place to 0 digits')

	number_to_str = str(number)
	split_number = number_to_str.split('.')
	first_numbers = int(split_number[0])  # the whole number as int
	past_decimal = split_number[1]  # number(s) past the decimal as str

	# additional check to make sure there's only 15 digits past decimal
	if len(past_decimal) > 15:
		past_decimal = past_decimal[:15]
		# honestly not sure if this is needed but gonna keep this for now
		# added below because a test failed because 'e' was in it (at the end of it at least)
		# a link to the test: https://github.com/Aethese/rounder/runs/6277132398
		if past_decimal[-1] == 'e':
			past_decimal = past_decimal[:-2]
		elif past_decimal[-1] == '-':  # we love edge cases
			past_decimal = past_decimal[:-3]
		
		if not disable_warnings:
			print('[Rounder] Warning: Automatically set digits past decimal place to just 15')

	negative_number = bool(first_numbers < 0)  # check if negative number

	if round_place == 0:
		if int(past_decimal[0]) >= 5:
			if negative_number:
				first_numbers -= 1
			else:
				first_numbers += 1
			return first_numbers
		elif int(past_decimal[0]) == 4:
			search = _search_number(round_place, first_numbers, past_decimal)

			# if the number doesn't need rounded up just return original first number(s)
			if isinstance(search, int):
				return search

			search_split = str(search).split('.')
			if int(search_split[1][0]) >= 5:  # get first digit past decimal point
				if negative_number:
					first_numbers -= 1
				else:
					first_numbers += 1
				return first_numbers
			else:
				return int(search)
		else:  # numbers past decimal don't need rounding
			return first_numbers
	else:  # round past decimal point
		if len(past_decimal) <= round_place or len(past_decimal) == 1:
			return _return_handler(number, f'Unable to round number. Number: {number}, Round place: {round_place}', IndexError)

		if int(past_decimal[round_place]) >= 5:
			rounded_number = _round_past_decimal(round_place, first_numbers, past_decimal)
			return rounded_number
		elif int(past_decimal[round_place]) == 4:
			rounded_number = _search_number(round_place, first_numbers, past_decimal)
			return rounded_number
		else:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)
