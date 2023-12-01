#!python3

import re

def main():
	with open("test.txt", 'r') as f:
		total = 0;
		for l in f:
			val = ""
			b = re.search(r'\d', l)
			val += b.group()[0]
			e = re.search(r'\d', l[::-1])
			val += e.group()[0]
			print(val)
		print(total)
if __name__ == '__main__':
	main()