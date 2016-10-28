col1_r6 = " "
col1_r5 = " "
col1_r4 = " "
col1_r3 = " "
col1_r2 = " "
col1_r1 = " "
col1_r0 = " "

col2_r6 = " "
col2_r5 = " "
col2_r4 = " "
col2_r3 = " "
col2_r2 = " "
col2_r1 = " "
col2_r0 = " "

col3_r6 = " "
col3_r5 = " "
col3_r4 = " "
col3_r3 = " "
col3_r2 = " "
col3_r1 = " "
col3_r0 = " "

col4_r6 = " "
col4_r5 = " "
col4_r4 = " "
col4_r3 = " "
col4_r2 = " "
col4_r1 = " "
col4_r0 = " "

col5_r6 = " "
col5_r5 = " "
col5_r4 = " "
col5_r3 = " "
col5_r2 = " "
col5_r1 = " "
col5_r0 = " "

col6_r6 = " "
col6_r5 = " "
col6_r4 = " "
col6_r3 = " "
col6_r2 = " "
col6_r1 = " "
col6_r0 = " "

col7_r6 = " "
col7_r5 = " "
col7_r4 = " "
col7_r3 = " "
col7_r2 = " "
col7_r1 = " "
col7_r0 = " "







bored = [
	["|", col1_r6, "-", col2_r6, "-", col3_r6, "-", col4_r6, "-", col5_r6, "-", col6_r6, "-", col7_r6, "|"],
	["|", col1_r5, "-", col2_r5, "-", col3_r5, "-", col4_r5, "-", col5_r5, "-", col6_r5, "-", col7_r5, "|"],
	["|", col1_r4, "-", col2_r4, "-", col3_r4, "-", col4_r4, "-", col5_r4, "-", col6_r4, "-", col7_r4, "|"],
	["|", col1_r3, "-", col2_r3, "-", col3_r3, "-", col4_r3, "-", col5_r3, "-", col6_r3, "-", col7_r3, "|"],
	["|", col1_r2, "-", col2_r2, "-", col3_r2, "-", col4_r2, "-", col5_r2, "-", col6_r2, "-", col7_r2, "|"],
	["|", col1_r1, "-", col2_r1, "-", col3_r1, "-", col4_r1, "-", col5_r1, "-", col6_r1, "-", col7_r1, "|"],
	["|", col1_r0, "-", col2_r0, "-", col3_r0, "-", col4_r0, "-", col5_r0, "-", col6_r0, "-", col7_r0, "|"],
]

def print_bored(bored):
	for i in bored:
		print("".join(i))

turn = 0

while True:
	print_bored(bored)

	x = int(input("\nWhich colum would you like(1-7)? "))
	

	if x == 1:
		x = 1
	elif x == 2:
		x = 3
	elif x == 3:
		x = 5
	elif x == 4:
		x = 7
	elif x == 5:
		x = 9
	elif x == 6:
		x = 11
	elif x == 7:
		x = 13
		
	for i in range(len(bored)-1, 0, -1):
		if bored[i][x] == " ":
			bored[i][x] = "O"
			break
		
	for i in range(0,len(bored)-1):
		for n in range(0,len(bored[0])-1):
			if bored[i][n] == "O":
				for y in range(0,4):
					if bored[(i+y)-1][(n+y)-1] == "O":
						print("You Win")