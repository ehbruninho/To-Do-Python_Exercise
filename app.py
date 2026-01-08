from view.menu import menu
<<<<<<< HEAD
from model.storage import *

def main():
    if exist_archive():
        dict_task = convert_json_obj()
    else:
        dict_task = {}
=======

def main():
    dict_task = {}
>>>>>>> 849d99c37d4b86a35e2a809d9ea46aa331779006
    menu(dict_task)

if __name__ == "__main__":
    main()