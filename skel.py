#!/usr/bin/python3

import sys
import os

if len(sys.argv)<2:
    print("Usage: skel <binary>")
    sys.exit(0)

program = str(sys.argv[1])
current = os.getcwd()

skel = '''#!/usr/bin/python3
from pwn import *
gs = \'\'\'
continue
\'\'\'
elf = context.binary = ELF('./{}')
context.terminal = ['tmux', 'splitw', '-hp', '70']

def start():
    if args.GDB:
        return gdb.debug('./{}', gdbscript=gs)
    if args.REMOTE:
        return remote('127.0.0.1', 5555)
    else:
        return process('./{}')
r = start()
#========= exploit here ===================



#========= interactive ====================
r.interactive()
'''.format(program, program, program)
try:
    with open('xpl.py', 'w') as f:
        f.write(skel)
        f.close()
except:
    print("Can't write xpl.py!")
