import os


class Cli_Executor:
    def __init__(self):
        self.output = None

    def execute(self, command):
        self.output = os.popen(f"{command}").read()

    def get_output(self):
        return self.output
