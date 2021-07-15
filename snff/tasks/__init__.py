from snff.tasks.environment import execute as exec_environment
from snff.tasks.console import execute as exec_console

__tasks = []
__tasks.append(exec_console)
__tasks.append(exec_environment)

def execute() -> None:
    for task in __tasks:
        task()
