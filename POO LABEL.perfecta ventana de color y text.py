import tkinter as tk
ventana= tk.Tk()
ventana.title("Primer ventana")
ventana.geometry("400x300")

#PARA DARLE COLOR desde la pagina:http://wiki.tcl.tk/16166
ventana.configure(background="olive drab")

etiqueta1=tk.Label(ventana, text="Aquí texto",bg="green", fg="white")

#cuando terminamos de escribir los atributos de la etiqueta se usa unMANEJADOR pack etiqueta1.pack()
etiqueta1.pack(fill=tk.X)  #si quiero q la etiqueta ocupe todo un "renglon completo" le
                           #agrego dentro del () a pack
                           #pack(fill=tk.X)   ...sino lo dejo vacío :  etiqueta1.pack()
#etiqueta1.pack()

#generar otra etiqueta
etiqueta2=tk.Label(ventana, text="Va quedando",bg="dark goldenrod", fg="white")

#Con .pack le podemos dar distancia entre etiqueta y etiqueta usando ademas(padx= y pady=)serian
# los ejes, si a y le pongo 40 la distancia se agranda.
#etiqueta2.pack(padx=20,pady=50) 

#Si quiero agrandar el espacio alrededor de mi mensaje, es decir agrandar el rectangulo o cuadrado,
#puedo hacer lo siguiente en la LINEA ANTERIOR 
etiqueta2.pack(padx=20,pady=50, ipadx=20, ipady=20) 

etiqueta3=tk.Label(ventana, text="Mejor",bg="dark goldenrod", fg="white")


etiqueta3.pack(padx=20,pady=20)

#También puedo enviar a la derecha o izquierda la etiqueta3 por ej

#etiqueta3.pack(side=tk.LEFT)


ventana.mainloop()