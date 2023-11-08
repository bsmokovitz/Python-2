def is_prime(num):
    #
# Write your code here.
#
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()