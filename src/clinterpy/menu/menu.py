from typing import Callable

from clinterpy.menu.base_menu import BaseMenu


class Menu(BaseMenu):
    def display(self, parent_path: str = "") -> None:
        self.output: str = self.initial_output

        while True:
            print(self._render_menu(parent_path))
            cmd = input(self.prompt)
            if cmd == "q":
                break
            try:
                action = self.actions[cmd]
                if isinstance(action, Menu):
                    action.display(self.path)
                    continue

                # replace with callable()
                if isinstance(action, Callable):
                    result = action()
                    if isinstance(result, Menu):
                        result.display(self.path)

                    elif isinstance(result, str):
                        self.output = result

                else:
                    self.output = action

                if not self.loop:
                    break
                # TODO M: Error on Async Menu

            # TODO finer error or do not crash but use text-error message
            except KeyError:
                self.output = f"'{cmd}' does not specify an action"
