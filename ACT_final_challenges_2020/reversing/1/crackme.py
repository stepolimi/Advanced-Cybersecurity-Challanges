'''
tT make the program debuggable with gdb, we should go after the signal call in the main and before the call of "int3" and execute "handle 5 pass" to let the SIGTRAP signal to go to the right function inside the catch, make a step and stop passing SIGTRAP to the program with "handle 5 nopass" and continue the right execution of it.

gdb crackme
start flag{l0v3ly_4nt1r3v_tr1ck5_w_s1gn4l5}
n
n
n
n
n
n
n
n
n
n
n
handle 5 pass
n
handle 5 nopass
n
b *0x5555555547dc
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
q

The commented section above is the final cycle that I used to find the flag, at each cycle I added a c to go to the next check of the program and the found character to be given in input to the program.
the breakpoint is at each cycle in the xor where rax is the value that is been xored with the input and the result sould be equal to the global variable[i] that can be seen on ghidra at &DAT_00100970. By putting
the value of rax in given and the value of the global variable in target the small script under here finds the ith value of the key.

It is probably not a pretty solution but a working one if u have around 30 minutes to spare.

'''

target = 0x17
given = 0x73
for i in range(0x29,0x7e):
	if(i ^ given == target):
		print (chr(i))