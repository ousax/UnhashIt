from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from os.path import exists, isfile
from sys import argv
from colorama import Fore
text = argv[1] if len(argv) > 1 else "r" # required
psw = argv[2] if len(argv) > 2 else "r"
while text == "r" or text == "":
    text = str(input(Fore.GREEN+'Text: '+Fore.RESET))
while psw == "r" or not exists(psw):
    psw = str(input(Fore.GREEN+"Enter the password path, name: "+Fore.RESET))
class Unhashme:
    # echo -n "string" | sha1sum 
    # sha1('string\n'.encode()).hexdiges()
    def __init__(self, text, psw):
        self.text = text
        self.psw = psw
        if not exists(psw) and not isfile(psw):
            exit(f"{psw} is not valid password file!.")
        else:
            if len(text) not in [32, 40, 56, 64, 96, 128]:
                exit()
            else:
                print(len(text))
                try:
                    with open(psw, 'r') as PSW:
                        Psw = (PSW.readlines())
                        if len(text) == 32:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if md5(f"{x}\n".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                    break
                                else:
                                    pass
                        elif len(text) == 56:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if sha224(f"{x}".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                    break
                                else:
                                    pass
                        elif len(text) == 40:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if sha1(f"{x}".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                    break
                                else:
                                    pass
                        elif len(text) == 64:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if sha256(f"{x}".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                    break
                                else:    
                                    pass
                        elif len(text) == 96:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if sha384(f"{x}".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                else:
                                    pass
                        elif len(text) == 128:
                            for x in Psw:
                                x = x.replace('\n', '')
                                if sha512(f"{x}".encode('utf-8')).hexdigest() == text:
                                    print(Fore.YELLOW+x, text+Fore.RESET)
                                    break
                                else:
                                    pass
                except Exception as MainError:
                    exit(MainError)
Unhashme(text, psw)
