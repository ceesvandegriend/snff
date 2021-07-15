from snff.tasks.environment import execute as exec_environment
from snff.tasks.console import execute as exec_console
from snff.tasks.ifconfig import execute as exec_ifconfig


__tasks = []
__tasks.append(exec_console)
__tasks.append(exec_environment)
__tasks.append(exec_ifconfig)


def execute() -> None:
    for task in __tasks:
        task()
