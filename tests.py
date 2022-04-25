import os
import rounder
os.system('cls' if os.name == 'nt' else 'clear')


try:
	test_1a = rounder.round(4.5, 0)
	test_1b = rounder.round(4.4, 0)
except Exception as e:
	print('Test 1 failed with error:', e)

if test_1a == 5 and test_1b == 4:
	print('Test 1 passed')
else:
	print('Test 1 failed:', test_1a, test_1b)
