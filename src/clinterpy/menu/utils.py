import os


# TODO undeprecate
def clear_screen() -> str:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    return ""
