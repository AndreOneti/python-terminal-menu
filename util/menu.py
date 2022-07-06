#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from typing import Callable, Dict
from util.exceptions import BackException
from simple_term_menu import TerminalMenu


class Menu(TerminalMenu):
    def __init__(self, title: str, menu_entries: Dict[str, Callable] = {}, **kwargs) -> None:
        self.selected_entry = ""
        self.selected_index = 0
        self.menu_entries = [app for app in menu_entries]
        self.switcher = menu_entries

        self.menu_highlight_style = ("fg_cyan", "bold")
        self.menu_cursor_style = ("fg_red", "bold")
        self.title = f"  {title.strip()}\n"
        self.cycle_cursor = True
        self.clear_screen = True
        self.menu_cursor = "> "

        self.menu_entries.append("Quit")
        self.switcher.update({"Quit": lambda: quit(0)})

        super().__init__(
            title=self.title,
            menu_cursor=self.menu_cursor,
            menu_entries=self.menu_entries,
            cycle_cursor=self.cycle_cursor,
            clear_screen=self.clear_screen,
            menu_cursor_style=self.menu_cursor_style,
            menu_highlight_style=self.menu_highlight_style,
            **kwargs
        )

    def show(self) -> None:
        while True:
            try:
                self.selected_index = super().show()
                self.selected_entry = self.menu_entries[self.selected_index]
                self.switcher.get(self.selected_entry, self.error)()
            except BackException:
                pass
            except Exception as e:
                break

    def error(self) -> None:
        print("Error: selected item not found")
        sleep(2)


class MenuItem(TerminalMenu):
    def __init__(self, title: str, menu_entries: Dict[str, Callable] = {}, **kwargs) -> None:
        self.selected_entry = ""
        self.selected_index = 0
        self.menu_entries = [app for app in menu_entries]
        self.switcher = menu_entries

        self.menu_highlight_style = ("fg_cyan", "bold")
        self.menu_cursor_style = ("fg_red", "bold")
        self.title = f"  {title.strip()}\n"
        self.cycle_cursor = True
        self.clear_screen = True
        self.menu_cursor = "> "

        self.menu_entries.append("Back")
        self.switcher.update({"Back": self.back})

        super().__init__(
            title=self.title,
            menu_cursor=self.menu_cursor,
            menu_entries=self.menu_entries,
            cycle_cursor=self.cycle_cursor,
            clear_screen=self.clear_screen,
            menu_cursor_style=self.menu_cursor_style,
            menu_highlight_style=self.menu_highlight_style,
            **kwargs
        )

    def show(self) -> None:
        while True:
            try:
                self.selected_index = super().show()
                self.selected_entry = self.menu_entries[self.selected_index]
                self.switcher.get(self.selected_entry, self.error)()
            except BackException as e:
                break
            except Exception as e:
                raise e

    def error(self) -> None:
        print("Error: selected item not found")
        sleep(2)

    def back(self) -> None:
        raise BackException()
