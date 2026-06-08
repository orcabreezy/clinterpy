from typing import Callable

from clinterpy.menu.base_menu import BaseMenu


class Menu(BaseMenu):
    def display(self) -> None:
        self.output: str = self.initial_output

        while True:
            print(self._render_menu())
            cmd = input(self.prompt)
            if cmd == "q":
                break
            try:
                action = self.actions[cmd]
                if isinstance(action, Menu):
                    action._set_path(self.path)
                    action.display()
                    continue

                if isinstance(action, Callable):
                    result = action()
                    if isinstance(result, Menu):
                        result._set_path(self.path)
                        result.display()

                    elif isinstance(result, str):
                        self.output = result

                else:
                    self.output = action

                if not self.loop:
                    break
                # TODO M: Error on Async Menu

            except KeyError:
                self.output = f"'{cmd}' does not specify an action"
