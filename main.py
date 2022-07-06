#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from util.menu import Menu, MenuItem


def sleeping():
    while True:
        time = input("Enter with time to sleep: ")
        try:
            time = float(time)
            break
        except:
            print("Please enter with only numbers")

    print("Sleeping now ...")
    sleep(time)
    print("Waking up now ...")
    sleep(.5)


def print_hello_world():
    print("Hello World..")
    sleep(2)


def main():
    hello_world = MenuItem(
        title="Hello World",
        menu_entries={
            "Print Hello World!": print_hello_world
        }
    )

    menu_lvl_2 = MenuItem(
        title="2º menu level",
        menu_entries={
            "Print Hello World!": print_hello_world
        }
    )

    menu_lvl_1 = MenuItem(
        title="1º menu level",
        menu_entries={
            "2º menu level": menu_lvl_2.show
        }
    )

    menu = Menu(
        title="Main menu",
        menu_entries={
            "sleeping X seconds":  sleeping,
            "Hello World": hello_world.show,
            "Menu levels": menu_lvl_1.show
        }
    )

    menu.show()


if __name__ == "__main__":
    main()
