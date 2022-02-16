from tkinter import *
from tkinter.ttk import Combobox

from individual_generator import initialize_child_individual

def combobox_factory(label_text, options_list, row,container):
    # Seleccionar nivel (inicial, primaria y secundaria)
    select_codigo_modular_label = Label(container, text=label_text, font=("Lato", 18),
                                        bg="#D1F2F2",
                                        fg="black", padx=20)
    select_codigo_modular_label.grid(row=row, column=0, columnspan=4, sticky=NW)

    # create a combobox
    selected_nivel_type = StringVar()
    # Llenando los valores de los documentos
    niveles_combobox = Combobox(container, textvariable=selected_nivel_type, width=40)
    nivel_list = options_list
    niveles_combobox['values'] = nivel_list
    niveles_combobox['state'] = 'readonly'
    niveles_combobox.set(nivel_list[0])
    niveles_combobox.grid(row=row, column=3, columnspan=3, sticky=NW)


def constancia_vacante_widgets_factory(child):
    # Quitar, el TK() cuándo terminemos de probar
    child = Tk()
    initialize_child_individual(child)


    combobox_factory(label_text="1. Seleccione el nivel:", options_list=['inicial', 'primario','secundario'], row=4, container=child)

    combobox_factory(label_text="2. Seleccione el código modular:", options_list=['0872010','0872184', '1240993', '1542471', '1542489'], row=5,
                     container=child)

    combobox_factory(label_text="3. Seleccione el grado:", options_list=['0872010','0872184', '1240993', '1542471', '1542489'], row=5,
                     container=child)







    # Quitar, el child.mainloop() cuándo terminemos de probar
    child.mainloop()


if __name__ == '__main__':
    constancia_vacante_widgets_factory("child")

