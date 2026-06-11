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
        # TODO mutable default argument
        action_string: list[str] | None = None,
    ):
        self.loop: bool = loop
        self.initial_output: str = initial_output
        self.actions: dict[str, Callable[[], str | Self] | Self] = {
            s[0]: actions[s] for s in actions
        }
        # TODO auto-collision detection, quit collision detection
        self.prompt: str = (
            ("(q)uit, " + ", ".join(f"({s[0]}){s[1:]}" for s in actions) + ": ")
            if action_string is None
            else "(q)uit, "
            + ", ".join(f"({s[0]}){s[1:]}" for s in action_string)
            + ": "
        )
        self.path: str = name
        self.output: str = self.initial_output

    # TODO optionify (bad when nested :()
    # - inject from above? when not specified otherwise
    def _render_menu(self, parent_path: str) -> str:
        utils.clear_screen()
        screen: str = "-" * 8 + "\n"
        screen += self.output + "\n"
        screen += ("-" * 8) + "\n"
        screen += (parent_path + " > " if parent_path else "") + self.path + "\n"

        self.output = ""

        return screen
