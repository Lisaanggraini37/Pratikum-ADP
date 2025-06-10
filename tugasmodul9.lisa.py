from termcolor import colored, cprint
import time
import os

os.system("cls")

for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 10, "white", "on_blue", end="")
    cprint(" " * 8, "white", "on_white")
for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 1, "white", "on_blue", end="")
    cprint(" " * 1, "white", "on_white", end="")
    cprint(" " * 8, "white", "on_blue", end="")
    cprint(" " * 8, "white", "on_white")
for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 10, "white", "on_blue", end="")
    cprint(" " * 8, "white", "on_white")
for i in range(3):
    cprint(" " * 18, "white", "on_blue", end="")
    cprint(" " * 8, "white", "on_yellow")
for i in range(3):
    cprint(" " * 8, "white", "on_blue", end="")
    cprint(" " * 18, "white", "on_yellow")
for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 10, "white", "on_yellow", end="")
    cprint(" " * 8, "white", "on_white")
for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 8, "white", "on_yellow", end="")
    cprint(" " * 1, "white", "on_white", end="")
    cprint(" " * 1, "white", "on_yellow", end="")
    cprint(" " * 8, "white", "on_white")
for i in range(1):
    cprint(" " * 8, "white", "on_white", end="")
    cprint(" " * 10, "white", "on_yellow", end="")
    cprint(" " * 8, "white", "on_white")

print()
print(colored("       P Y T H O N", "blue", attrs=["bold"]))
time.sleep(1)

print(colored("\nLoading Application...\n", "green"))
time.sleep(1)
for i in range(0, 101, 10):
    bar = colored(" " * (i // 2), "white")
    cprint(f"{bar} {i}%", "white", "on_green")
    time.sleep(0.5)
    
time.sleep(1)
os.system("cls")

print()
print(colored("                        W E L C O M E ", "green", attrs=["bold"]))
print(colored("         You've successfully entered the PYTHON App!", "cyan"))
print(colored("Python App is now active – Let's start your coding adventure!", "yellow", attrs=["underline"]))
print()

