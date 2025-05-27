import colorama
from colorama import Fore, Back, Style, init, deinit, reinit
import inspect

init()

print("Основні атрибути colorama:")
print(dir(colorama))
print("\n")

print("Fore (кольори тексту):", dir(Fore))
print("Back (кольори фону):", dir(Back))
print("Style (стилі тексту):", dir(Style))
print("\n")

print("Функція init():", inspect.getdoc(init))
print("Функція deinit():", inspect.getdoc(deinit))
print("Функція reinit():", inspect.getdoc(reinit))