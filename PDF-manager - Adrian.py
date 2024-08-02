import customtkinter as tk
import os
import pypdf
from pathlib import Path
from tkinter import filedialog

app = tk.CTk()
app.geometry("200x350")
app.resizable(False,False)
app.title("PDF-MANAGER")

def select(certain = 0):
    file = filedialog.askopenfile().name
    if certain != 0:
        optional = filedialog.askopenfile().name
    else:
        optional = ''

    def directory(make):
        match make:
            case 0:
                if not os.path.exists('text'):
                    os.makedirs('text')
            case 1:
                if not os.path.exists('images'):
                    os.makedirs('images')
            case 2:
                if not os.path.exists('paginas'):
                    os.makedirs('paginas')

    def rotate_opt():
        rot = tk.CTkToplevel(app)
        rot.geometry("200x100")
        rot.resizable(False,False)
        rot.title("PDF-MANAGER")
        tk.CTkButton(rot,text='90',command=lambda:rotate(90,rot)).place(relx=0.5,rely=(0.2),anchor='center')
        tk.CTkButton(rot,text='180',command=lambda:rotate(180,rot)).place(relx=0.5,rely=(0.5),anchor='center')
        tk.CTkButton(rot,text='270',command=lambda:rotate(270,rot)).place(relx=0.5,rely=(0.8),anchor='center')

    def rotate(degrees,rot):
        rot.destroy()
        arquive ,arq_final, null = program()
        for page in arquive.pages:
            page.rotate(degrees)
            arq_final.add_page(page)

        with Path(f'Rotated.pdf').open(mode='wb') as arquivo_final:
            arq_final.write(arquivo_final)
        errorcheck(0)

    def separate():
        arquive ,arq_final, null = program()
        directory(2)
        re = 1

        for page in arquive.pages:
            arq_final = pypdf.PdfWriter()
            arq_final.add_page(page)
        
            with Path(f'paginas/Page test {re}.pdf').open(mode='wb') as final:
                arq_final.write(final)
                re += 1
        errorcheck(0)

    def merge():
        arquive ,arq_final, optional = program()
        arq_join = pypdf.PdfReader(optional.replace('"',''))
        arq_final.append(arquive)
        arq_final.append(arq_join)

        with Path(f'Merged.pdf').open(mode='wb') as arquivo_final:
            arq_final.write(arquivo_final)
        errorcheck(0)

    def extract_text():
        arquive ,arq_final, null = program()
        directory(0)
        for re, page in enumerate(arquive.pages):
            arq_final = page.extract_text().replace('\uf0b7','')
            with open(f'text/Text page {re}.txt','w', encoding='UTF-8') as arquivo_final:
                try:
                    arquivo_final.write(arq_final)
                except:
                    continue
        errorcheck(0)

    def extract_image():
        arquive ,arq_final, null = program() 
        directory(1)
        count = 0
        for i in range(len(arquive.pages)):
            try:
                for image_file_object in arquive.pages[i].images:
                    if 'png' in str(image_file_object.name):
                        with open(f'images/{str(count)} {image_file_object.name}', "wb") as arq_final:
                            arq_final.write(image_file_object.data)
                            count += 1
            except:
                continue
        errorcheck(0)

    def program(optional=optional):
        entry = file
        arquive = pypdf.PdfReader(entry.replace('"',''))
        arq_final = pypdf.PdfWriter()
        return arquive , arq_final, optional

    def errorcheck(error):
        match error:
            case 0:
                tk.CTkLabel(app,text=' '*200).place(relx=0.5,rely=(0.3),anchor='center')
            case 1:
                tk.CTkLabel(app,text='Allowed: .pdf extension').place(relx=0.5,rely=(0.3),anchor='center')

    if file[-3:] == 'pdf':
        tk.CTkButton(app,text='ROTATE',command=rotate_opt).place(relx=0.5,rely=(0.6),anchor='center')
        tk.CTkButton(app,text='SEPARATE',command=separate).place(relx=0.5,rely=(0.7),anchor='center')
        tk.CTkButton(app,text='EXTRACT TEXT',command=extract_text).place(relx=0.5,rely=(0.8),anchor='center')
        tk.CTkButton(app,text='EXTRACT IMAGE',command=extract_image).place(relx=0.5,rely=(0.9),anchor='center')
        
        if optional[-3:] == 'pdf':
            tk.CTkButton(app,text='MERGE',command=merge).place(relx=0.5,rely=(0.5),anchor='center')
    else:
        errorcheck(1)

def double():
    select(1)

entry = tk.CTkButton(app, text="SELECT ONE FILE" ,command=select).place(relx=0.5,rely=(0.1),anchor='center')
optional = tk.CTkButton(app, text="MERGE TWO FILE" ,command=double).place(relx=0.5,rely=(0.2),anchor='center')

app.mainloop()
