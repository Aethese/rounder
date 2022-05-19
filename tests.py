import os, time
import rounder
os.system('cls' if os.name == 'nt' else 'clear')

failed = 0
rounder.disable_warnings = False

print(f'Running Rounder version {rounder.__version__}')

try:  # Test 1
	test_1a = rounder.round(4.5191, 0)
	test_1b = rounder.round(4.4191)
except Exception as e:
	print('Test 1 failed with error:', e)
	failed += 1

if test_1a == 5 and test_1b == 4 and type(test_1a).__name__ == 'int' and type(test_1b).__name__ == 'int':
	print('Test 1 passed')
else:
	print('Test 1 failed:', test_1a, test_1b)
	failed += 1


try:  # Test 2
	test_2a = rounder.round(3.45631, 3)
	test_2b = rounder.round(3.45691, 3)
except Exception as e:
	print('Test 2 failed with error:', e)
	failed += 1

if test_2a == 3.456 and test_2b == 3.457 and type(test_2a).__name__ == 'float' and type(test_2b).__name__ == 'float':
	print('Test 2 passed')
else:
	print('Test 2 failed:', test_2a, test_2b)
	failed += 1


try:  # Test 3
	test_3a = rounder.round(3.45112, 1)
	test_3b = rounder.round(3.41112, 1)
except Exception as e:
	print('Test 3 failed with error:', e)
	failed += 1

if test_3a == 3.5 and test_3b == 3.4 and type(test_3a).__name__ == 'float' and type(test_3b).__name__ == 'float':
	print('Test 3 passed')
else:
	print('Test 3 failed:', test_3a, test_3b)
	failed += 1


try:  # Test 4
	rounder.return_format = 'same_number'
	test_4a = rounder.round('not inappropriate', 1)

	rounder.return_format = 'error_message'
	test_4b = rounder.round(3.14, 5)
except Exception as e:
	print('Test 4 failed with error:', e)
	failed += 1

test_4b_error = '[Rounder] Unable to round number. Number: 3.14, Round place: 5'
if test_4a == 'not inappropriate' and test_4b == test_4b_error and type(test_4a).__name__ == 'str' and type(test_4b).__name__ == 'str':
	print('Test 4 passed')
else:
	print('Test 4 failed:', test_4a, test_4b)
	failed += 1


try:  # Test 5
	start_time1 = time.time()
	rounder.round(3.14159, 2)
	rounder.round(3.14159, 3)
	rounder.round(3.14159, 4)
	finish_time1 = time.time() - start_time1
	finish_time1a = rounder.round(finish_time1, 2)  # hehe

	start_time2 = time.time()
	round(3.14159, 2)
	round(3.14159, 3)
	round(3.14159, 4)
	finish_time2 = time.time() - start_time1
	finish_time2a = rounder.round(finish_time2, 2)
except Exception as e:
	print('Test 5 failed with error:', e)
	failed += 1

print('Test 5 passed with times:')
print(finish_time1a, 'for Rounder')
print(finish_time2a, 'for built-in round')

print(finish_time1, 'Rounder full number')
print(finish_time2, 'built-in round full number')


try:  # test 6
	test_6a = rounder.round(3.99, 1)
	test_6b = rounder.round(3.44512)
except Exception as e:
	print('Test 6 failed with error:', e)
	failed += 1

if test_6a == 4 and test_6b == 4 and type(test_6a).__name__ == 'int' and type(test_6b).__name__ == 'int':
	print('Test 6 passed')
else:
	print('Test 6 failed:', test_6a, test_6b)
	failed += 1


try:  # Test 7
	test_7a = rounder.round(2.444444444444)
	test_7b = rounder.round(2.444444444445)
except Exception as e:
	print('Test 7 failed with error:', e)
	failed += 1

if test_7a == 2 and test_7b == 3 and type(test_7a).__name__ == 'int' and type(test_7b).__name__ == 'int':
	print('Test 7 passed')
else:
	print('Test 7 failed:', test_7a, test_7b)
	failed += 1


try:  # Test 8
	test_8a = rounder.round(-3.5)
	test_8b = rounder.round(-3.3445)
except Exception as e:
	print('Test 8 failed with error:', e)
	failed += 1

if test_8a == -4 and test_8b == -3 and type(test_8a).__name__ == 'int' and type(test_8b).__name__ == 'int':
	print('Test 8 passed')
else:
	print('Test 8 failed:', test_8a, test_8b)
	failed += 1


try:  # Test 9
	test_9a = rounder.round(3.123124914285135135134, 3)
	rounder.return_format = 'none'
	test_9b = rounder.round(3.14319041930434, 20)
except Exception as e:
	print('Test 9 failed with error:', e)
	failed += 1

if test_9a == 3.123 and test_9b == None and type(test_9a).__name__ == 'float':
	print('Test 9 passed')
else:
	print('Test 9 failed:', test_9a, test_9b)


try:  # Test 10
	rounder.return_format = 'raise_error'
	test_10 = rounder.round(3.14319041930434, 20)
except IndexError:
	print('Test 10 passed')
except Exception as e:
	print('Test 10 failed with error:', e)
	failed += 1
rounder.return_format = 'same_number'  # reset return_format


try:  # Test 11
	test_11a = rounder.round(-3.9)
	test_11b = rounder.round(-3.447)
except Exception as e:
	print('Test 11 failed with error:', e)
	failed += 1

if test_11a == -4 and test_11b == -4 and type(test_11a).__name__ == 'int' and type(test_11b).__name__ == 'int':
	print('Test 11 passed')
else:
	print('Test 11 failed:', test_11a, test_11b)
	failed += 1


try:  # Test 12
	test_12a = rounder.round(4.112309, 5)
	rounder.return_format = 'same_number'
	test_12b = rounder.round(4.1933012, 12)
except Exception as e:
	print('Test 12 failed with error:', e)
	failed += 1

if test_12a == 4.11231 and test_12b == 4.1933012 and type(test_12a).__name__ == 'float' and type(test_12b).__name__ == 'float':
	print('Test 12 passed')
else:
	print('Test 12 failed:', test_12a, test_12b)
	failed += 1


try:  # Test 13
	test_13a = rounder.round(341.4)
	test_13b = rounder.round(341.5)
except Exception as e:
	print('Test 13 failed with error:', e)
	failed += 1

if test_13a == 341 and test_13b == 342 and type(test_13a).__name__ == 'int' and type(test_13b).__name__ == 'int':
	print('Test 13 passed')
else:
	print('Test 13 failed:', test_13a, test_13b)
	failed += 1


try:  # Test 14
	test_14a = rounder.round(341.4897, -1)
	test_14b = rounder.round(.1, -3)
except Exception as e:
	print('Test 14 failed with error:', e)
	failed += 1

if test_14a == 342 and test_14b == 0 and type(test_14a).__name__ == 'int' and type(test_14b).__name__ == 'int':
	print('Test 14 passed')
else:
	print('Test 14 failed:', test_14a, test_14b)
	failed += 1


try:  # Test 15
	rounder.return_format = 'none'
	test_15a = rounder.round(3.1, 1)
	test_15b = rounder.round(3.6, 1)
except Exception as e:
	print('Test 15 failed with error:', e)
	failed += 1

if test_15a == 3.1 and test_15b == 3.6 and type(test_15a).__name__ == 'float' and type(test_15b).__name__ == 'float':
	print('Test 15 passed')
else:
	print('Test 15 failed:', test_15a, test_15b)
	failed += 1


print(f'\n{failed} test(s) failed')
if failed >= 1:
	exit(1)
