'''
Rounding module that rounds a float just like the built in round function lol
'''

def round(number: float, round_place: int = 1):
	'''
	Rounds a float just like the built in round function lol

	Parameters
	----------
	number : float
		number that needs to be rounded
	round_place : int
		place after decimal to be rounded. if not passed defaults to the 10th place
	
	Returns
	-------
	number : any except float
		if a float isn't passed then the same value passed will be returned
	'''
	is_float = isinstance(number, float)
	if not is_float:
		return number

	number_to_str = str(number)
	split_number = number_to_str.split('.')
	past_decimal = split_number[1]

	return 	split_number