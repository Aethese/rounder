'''
Rounding module that rounds a float just like the built in round function lol
'''

def round(number: float, round_place: int = 0):
	'''
	Rounds a float just like the built in round function lol

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
	'''
	is_float = isinstance(number, float)
	if not is_float:
		return number

	number_to_str = str(number)
	split_number = number_to_str.split('.')
	past_decimal = split_number[1]  # number(s) past the decimal

	if round_place == 0:
		first_number = int(split_number[0])
		if int(past_decimal) >= 5:
			first_number += 1
			return first_number
		else:
			return first_number

	return split_number  # just for now :)
