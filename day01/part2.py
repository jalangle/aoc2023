#!python3

import re

def cap_to_value(v):

	if v == "one" or v == "eno":
		return "1"
	if v == "two" or v == "owt":
		return "2"
	if v == "three" or v == "eerht":
		return "3"
	if v == "four" or v == "ruof":
		return "4"
	if v == "five" or v == "evif":
		return "5"
	if v == "six" or v == "xis":
		return "6"
	if v == "seven" or v == "neves":
		return "7"
	if v == "eight" or v == "thgie":
		return "8"
	if v == "nine" or v == "enin":
		return "9"
	return v

def main():
	with open("input.txt", 'r') as f:
		total = 0;
		for l in f:
			val = ""
			b = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', l)
			if b:
				val += cap_to_value(b.group()[::-1])
			e = re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', l[::-1])
			if e:
				val += cap_to_value(e.group()[::-1])
			else:
				print("WTF")
			print(val)
			total += int(val)
		print(total)
if __name__ == '__main__':
	main()