### pwnable_wARMup

The architecture of this binary is ARM.  

#### main function
![](https://user-images.githubusercontent.com/24853452/52264299-9f799000-2974-11e9-87e5-7423d391545e.png)

*read function* can accept user input in maximum 0x78bytes. However, the stack buffer is 0x68bytes. Therefore by using stack-overflow, we can overwrite the return address. Qemu is not stuck in NX, so we will write shellcode in stack, and execute it to get the shell!  

However, we do not know the stack address, and it is not fixed. So we will use ROP and *read function* one more time.

----------

![](https://user-images.githubusercontent.com/24853452/52265258-fe400900-2976-11e9-961d-2222c349bb66.png)


----------

0x1054c: pop {r11, pc}

r11 <-0xf6ffe010, pc <- 0x10364

----------

![](https://user-images.githubusercontent.com/24853452/52265120-af926f00-2976-11e9-8983-1a005957f881.png)

r3 <- 0xxf6ffe010, pc <-0x10534

----------

![](https://user-images.githubusercontent.com/24853452/52265412-6131a000-2977-11e9-815c-dfed323b2c70.png)

read(0, 0xf6ffe010, 0x78) will be executed.  
0xf6ffe010 <- 0xf6ffe014+shellcode

0x10548: sub, sp, r11, #4  
sp <- 0xf6ffe00c  

0x1054c: pop {r11, pc}  
r11 <-[0xf6ffe00c], pc <- [0xf6ffe010]=0xf6ffe014(shellcode)
