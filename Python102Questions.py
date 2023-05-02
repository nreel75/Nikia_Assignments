def hello_name(user_name):
	print(user_name)

hello_name("Jared")


def first_odds():
	odd_numbers = list(range(1,100,2))
	print(odd_numbers)

first_odds()

def max_num_in_list(a_list):
	print (max(a_list))

max_num_in_list([1, 2, 43, 4, 55, 6, 67, 78, 9,79])

def is_leap_year(a_year):
	if a_year%4 == 0 and a_year%100 != 0:
		return True
	elif a_year%4 == 0 and a_year%400 == 0:
		return True
	else:
		return False

print(is_leap_year(2024))


def is_consecutive(a_list):
	if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
		return True
   
is_consecutive([8, 2, 3, 1, 6, 7, 4, 5, 9])