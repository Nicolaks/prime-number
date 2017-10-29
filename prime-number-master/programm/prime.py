import os
from math import *

# Function return true if a number is prime.
def is_prime(n):
	for i in range(2, int(sqrt(n)+1)):
		if n%i == 0:
			return False
	return True


# Create a while, with a top number, and check if the number
# is prime ans after put him in file.
def launch():
	n = int(input("What number should I go up to ? "))

	for p in range(2, n+1):
		if is_prime(p):
			print(p)
			prime_file = open("data.txt", "a")
			prime_file.write(str(p) + " " + str(is_prime(p)) + "\n")
			prime_file.close()


# Convert bytes.
def convert_bytes(num):
	global res
	res = num / 1024.0
	return res


# Allow to see the size of a file.
def file_size(file_path):
	if os.path.isfile(file_path):
		file_info = os.stat(file_path)
		return convert_bytes(file_info.st_size)


# Function who create new file if the file is > to 8 mo.
def create_file(name):
	new_file = open(name, "a")


# Main function who launch all the program.
def main():

	# Create alphabet to give name for files.
	alpha_grec = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
	 "theta", "iota", "kappa", "lambba", "mu", "nu", "xi", "omicron", "pi", "rho",
	  "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]

	launch()
	file_path = "data.txt"
	marks = str(int(file_size(file_path)))
	print(marks + " ko")

	name = "random"
	if res >= 1000:
		create_file(name)



main()
