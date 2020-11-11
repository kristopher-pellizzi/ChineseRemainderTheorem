from EuclidMCD import *
import argparse
from functools import reduce

def CRT(equations):
	Mt = reduce(lambda acc, val: acc * val, map(lambda x: x[1], equations), 1)
	M = tuple(map(lambda x: Mt // x[1], equations))
	l = [None] * len(equations)

	sol = 0
	for i in range(len(equations)):
		l[i] = euclid_core(M[i], equations[i][1])[1 if M[i] > equations[i][1] else 2]
		sol += equations[i][0] * l[i] * M[i]

	return (sol % Mt, Mt)

def poly_CRT(equations, modulus):
	Mt = reduce(lambda acc, val: poly_mul(acc, val), map(lambda x: x[1], equations), (1, ))
	M = tuple(map(lambda x: (poly_division(Mt, x[1]) if not modulus else poly_mod_division(poly_mod_normalize(Mt, modulus), poly_mod_normalize(x[1], modulus), modulus))[0], equations))
	l = [None] * len(equations)

	sol = (0, )
	for i in range(len(equations)):
	
		l[i] = poly_euclid_core(M[i], equations[i][1], modulus)[1 if len(M[i]) > len(equations[i][1]) else 2]
		curr_product = poly_mul(equations[i][0], poly_mul(l[i], M[i]))
		if modulus:
			curr_product = poly_mod_normalize(curr_product, modulus)
		sol = poly_sum(sol, curr_product)

	return ((poly_division(sol, Mt) if not modulus else poly_mod_division(poly_mod_normalize(sol, modulus), poly_mod_normalize(Mt, modulus), modulus))[1], Mt if not modulus else poly_mod_normalize(Mt, modulus))

def poly_sum(f, g):
	lf = len(f)
	lg = len(g)
	if lf < lg:
		f = [0 for i in range(lg-lf)] + list(f)
	elif lg < lf:
		g = [0 for i in range(lf-lg)] + list(g)

	l = list(map(lambda x, y: 0 if math.isclose(x, -y, abs_tol = 0.0001) else x + y, f, g))
	return remove_leading_zeros(l)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Application of Chinese Remainder Theorem (CRT) to compute solution of a system of modular equations")
	parser.add_argument('vals', nargs = '+')
	parser.add_argument('-m', nargs = '?', default=None)
	parser.add_argument('--poly', action='store_true', default=False)
	namespace = parser.parse_args()
	if len(namespace.vals) < 2:
		raise RuntimeError("Must pass at least 2 equations")
		exit(-1)
	if not namespace.poly:
		# Convert string input into tuples of couple of integers
		equations = tuple(map(lambda x: tuple(map(lambda y: int(y.strip()), x.strip().split('%'))), namespace.vals))
		sol = CRT(equations)
		print("{0} mod {1}".format(sol[0], sol[1]))
		print()
		exit(0)

	if namespace.m:
		namespace.m = int(namespace.m)
	# Convert string input into tuples of couple of polynomes
	equations = tuple(map(lambda x: tuple(map(lambda y: tuple(map(lambda z: float(z.strip()), tuple(y.strip().split(',')))), x.strip().split('%'))), namespace.vals))
	sol = poly_CRT(equations, namespace.m)
	print("({0}) mod ({1})".format(poly_string(sol[0]), poly_string(sol[1])))
	print()


