def file_transport():
    from sys import argv
    name = []
    if(len(argv) == 1):
        print("Set arguments")
        exit()
    for i in range(len(argv)):
        if(i == 0):
            pass
        else:
            name.append(argv[i])
    return name[0],name[1]

def prime_numbers(first,second):
	while (second < first):
		q1 = 2
		not_prime_number = False
		while((q1 < second)):
			if(not(second%q1)):
				not_prime_number = True
				break
			if(q1 <= 4):
				q1 += 1
			else:
				q1 += 2
		if(not_prime_number == False):
			file = open("y.csv","a")
			file.write("1,")
			file.close()
			file = open("x.csv","a")
			file.write(f"{second},")
			file.close()
		elif(not_prime_number == True):
			file = open("y.csv","a")
			file.write("0,")
			file.close()
			file = open("x.csv","a")
			file.write(f"{second},")
			file.close()
		second += 1
		
def main():
	first, second = file_transport()
	first, second = int(first), int(second)
	prime_numbers(first, second)
	return 0

if(__name__ == "__main__"):
	main()