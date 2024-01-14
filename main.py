from logical_layer import Cli_Executor

teste = Cli_Executor()

teste.execute("cat launch.json")

print(teste.get_output())
