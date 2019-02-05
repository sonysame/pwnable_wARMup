### pwnable_wARMup

The architecture of this binary is ARM.  

#### main function
![](https://user-images.githubusercontent.com/24853452/52264299-9f799000-2974-11e9-87e5-7423d391545e.png)

*read function* can accept user input in maximum 0x78bytes. However, the stack buffer is 0x68bytes. Therefore by using stack-overflow, we can overwrite the return address. 

## 1. Use only ROP (ASLR)
#### Gadget1
![](https://user-images.githubusercontent.com/24853452/52265120-af926f00-2976-11e9-8983-1a005957f881.png)

#### Gadget2
![](https://user-images.githubusercontent.com/24853452/52275199-2d17a880-2992-11e9-9ef5-33ec5c9b056e.png)


1) Move the flow of program to Gadget1 and make r3 the address of puts@got.  
 
2) Move the flow to Gadget2. Now, r0 is puts@got. (mov r0, r3)  

3) Move the flow to 0x10528 which calls puts@plt. Now, we can leak the real address of function *puts*. By calculating the offset, we can get the real address of function *string*. Also, give the input including "/bin/sh\x00" in order to fix the address of "/bin/sh\x00"   

4) Move the flow to Gadget1 and make r3 the address of puts@got. 

5) Move the flow to 0x10534 which moves r3 to r1 and calls read@plt. Now we can store the address of system into puts@got.  

6) Move the flow to Gadget1 and make r3 the address of "/bin/sh\x00".  

7) Move the flow to Gadget2. Now, r0 is the address of "/bin/sh"\x00. (mov r0, r3) 

8) Move the flow to 0x10528 which calls puts@plt with argument in r0. This means, we call system function with argument "/bin/sh\x00"

After I got the flag, I noticed that the libc address is fixed:)


***

## 2. Use NX
Qemu is not stuck in NX, so we can also use shellcode in stack.  

However, we do not know the stack address, and it is not fixed. So we will use ROP and *read function* one more time.

#### Gadget1
![](https://user-images.githubusercontent.com/24853452/52265120-af926f00-2976-11e9-8983-1a005957f881.png)


1) Move flow to Gadget1 and make r3 the address of certain stack area.   
 
2)  Move the flow to 0x10534 which moves r3 to r1 and calls read@plt. Give shellcode as a read function input. Now we can store shellcode to stack area and we know the accurate address of shellcode.

3) Move the flow to shellcode!

