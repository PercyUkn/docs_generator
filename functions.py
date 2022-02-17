from tkinter import *
from PIL import Image, ImageTk


# place an image on the grid

from factories import constancia_vacante_widgets_factory_individual, constancia_vacante_widgets_factory_bloque


def display_logo(url, row, column, factor, container, padx=20, pady=40):
    img = Image.open(url)
    img = img.resize((int(img.size[0] / factor), int(img.size[1] / factor)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="#00A6FF",master=container)
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=padx, pady=pady)


def display_icon(url, row, column, stick, funct):
    icon = Image.open(url)
    icon = icon.resize((20, 20))
    icon = ImageTk.PhotoImage(icon)
    icon_label = Button(image=icon, command=funct, width=25, height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=stick)

def generate_child_indvidual(child, document_type, generation_type, function):
    function(child, document_type, generation_type)
    display_logo('resources/insignia.png', row=0, column=0, factor=5.5, padx=20, pady=20, container=child)
    #child.geometry("750x250")
    child.title(f"Generador individual: {document_type} - {generation_type}")

def generate_child_bloque(child, document_type, generation_type, function):
    function(child, document_type, generation_type)
    display_logo('resources/insignia.png', row=0, column=0, factor=5.5, padx=20, pady=20, container=child)
    #child.geometry("750x250")
    child.title(f"Generador en bloque: {document_type} - {generation_type}")

def generate_window(parent, document_type, generation_type):
    # Switch para la función Lambda según el tipo de documento
    child_individual = Toplevel(parent)
    if generation_type.upper() == "INDIVIDUAL":
        generate_child_indvidual(child_individual, document_type, generation_type, function=constancia_vacante_widgets_factory_individual)
    elif generation_type.upper() == "BLOQUE":
        generate_child_bloque(child_individual, document_type, generation_type,
                                 function=constancia_vacante_widgets_factory_bloque)



