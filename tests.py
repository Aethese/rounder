import os
import rounder
os.system('cls' if os.name == 'nt' else 'clear')  # don't ask


try:  # Test 1
	test_1a = rounder.round(4.5, 0)
	test_1b = rounder.round(4.4)
except Exception as e:
	print('Test 1 failed with error:', e)

if test_1a == 5 and test_1b == 4:
	print('Test 1 passed')
else:
	print('Test 1 failed:', test_1a, test_1b)


try:  # Test 2
	test_2a = rounder.round(3.45631, 3)
	test_2b = rounder.round(3.45691, 3)
except Exception as e:
	print('Test 2 failed with error:', e)

if test_2a == 3.456 and test_2b == 3.457:
	print('Test 2 passed')
else:
	print('Test 2 failed:', test_2a, test_2b)


try:  # Test 3
	test_3a = rounder.round(3.45112, 1)
	test_3b = rounder.round(3.41112, 1)
except Exception as e:
	print('Test 3 failed with error:', e)

if test_3a == 3.5 and test_3b == 3.4:
	print('Test 3 passed')
else:
	print('Test 3 failed:', test_3a, test_3b)


try:  # Test 4
	test_4a = rounder.round('penis', 1)
	test_4b = rounder.round('yes')
except Exception as e:
	print('Test 4 failed with error:', e)

if test_4a == 'penis' and test_4b == 'yes':
	print('Test 4 passed')
else:
	print('Test 4 failed:', test_4a, test_4b)


custom_test_5a = float(input('Custom test: '))  # Test 5
custom_test_5b = int(input('What digit place? '))
print(rounder.round(custom_test_5a, custom_test_5b))
