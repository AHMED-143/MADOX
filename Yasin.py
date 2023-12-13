import os
import zlib
import time
import base64


logo=("""

██    ██  █████  ███████ ██ ███    ██ 
 ██  ██  ██   ██ ██      ██ ████   ██ 
  ████   ███████ ███████ ██ ██ ██  ██ 
   ██    ██   ██      ██ ██ ██  ██ ██ 
   ██    ██   ██ ███████ ██ ██   ████ 
\x1b[38;5;51m─────────────────────────────────────────────\033[1;37m
 [×] OWNER  > YASIN ARAFAT
 [×] GITHUB > AHMED-143
 [×] TOOLS  > DECODER
\x1b[38;5;51m─────────────────────────────────────────────\033[1;37m""")


print(logo)
def clear():
	os.system('clear')
	print(logo)
	
def line():
    print(f"\x1b[38;5;51m─────────────────────────────────────────────\033[1;37m")
 
def yasin():
	clear()
	print(" [1] TRY NORMAL DECODE ")
	line()
	axy=input(" [?] CHOICE OPTION : ")
	if axy in ["1"]:
		print(" \033[1;32mWAIT FOR DECODE TOOLS OPENING\033[1;37m\n");time.sleep(5)
		xxx()
	else:
		exit()


def xxx():
	clear()
	print(f" [A] ZLIB ")
	print(f" [B] BASE64 ")
	line()
	op=input(" [x] CHOICE : ")
	if op in ["A"]:
		zlib()
	elif op in ["B"]:
		base()
	else:
		exit()

def zlib():
	clear()
	print(f' [A] Zlib ENCODE ')
	print(f' [B] Zlib DECODE ')
	print(f' [x] BACK TO MENU ')
	line()
	x = input(f" [?] CHOICE : ")
	if x in ["A"]:
		encode()
	elif x in ["B"]:
		decode()
	elif x in ["x"]:
		yasin()
	else:
		exit()
		

def decode():
	clear()
	put=input(' put text here > ')
	main=eval(put)
	dec=zlib.decompress(main)
	print(dec.decode('utf-8'))
	

def encode():
	clear()
	put=input(' PUT TEXT HERE > ')
	byte = put.encode('utf-8')
	compile = zlib.compress(byte)
	print(compile)

def base():
	clear()
	print(f' [A] BASE64 ENCODE ')
	print(f' [B] BASE64 DECODE ')
	print(f' [x] BACK TO MENU ')
	line()
	x = input(f" [?] CHOICE : ")
	if x in ["A"]:
		hex()
	elif x in ["B"]:
		dex()
	elif x in ["x"]:
		yasin()
	else:
		exit('FUCK YOU ')

def dex():
	clear()
	put = input('PUT TEXT HERE > ')
	main=eval(put)
	encode = base64.b64decode(main).decode('utf-8')
	print(encode)
def hex():
	clear()
	put = input('put Text here > ')
	byte = put.encode('utf-8')
	compile = base64.b64encode(byte)
	print(compile)
yasin()
