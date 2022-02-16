import random
import time
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import os

import folder as folder
from docxtpl import DocxTemplate

from individual_generator import initialize_child_individual
import pandas as pd
import comtypes.client

def combobox_factory(label_text, options_list, container, row, column=0, flexible=False, column_widget=0):
    if not flexible:
        column_widget = column + 2

    combobox_label = Label(container, text=label_text, font=("Lato", 14),
                           bg="#D1F2F2",
                           fg="black", padx=20)
    combobox_label.grid(row=row, column=column, columnspan=3, sticky=NW)

    # create a combobox
    selected_combobox = StringVar()
    combobox = Combobox(container, textvariable=selected_combobox, width=40)
    combobox['values'] = options_list
    combobox['state'] = 'readonly'
    combobox.set(options_list[0])
    combobox.grid(row=row, column=column_widget, columnspan=2, sticky=NW)
    return selected_combobox


def text_input_factory(label_text, container, row, column=0, flexible=False, column_widget=0):
    if not flexible:
        column_widget = column + 2
    input_text_label = Label(container, text=label_text, font=("Lato", 14),
                             bg="#D1F2F2",
                             fg="black", padx=20)
    input_text_label.grid(row=row, column=column, columnspan=2, sticky=NW)

    typed_text = StringVar()
    input_text = Entry(container, textvariable=typed_text, width=40)
    input_text.grid(row=row, column=column_widget, columnspan=2, sticky=NW)
    return typed_text


def update_path(path_selected, parent):
    folder_selected = filedialog.askdirectory(parent=parent,title="Seleccionar ruta de destino")
    path_selected.set(folder_selected)


def update_file_path(selected_file_path, parent):
    file_selected = filedialog.askopenfilename(filetypes=(("Archivos csv", "*.csv"), ("All files", "*.*")),parent=parent, title="Seleccionar archivo de origen")
    selected_file_path.set(file_selected)

def convert_word_to_pdf(input_file_path,output_file_path):
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    doc = word.Documents.Open(input_file_path)
    doc.SaveAs(output_file_path, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def set_origin_path_factory(container, row, column, default_path, label_text="Seleccione el archivo CSV:", ):
    input_text_label = Label(container, text=label_text, font=("Lato", 14),
                             bg="#D1F2F2",
                             fg="black", padx=20)
    input_text_label.grid(row=row, column=column, columnspan=3, sticky=NW)

    file_selected = StringVar()
    file_selected.set(default_path)
    input_path = Entry(container, textvariable=file_selected, width=40, state="disabled")
    input_path.grid(row=row + 1, column=column+1, columnspan=3, rowspan=2, sticky=NW)

    # Update dest path file button
    update_path_button = Button(container, text="Seleccionar archivo",
                                command=lambda: update_file_path(file_selected,parent=container),
                                font=("Lato", 14),
                                height=1, width=15, bg="#00A6FF", fg="white")
    update_path_button.grid(row=row + 1, column=column, sticky=N)
    return file_selected


def set_dest_path_factory(container, row, column, default_path,
                          label_text="Seleccione la ruta de destino para guardar:", ):
    input_text_label = Label(container, text=label_text, font=("Lato", 14),
                             bg="#D1F2F2",
                             fg="black", padx=20)
    input_text_label.grid(row=row, column=column, columnspan=3, sticky=NW)

    if not (os.path.exists(default_path)):
        os.makedirs(default_path)
        os.makedirs(default_path+"/word")
        os.makedirs(default_path+"/pdf")

    path_selected = StringVar()
    path_selected.set(default_path)
    input_path = Entry(container, textvariable=path_selected, width=40, state="disabled")
    input_path.grid(row=row + 1, column=column + 1, columnspan=3, rowspan=2, sticky=NW)

    # Update dest path file button
    update_path_button = Button(container, text="Actualizar destino",
                                command=lambda: update_path(path_selected, parent=container),
                                font=("Lato", 14),
                                height=1, width=15, bg="#00A6FF", fg="white")
    update_path_button.grid(row=row + 1, column=column, sticky=N)
    return path_selected


def constancia_vacante_widgets_factory_individual(child, document_type, generation_type):
    # Quitar, el TK() cuándo terminemos de probar
    # child = Tk()
    initialize_child_individual(child, document_type)

    generation_type_label = Label(child, text=f"Generando documentos bajo modalidad {generation_type}",
                                  font=("Lato", 14),
                                  bg="#D1F2F2",
                                  fg="black", padx=20)
    generation_type_label.grid(row=3, column=0, columnspan=3, sticky=NW)

    nivel = combobox_factory(label_text="1. Seleccione el nivel:", options_list=['inicial', 'primario', 'secundario'],
                             row=4, container=child)

    codigo_modular = combobox_factory(label_text="2. Seleccione el código modular:",
                                      options_list=['0872010', '0872184', '1240993', '1542471', '1542489'], row=5,
                                      container=child)

    grado = combobox_factory(label_text="3. Seleccione el grado:",
                             options_list=['inicial de 3 años', 'inicial de 4 años', 'inicial de 5 años',
                                           'primero de primaria', 'segundo de primaria', 'tercero de primaria',
                                           'cuarto de primaria', 'quinto de primaria', 'sexto de primaria',
                                           'primero de secundaria', 'segundo de secundaria', 'tercero de secundaria',
                                           'cuarto de secundaria', 'quinto de secundaria'], row=6,
                             container=child)

    pronombre = combobox_factory(label_text="4. Seleccione el pronombre:",
                                 options_list=['el', 'la'], row=7,
                                 container=child)

    apellidos = text_input_factory(label_text="5. Ingresar los apellidos:", row=8, container=child)

    nombres = text_input_factory(label_text="6. Ingresar los nombres:", row=9, container=child)

    institucion_anterior = text_input_factory(label_text="7. Ingresar la institución anterior:", row=10,
                                              container=child)

    dni = text_input_factory(label_text="8. Ingresar el DNI:", row=4, container=child, column=4, flexible=True,
                             column_widget=5)

    dest_path = set_dest_path_factory(column=4, row=5, default_path=os.path.expanduser(
        f'~/Documents/GeneratedDocuments/{document_type}'), container=child)

    button_state = StringVar()
    button_state.set("Generar")

    # Generate button
    generate_button = Button(child, textvariable=button_state,
                             command=lambda: make_word_indvidual(
                                 datos_plantilla={
                                     "NIVEL": nivel.get(),
                                     "CODIGO_MODULAR": codigo_modular.get(),
                                     "GRADO_ESCOLAR": grado.get(),
                                     "APELLIDOS": apellidos.get(),
                                     "NOMBRES": nombres.get(),
                                     "DNI": dni.get(),
                                     "PRONOMBRE": pronombre.get(),
                                     "INSTITUCION_ANTERIOR": institucion_anterior.get()
                                 },
                                 dest_path=dest_path.get(),
                                 button_state=button_state
                             ),
                             font=("Lato", 14),
                             height=1, width=15, bg="#00A6FF", fg="white")
    generate_button.grid(row=11, column=4, sticky=N)

    # Quitar, el child.mainloop() cuándo terminemos de probar
    # child.mainloop()


def constancia_vacante_widgets_factory_bloque(child, document_type, generation_type):
    # Quitar, el TK() cuándo terminemos de probar
    # child = Tk()
    initialize_child_individual(child, document_type)

    generation_type_label = Label(child, text=f"Generando documentos bajo modalidad {generation_type}",
                                  font=("Lato", 14),
                                  bg="#D1F2F2",
                                  fg="black", padx=20)
    generation_type_label.grid(row=3, column=0, columnspan=3, sticky=NW)

    selected_file_path = set_origin_path_factory(container=child, default_path=None, row=4, column=0,label_text="1. Seleccione el archivo CSV:")

    dest_path = set_dest_path_factory(column=0, row=7, default_path=os.path.expanduser(
        f'~/Documents/GeneratedDocuments/{document_type}'), container=child, label_text="2. Seleccione la ruta de destino para guardar:")

    button_state = StringVar()
    button_state.set("Generar")
    # Generate button
    generate_button = Button(child, textvariable=button_state,
                             command=lambda: make_word_bloque(selected_file_path.get(), dest_path.get(), button_state),
                             font=("Lato", 14),
                             height=1, width=15, bg="#00A6FF", fg="white")
    generate_button.grid(row=11, column=4, sticky=N)

    # Quitar, el child.mainloop() cuándo terminemos de probar
    # child.mainloop()


def make_word_indvidual(datos_plantilla, dest_path, button_state, alert=True):
    button_state.set("Generando")
    # Switch dependiendo del tipo de documento (vacante, no adeudo, etc.)
    if datos_plantilla["INSTITUCION_ANTERIOR"].upper().startswith("XX"):
        if datos_plantilla["DNI"].upper().startswith("XX"):
            tpl = DocxTemplate("templates/constancia-vacante-simple-plantilla.docx")
        else:
            tpl = DocxTemplate("templates/constancia-vacante-simple-DNI-plantilla.docx")
    else:
        tpl = DocxTemplate("templates/constancia-vacante-plantilla.docx")
    codigo_modular = datos_plantilla["CODIGO_MODULAR"]
    datos_plantilla["CODIGO_MODULAR"] = f'{codigo_modular:07}'
    tpl.render(datos_plantilla)
    # Debe pasar también la ruta de descarga, por defecto debe ser la misma que la de dónde está el programa
    # folder_selected = filedialog.askdirectory()
    output_path_word = os.path.join(dest_path,"word",
                              f"Constancia de vacante - {datos_plantilla['APELLIDOS']}, {datos_plantilla['NOMBRES']}.docx")
    output_path_pdf = os.path.join(dest_path,"pdf",
                                    f"Constancia de vacante - {datos_plantilla['APELLIDOS']}, {datos_plantilla['NOMBRES']}.pdf")
    tpl.save(output_path_word)
    # Esperar a que se genere el word primero, luego generar el PDF
    #time.sleep(random.randint(5, 10))
    convert_word_to_pdf(output_path_word, output_path_pdf)
    if alert:
        messagebox.showinfo("Documento generado con éxito", f"Se guardó el documento en: {output_path_word}")
        button_state.set("Generar")


def make_word_bloque(selected_file_path, dest_path, button_state):
    button_state.set("Generando")
    df = pd.read_csv(selected_file_path, encoding='utf8')
    registros = df.to_dict(orient='records')
    for registro in registros:
        make_word_indvidual(registro, dest_path, button_state, alert=False)
    messagebox.showinfo("Documentos generados con éxito", f"Se guardaron en: {dest_path}")
    button_state.set("Generar")


if __name__ == '__main__':
    constancia_vacante_widgets_factory_individual("child")
