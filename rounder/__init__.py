'''
Rounding module that rounds a float just like the built-in round function,
except with better precision

Rounder options
---------------
disable_warnings : bool
	able to choose if warnings are disabled or not
return_format : str
	able to choose how errors are returned. default is 'raise_error'
	available options (all changed as string):
		same_number: the same number passed onto the function
		error_message: an error message as to why it failed
		raise_error: will raise an error when an error does occur
		none: just return None on error
		anything else: just return same number passed
'''

__version__ = '1.4.7'
disable_warnings = False
# available options for return format can be seen at top of file
return_format = 'raise_error'


def _return_handler(number, error=None, exception_type=None):
	'''
	handles how errors are returned

	Available Return Options
	------------------------
	same_number: the same number passed onto the function
	error_message: an error message as to why it failed
	raise_error: will raise an error when an error does occur
	none: just return None on error
	'''
	if return_format == 'none':
		return None
	elif return_format == 'error_message':
		return f'[Rounder] {error}'
	elif return_format == 'raise_error':
		raise exception_type(f'[Rounder] {error}')
	else:  # in any other case just return the number
		return number


def _round_past_decimal(round_place, first_numbers, past_decimal):
	'''rounds past decimal point and returns full float (or int) number when done'''
	zero_string = ''  # add a 1 to whatever place needs changed to be 1 higher

	# the for range determines where the number that needs to be changed is
	for i in range(round_place):
		if (i + 1) == round_place:
			zero_string += '1'
			break
		zero_string += '0'

	zero_string = float('0.' + zero_string)
	old_past = float('0.' + past_decimal)                      # old past decimal numbers
	new_past_numbers = str(zero_string + old_past).split('.')  # new past decimal numbers

	# this will happen if rounding by whole number or by rounding the tenth spot and it
	# forces the number to round up
	if int(new_past_numbers[0]) >= 1:
		first_numbers += int(new_past_numbers[0])
		return first_numbers
	elif int(new_past_numbers[0]) <= -1:
		first_numbers -= int(new_past_numbers[0])
		return first_numbers

	rounded_number = str(first_numbers) + '.' + new_past_numbers[1][:round_place]
	return float(rounded_number)


def _search_number(round_place: int, first_numbers: int, past_decimal: int):
	'''searches through the number to see if 4 needs to be rounded up'''
	for i in past_decimal[round_place:]:
		if int(i) >= 5:
			return _round_past_decimal(1 if round_place == 0 else round_place,
				first_numbers, past_decimal)
		elif int(i) <= 3:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)

	# if it goes through a whole number of 4s and can't round up
	rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
	return float(rounded_number)


def round(passed_in_number: float, round_place: int = 0):
	'''
	Rounds a float just like the built in round function,
	except with more advanced rounding

	Rounder uses artificial intelligence to round beyond the point you want rounded
	for more precise rounding. So `3.45` rounded by the whole number using Rounder
	is `4`, but if you used the built-in round function it'd be `3`

	Made by Aethese :)

	Parameters
	----------
	passed_in_number : float
		number that needs to be rounded
	round_place : int
		place after decimal to be rounded. if not passed, defaults to whole number

	Returns
	-------
	number : any except float
		if a float isn't passed then the same value passed will be returned
	first_number : int
		if number is being rounded to a whole number than it will return rounded
		for whole number. ex: `4.5` is returned as `5` or `4.4` is returned as `4`
	rounded_number : float
		the actual rounded number that the user wants
	_return_handler : None, str, any
		depends on what the developer specified, but it can return None,
		an error string or raise an error, or whatever number was inputted
		as the options
	'''
	if not isinstance(passed_in_number, float):
		return _return_handler(passed_in_number,
			f'{passed_in_number} is a {type(passed_in_number).__name__}, not a float',
			ValueError)

	# we lose precision after rounding past the 15th round place
	if round_place > 15:
		round_place = 15
		if not disable_warnings:
			print('[Rounder] Warning: Automatically set round place to 15 digits')
	elif round_place < 0:  # no support for rounding the whole number in a specific spot
		round_place = 0
		if not disable_warnings:
			print('[Rounder] Warning: Automatically set round place to 0 digits')

	number_as_str = str(passed_in_number)  # not used again, except in split_number
	split_number = number_as_str.split('.')
	first_numbers = int(split_number[0])  # the whole number as int
	past_decimal = split_number[1]  # number(s) past the decimal as str

	# additional check to make sure there's only 15 digits past decimal
	if len(past_decimal) > 15:
		past_decimal = past_decimal[:15]

		if not disable_warnings:
			print('[Rounder] Warning: Automatically set digits past decimal place to just 15')

		# sometimes after limiting digits, the last number is an e or -
		# that causes errors so we remove them :)
		if past_decimal[-1] == 'e':
			past_decimal = past_decimal[:-1]
			# need to lower the round place in case there are conflicts
			if round_place == 15:
				round_place -= 1
			if not disable_warnings:
				print('[Rounder] Warning: Prevented error by removing leading \'e\'')
		elif past_decimal[-1] == '-':
			past_decimal = past_decimal[:-2]  # 2 spots because it's 'e-' at the end
			# lower round place like with 'e' but need to remove one more since 'e-'
			if round_place == 15:
				round_place -= 2
			elif round_place == 14:
				round_place -= 1
			if not disable_warnings:
				print('[Rounder] Warning: Prevented error by removing leading \'-\'')

	negative_number = bool(first_numbers < 0)

	# pre-checks complete, commence rounding B)
	if round_place == 0:
		if int(past_decimal[0]) >= 5:
			if negative_number:
				first_numbers -= 1
			else:
				first_numbers += 1

			return first_numbers
		elif int(past_decimal[0]) == 4:
			search = _search_number(round_place, first_numbers, past_decimal)
			search_split = str(search).split('.')

			if int(search_split[1][0]) >= 5:  # get first digit past decimal point
				if negative_number:
					first_numbers -= 1
				else:
					first_numbers += 1

				return first_numbers
			else:  # can not round up
				return int(search)
		else:  # numbers past decimal don't need rounding
			return first_numbers
	else:  # round past decimal point
		if len(past_decimal) < round_place:  # if available digits is smaller than round place
			return _return_handler(passed_in_number,
				f'Unable to round number. Number: {passed_in_number}, Round place: {round_place}',
				IndexError)

		# if round place is equal to the amount of digits available
		if len(past_decimal) == round_place:
			past_decimal += '0'

		if int(past_decimal[round_place]) >= 5:
			rounded_number = _round_past_decimal(round_place, first_numbers, past_decimal)
			return rounded_number
		elif int(past_decimal[round_place]) == 4:
			rounded_number = _search_number(round_place, first_numbers, past_decimal)
			return rounded_number
		else:
			rounded_number = str(first_numbers) + '.' + past_decimal[:round_place]
			return float(rounded_number)
