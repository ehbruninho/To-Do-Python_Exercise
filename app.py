from view.menu import menu
from model.storage import *

def main():
    if exist_archive():
        dict_task = convert_json_obj()
    else:
        dict_task = {}
    menu(dict_task)

if __name__ == "__main__":
    main()