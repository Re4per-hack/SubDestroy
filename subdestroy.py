import requests, signal, argparse, sys
from pwn import  * 

parser = argparse.ArgumentParser(description='Subdomain fuzzer')

parser.add_argument('-t','--target', help='IP (Obligatory)')
parser.add_argument('-d','--domain', help='Domain example.com (Obligatory)')
parser.add_argument('-w', '--wordlist', help='URL wordlist (Obligatory)')
parser.add_argument('-p','--protocol', help='Select Protocol |https/http| (Optional-Default=http)')
args = parser.parse_args()
if args.target is None or args.wordlist is None or args.domain is None:
    print(parser.print_help())
    sys.exit(1)
else: 
    if args.protocol == "http" or None :
        protocol = "http://"
    elif args.protocol == "https":
        protocol = "http://"
    else: 
        protocol = "http://"
    words = log.progress('Subdominio:')
    results = log.progress('Subdomains founded:')
    domain = args.domain    
    target = args.target
    subdomains = ("")
    ruta = args.wordlist
    with open(ruta) as wordlist:
        for sub in wordlist:
            url = (f"{protocol}{target}")
            sub_fix = sub.strip()
            words.status(sub_fix)
            header = {"Host": f"{sub_fix}.{domain}"}
            page = requests.get(url=url, headers=header, allow_redirects=False)
            status = str(page)
            if "200" in status: 
                subdomains += (f"{sub_fix} ")
                results.status(subdomains)
        print("[!] The attack ended")