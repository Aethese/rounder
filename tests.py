import os, time
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
	test_4a = rounder.round('not inappropriate', 1)
	test_4b = rounder.round('yes')
except Exception as e:
	print('Test 4 failed with error:', e)

if test_4a == 'not inappropriate' and test_4b == 'yes':
	print('Test 4 passed')
else:
	print('Test 4 failed:', test_4a, test_4b)


try:
	start_time1 = time.time()
	rounder.round(3.14159, 4)
	finish_time1 = time.time() - start_time1
	finish_time1a = rounder.round(finish_time1, 2)  # hehe

	start_time2 = time.time()
	round(3.14159, 4)
	finish_time2 = time.time() - start_time1
	finish_time2a = rounder.round(finish_time2, 2)
except Exception as e:
	print('Test 5 failed with error:', e)

print('Test 5 passed with times:')
print(finish_time1a, 'for rounder')
print(finish_time2a, 'for built in round')

print(finish_time1, 'rounder full number')
print(finish_time2, 'built in round full number')
