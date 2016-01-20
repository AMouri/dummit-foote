def add(a, b, n):
	inter = a + b
	return inter - (inter / n) * n

def multiply(a, b, n):
	inter = a * b
	return inter - (inter / n) * n

def gcd(a, n):
	def recurse(x, y):
		if y == 0:
			return (x, 1, 0)
		else:
			(d, a, b) = recurse(y, x % y)
			return (d, b, a - (x / y) * b)
	result = recurse(a, n)
	if result[0] == 1:
		return result[1] - (result[1] / n) * n
	else:
		return None

