import os
import argparse
from logical_layer import Recon

if __name__ == "__main__":
    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recon",
        dest="recon",
        action="store_true",
        help="Comando para rodar ferramentas de reconhecimento e gravar no BD",
    )
    parser.add_argument(
        "--domain",
        help="Especifica um unico domínio para rodar as ferramentas de recon",
    )
    parser.add_argument(
        "--listfile",
        help="Especifica um arquivo com lista de domínios para rodar as ferramentas de recon",
    )
    args = parser.parse_args()

    if not args.recon:
        print("Escolha uma opção. -h para ajuda")
        exit()

    if args.recon and (
        (args.domain and args.listfile) or (not args.domain and not args.listfile)
    ):
        print("Para opção --recon passe um dominio ou um arquivo com lista de dominios")
        exit()

    if args.listfile:
        if not os.path.isfile(args.listfile):
            print("Arquivo contendo lista de dominios não encontrado")
            exit()

    recon = Recon(args.domain, args.listfile)
    recon.start()

#

# teste = Cli_Executor()

# teste.execute("cat launch.json")

# print(teste.get_output())
