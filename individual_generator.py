# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# initiallize a Tkinter root object
from functions import *

# index window
#child = Tk()
def initialize_child_individual(child, document_type):
    child.title("Generador individual: ")
    child.geometry('+%d+%d' % (350, 10))  # place GUI at x=350, y=10
    child.resizable(False, False)

    # header area - logo & browse button
    header = Frame(child, width=1440, height=180, bg="#00A6FF")
    header.grid(columnspan=7, rowspan=2, row=0)

    # main content area - text and image extraction
    main_content = Frame(child, width=1440, height=700, bg="#D1F2F2")
    main_content.grid(columnspan=7, rowspan=10, row=2)

    #display_logo('resources/insignia.png', row=0, column=0, factor=5.5, padx=20, pady=20, container=child)
    header_title = Label(child, text=f"Generador de documentos - {document_type}", font=("Lato", 25), bg="#00A6FF", fg="white", pady=40,
                         padx=20)
    header_title.grid(row=0, column=4, columnspan=3, )



    # Recordar quitar esto cuándoo se termine de probar
    #child.mainloop()


# class generador:
#    def generar_vacantes(self):

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
