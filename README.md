## CENTRO UNIVERSITARIO DE BOCA DEL MONTE
### FACULTAD DE INGENIERIA EN SISTEMAS


## Titulo: **Proyecto 3 Algoritmos**



### Nombres: Crosvy Rolando Culajay Zabala
###          Ruth Estefania Perez Damian 
###          Jose Rodolfo Samayoa Matias
###          Kevin Antulio Poitan Cos
### Sección “A”


***
***
# **`Python Interfaz Grafica`**
    Una de las formas más sencillas que existen en Python para crear interfaces gráficas GUI, es con la ayuda de tkinter.
    Las GUI a menudo usan una forma de programación OO controlada por eventos, el programa responde a eventos, que son acciones que un usuario realiza. Las acciones que realiza el usuario no son otra cosa que botones que son presionados.

# *Ejemplo*

```
from tkinter import *
 
root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
 
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")
     
l = Label(text = "What is 24 * 5 ? ")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 
Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan")
 
Display = Button(root, height = 2,
                 width = 20,
                 text ="Show",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
```

> Tkinter es el paquete más utilizado para crear interfaces gráficas en Python. Es una capa orientada a objetos basada en Tcl (sencillo y versátil lenguaje de programación open-source) y Tk (la herramienta GUI estándar para Tcl).
***
***

## Widgets
A la hora de montar una vista con Tkinter, nos basaremos en widgets jerarquizados, que irán componiendo poco a poco nuestra interfaz. Algunos de los más comunes son:
Tk: es la raíz de la interfaz, donde vamos a colocar el resto de widgets.
Frame: marco que permite agrupar diferentes widgets.
Label: etiqueta estática que permite mostrar texto o imagen.
Entry: etiqueta que permite introducir texto corto (típico de formularios).
Text: campo que permite introducir texto largo (típico para añadir comentarios).
Button: ejecuta una función al ser pulsado.
Menu: clásico menú superior con opciones (Archivo, Editar…).

## Configuración
>Para configurar un widget, simplemente llamamos a .config() y pasamos los argumentos que queramos modificar. Algunas opciones son:

* bg: modifica el color de fondo. Se puede indicar con el color en inglés (incluyendo modificadores, como “darkgreen”) o su código RGB en hexadecimal (“#aaaaaa” para blanco). Ojo: en MacOS no se puede modificar el color de fondo de los botones; aunque indiquemos un nuevo color, se mostrará en blanco. Lo más parecido que podemos hacer es configurar el highlightbackground, que pintará el fondo alrededor del botón del color que indiquemos.
* fg: cambia el color del texto.
* cursor: modifica la forma del cursor. Algunos de los más utilizados son “gumby”, “pencil”, “watch” o “cross”.
* height: altura en líneas del componente.
* width: anchura en caracteres del componente.
* font: nos permite especificar, en una tupla con nombre de la fuente, tamaño y estilo, la fuente a utilizar en el texto del componente. Por ejemplo, Font(“Times New Roman”, 24, “bold underline”).
* bd: modificamos la anchura del borde del widget.
* relief: cambiamos el estilo del borde del componente. Su valor puede ser “flat”, “sunken”, “raised”, “groove”, “solid” o “ridge”.
* state: permite deshabilitar el componente (state=DISABLED); por ejemplo, una Label en la que no se puede escribir o un Button que no se puede clickar.
* padding: espacio en blanco alrededor del widget en cuestión.
* command: de cara a que los botones hagan cosas, podemos indicar qué función ejecutar cuando se haga click en el mismo.



