from sys import *
RAM = []
for i in range(0, 64):
	RAM.append(0)


def read_file(filename):
	data = []

	#State refers to looking for numbers such as $ and &
	state = 0

	tok = ""
	for char in filename:
		tok += char
		print(tok)
		if tok == " " and state == 0:
			tok = ""
		elif tok == "\n" and state == 0:
			tok = ""
		elif (char == " " and state == 1) or (char == ";" and state == 1) or (char == "\n" and state == 1):
			data.append([tok[0:len(str(tok))-1], "data"])
			tok = ""
			state = 0

		elif tok == "mv":
			data.append([tok, "func"])
			tok = ""
		elif tok == "$" or tok == "&":
			data.append([tok, "ref"])
			tok = ""
			state = 1
	print(data)
	return data

def exe(data):
	global RAM
	i = 0

	print("EXE")
	while i < len(data):
		print(data[i])

		if data[i][1] == "func":
			if data[i+1][1] == "ref":
				if data[i+1][0] == "$":
					if data[i+3][0] == "&":
						RAM[int(data[i+4][0])] = data[i+2][0]
						print("Moving: ", data[i+2])

						i += 4

				elif data[i+1][0] == "&":
					if data[i+3][0] == "&":
						RAM[int(data[i+4][0])] = RAM[int(data[i+2][0])]
						RAM[int(data[i+2][0])] = 0

						i += 4

		i+=1




def open_file(filename):
	data = open(filename, "r").read()
	return data

def run():
	file = list(open_file(argv[1]))
	print(file)

	data = read_file(file)
	exe(data)


run()
print(RAM)