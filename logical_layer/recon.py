import sys
from os import fdopen
from subprocess import Popen, PIPE, STDOUT

# from db_layer import Crud_operations


class Recon:
    def __init__(self, domain, lista):
        if domain:
            self.domain = domain
            self.op = "single"
        elif lista:
            self.lista = lista
            self.op = "list"
        # crudBD = Crud_operations()

    def start(self):
        if self.op == "single":
            cmd = (
                "docker run -it --rm -v \"/Tools/reconFTW/OutputFolder/\":'/reconftw/Recon/' six2dez/reconftw:main -s -d "
                + self.domain
            )
        elif self.op == "list":
            cmd = (
                "docker run -it --rm -v \"/Tools/reconFTW/OutputFolder/\":'/reconftw/Recon/' six2dez/reconftw:main -s -d "
                + self.lista
            )

        print("INICIANDO EXECUÇÃO DO RECON-FTW...")
        print("Comando: " + cmd)
        self.execute(cmd)
        print("RECON-FTW terminou de processar")

        domainDir = "/Tools/reconFTW/OutputFolder/" + self.domain
        cmd = (
            r"cat "
            + domainDir
            + r"/webs/webs.txt | sed -E 's/^\s*.*:\/\///g' > "
            + domainDir
            + r"/webSubs.txt"
        )
        self.execute(cmd)

        cmd = (
            "sort -u "
            + domainDir
            + "/webSubs.txt "
            + domainDir
            + "/subdomains/subdomains.txt > "
            + domainDir
            + "/allSubs.txt"
        )
        self.execute(cmd)
        # with open(domainDir+"/allSubs.txt") as subs:
        #    crudBD.insert_Subs(self.domain, subs, 'reconftw')

    def execute(self, cmd):
        with Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT) as sp:
            with fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
                for line in sp.stdout:
                    stdout.write(line)
                    stdout.flush()

    def get_output(self):
        return self.output
