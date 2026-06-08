from abc import ABC
from typing import Callable, Self

import clinterpy.menu.utils as utils


class BaseMenu(ABC):
    def __init__(
        self,
        name: str,
        # TODO check best typing solution
        actions: dict[str, Callable[[], str | Self] | Self],
        loop: bool = True,
        initial_output: str = "",
        action_string: list[str] = [],
    ):
        self.loop: bool = loop
        self.initial_output: str = initial_output
        self.actions: dict[str, Callable[[], str | Self] | Self] = {
            s[0]: actions[s] for s in actions
        }
        # TODO auto-collision detection
        self.prompt: str = (
            ("(q)uit, " + ", ".join(f"({s[0]}){s[1:]}" for s in actions) + ": ")
            if action_string == []
            else "(q)uit, "
            + ", ".join(f"({s[0]}){s[1:]}" for s in action_string)
            + ": "
        )
        self.path: str = name
        self.output: str = self.initial_output

    def _set_path(self, path: str):
        self.path = path + " > " + self.path

    # TODO optionify
    def _render_menu(self) -> str:
        utils.clear_screen()
        screen = "-" * 8 + "\n"
        screen += self.output + "\n"
        screen += ("-" * 8) + "\n"
        screen += self.path + "\n"

        self.output = ""

        return screen
