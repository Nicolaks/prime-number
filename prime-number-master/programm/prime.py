# <thanks to https://stackoverflow.com/users/166949/steveha
import os

# Function return true if a number is prime.
def is_prime(n):
	for i in range(2, n):
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


# Convert bytes
def convert_bytes(num):
	res = num / 1024.0
	return res


# Allow to see the size of a file
def file_size(file_path):
	if os.path.isfile(file_path):
		file_info = os.stat(file_path)
		return convert_bytes(file_info.st_size)


# Main function who launch all the program.
def main():
	launch()
	file_path = "data.txt"
	marks = str(int(file_size(file_path)))
	print(marks + " ko")


main()
