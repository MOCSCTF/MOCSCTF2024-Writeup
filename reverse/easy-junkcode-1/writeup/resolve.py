flag_0=[0x7c, 0xe, 0x12, 0x32, 0x72, 0x15, 0x17, 0x1a, 0x72, 0x71, 0x3f, 0x6, 0x43, 0x0, 0x25, 0x14, 0x5d, 0x20, 0x25, 0x8, 0x1, 0x2f, 0x22, 0x3e, 0x68, 0x71, 0x24, 0x3e, 0x5a, 0x2f, 0x61, 0x16, 0x6e, 0x2b, 0x24, 0x2f, 0x5a, 0x1e, 0x32, 0x51, 0x55, 0x24, 0x2c]
flag_2=[0x31, 0x41, 0x51, 0x61]
flag=""
cnt = 0
for i in flag_0:
    flag += chr(i^flag_2[cnt])
    cnt = cnt+1
    if cnt==4:
        cnt = 0
print(flag)