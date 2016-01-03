def gcd(a, b):
	def recurse(x, y):
		if y == 0:
			return (x, 1, 0)
		else:
			(d, a, b) = recurse(y, x % y)
			return (d, b, a - (x / y) * b)
	result = recurse(a, b)
	print "GCD is " + str(result[0])
	print "a = " + str(result[1])
	print "b = " + str(result[2])