# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter.ttk import Combobox

# initiallize a Tkinter root object


# index window
from functions import display_logo, generate_window

root = Tk()
root.title("Generador de documentos")
root.geometry('+%d+%d' % (350, 10))  # place GUI at x=350, y=10
root.resizable(False, False)

# header area - logo & browse button
header = Frame(root, width=1440, height=180, bg="#00A6FF")
header.grid(columnspan=7, rowspan=2, row=0)

# main content area - text and image extraction
main_content = Frame(root, width=1440, height=700, bg="#D1F2F2")
main_content.grid(columnspan=7, rowspan=10, row=2)

display_logo('resources/insignia.png', row=0, column=0, factor=5.5, padx=20, pady=20, container=root)
header_title = Label(root, text="Generador de documentos", font=("Lato", 50), bg="#00A6FF", fg="white", pady=40,
                     padx=20)
header_title.grid(row=0, column=4, columnspan=3, )

# first instruction
document_type_label = Label(root, text="1. Tipo de documento", font=("Lato", 18), bg="#D1F2F2", fg="black", pady=40,
                            padx=20)
document_type_label.grid(row=3, column=0, sticky=S)

select_document_label = Label(root, text="Seleccione el tipo de documento a generar:", font=("Lato", 18), bg="#D1F2F2",
                              fg="black", padx=20)
select_document_label.grid(row=4, column=0, columnspan=4, sticky=N)

# create a combobox
selected_document_type = StringVar()
# Llenando los valores de los documentos
document_types_combobox = Combobox(root, textvariable=selected_document_type, width=40)
document_types_list = ['Constancia de vacante', 'Constancia de no adeudo']
document_types_combobox['values'] = document_types_list
document_types_combobox['state'] = 'readonly'
document_types_combobox.grid(row=4, column=4, columnspan=3, sticky=NW)
document_types_combobox.set(document_types_list[0])

# Second instruction
generation_type_label = Label(root, text="2. Tipo de generación", font=("Lato", 18), bg="#D1F2F2", fg="black", pady=40,
                              padx=20)

# Agrupa a los radio button
selected_generation_type = StringVar()
generation_type_label.grid(row=5, column=0, sticky=S)
generation_type_radio_button_individual = Radiobutton(root, variable=selected_generation_type,
                                                      text="Generación individual", value="Individual", bg="#D1F2F2",
                                                      font=("Lato", 14))
generation_type_radio_button_individual.grid(row=6, column=0, sticky=N)
generation_type_radio_button_bloque = Radiobutton(root, variable=selected_generation_type,
                                                  text="Generación en bloque", value="Bloque", bg="#D1F2F2",
                                                  font=("Lato", 14))
generation_type_radio_button_bloque.grid(row=7, column=0, sticky=N)

# Seleccionando individual por defecto
generation_type_radio_button_individual.select()

# Generate button
generate_button = Button(root, text="Generar", command=lambda: generate_window(root, selected_document_type.get(),
                                                                               selected_generation_type.get()),
                         font=("Lato", 14),
                         height=1, width=15, bg="#00A6FF", fg="white")
generate_button.grid(row=9, column=4, sticky=N)

root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
