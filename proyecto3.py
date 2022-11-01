from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from io import open

#Variables de control
ubi = "" #Variable para verificar archivo
modif = "" #Variable para verificar borrado

#Funciones del Menu
	#Archivo
def nv():
	if(data.edit_modified() == 0):
		data.delete(1.0,END)
	elif(data.edit_modified() == 1):
		recuadro = mb.askquestion("Guardar", "¿Quiere guardar el archivo?")
		if(recuadro == 'yes'):
			gd() #Verificar que no guarde si regresa cancelar BORRAR
			if(modif != None):
				data.delete(1.0,END)
				data.edit_modified(False)
		else:
			data.delete(1.0,END)
			data.edit_modified(False)
		
def abr():
	nv()
	global ubi
	try:
		ubi = fd.askopenfilename(title="Abrir",filetypes = (("Fichero texto",".txt"),("Archivos Python",".py"),("Archivos Python",".pyw"),("Archivos C",".c"),("Archivos Cplusplus",".cpp"),("Todos los ficheros",".*")))		
	except TclError:
		mb.showwarning("Error", "Ocurrio un error y no se puede abrir el archivo")
	if(ubi != ""):
		archivo = open(ubi, "r+")
		contenido = archivo.read()
		data.delete(1.0,END)
		data.insert(INSERT, contenido)
		archivo.close()
		data.edit_modified(False)

def gd():
	global ubi
	if(data.edit_modified() == 0):
		mb.showinfo("Información", "Su información esta guardada.")
	elif(data.edit_modified() == 1):
		if(ubi != ""):
			contenido = data.get(1.0,END)
			arch = open(ubi, "w+")
			arch.write(contenido)
			arch.close()
			data.edit_modified(False)
			data.edit_reset()
		elif(ubi == ""):
			gdc()
			
def gdc():
	archivo = fd.asksaveasfile(title="Guardar como",mode="w+",defaultextension=".py",filetypes = (("Fichero texto",".txt"),("Archivos Python",".py"),("Archivos Python",".pyw"),("Archivos C",".c"),("Archivos Cplusplus",".cpp"),("Todos los ficheros",".*")))
	global modif
	modif = archivo
	if archivo is not None:
		contenido = data.get(1.0,END)
		archivo.write(contenido)
		archivo.close()
	
	#Editar
def deshacer():
	data.event_generate("<<Undo>>")
def rehacer():
	data.event_generate("<<Redo>>")
def cortar():
	data.event_generate("<<Cut>>")	
def copiar():
	data.event_generate("<<Copy>>")	
def pegar():
	data.event_generate("<<Paste>>")	
	
	#Ayuda
def Datos():
    
	vdatos = Toplevel(raiz)
	vdatos.geometry("360x130+460+450")
    

	Label(vdatos,text="Proyecto III Interfaz grafica").pack()
	Label(vdatos,text="Grupo 7").pack()
	Label(vdatos,text="Carnet: 7690-22-18420 Crosvy Culajay").pack()
	Label(vdatos,text="Carnet: 7690-22-3891 Kevin Cos").pack()
	Label(vdatos,text="Carnet: 7690-22-14922 Ruth Damian").pack()
	Label(vdatos,text="Carnet: 7690-22-17518 Jose Samayoa").pack()
    
 
#Manejar cuando se cierra el programa
def capp():
	if(data.edit_modified() != 0):
		r = mb.askquestion("Guardar", "¿Quiere guardar el archivo antes de salir?")
		if(r == 'yes'):
			gd() #Verificar que no guarde si regresa cancelar BORRAR
			if(modif != None):
				raiz.destroy()
		else:
			raiz.destroy()
	else:
		raiz.destroy()
	

raiz = Tk()
raiz.geometry("800x500+250+250") 
raiz.config(bg="black")
raiz.title("Proyecto III Interfaz grafica")
raiz.iconbitmap("LOGO.ico")#Logo de la ventana
raiz.resizable(0,0)
raiz.protocol("WM_DELETE_WINDOW", capp)
raiz.config(bd=10)#grosor de borde
raiz.config(relief="groove")#tipo de borde
raiz.config(cursor="pirate")

#scrollbar
barra = Scrollbar(raiz)
barra.pack( side = RIGHT, fill=Y )

#Creamos el Menu
menubar = Menu(raiz)

#Agregamos el Menu a la Raíz
raiz.config(menu=menubar)

#Creamos los submenus
archivo = Menu(menubar, tearoff=0) #tearoff=0 quitar opcion default
	#Agregamos los comandos al submenu Archivo
archivo.add_command(label="Nuevo", command=nv)
archivo.add_command(label="Abrir", command=abr)
archivo.add_command(label="Guardar", command=gd)
archivo.add_command(label="Guardar como", command=gdc)
archivo.add_separator()
archivo.add_command(label="Cerrar", command=raiz.quit)
	#Agregamos los comandos al submenu Editar
editar = Menu(menubar, tearoff=0)
editar.add_command(label="Deshacer", command=deshacer)
editar.add_command(label="Rehacer", command=rehacer)
editar.add_command(label="Cortar", command=cortar)
editar.add_command(label="Copiar", command=copiar)
editar.add_command(label="Pegar", command=pegar)
	#Agregamos los comandos al submenu Editar
ayuda = Menu(menubar,tearoff=0)
ayuda.add_command(label="Acerca de", command=Datos)

#Agregamos los submenus al Menu
menubar.add_cascade(label="Archivo", menu=archivo)
menubar.add_cascade(label="Editar", menu=editar)
menubar.add_cascade(label="Ayuda", menu=ayuda)

#Texto
data = Text(raiz)
data.config(cursor="hand2")
data.pack(fill=BOTH, expand=1)
data.config(font=("arial black",14,),bg="white",maxundo=20, yscrollcommand = barra.set)
barra.config( command = data.yview )

raiz.mainloop()