from tkinter import *
import time
import json
import random
from stage2 import Stage2
from tkinter import messagebox 
import webbrowser


def iniciar(app):
    root.withdraw()
    root.overrideredirect(False)
    root.geometry("1358x730+0+0")
    app = Application(root)
    app.configure(background="white")
    lblPortada.forget()
    app.createWidgets()
    root.deiconify()
    root.state("zoomed")


def pideSalir():
    if (messagebox.askyesno("Finalizar?","¿Querés salir del programa realmente?")):
        root.destroy()

class Application(Frame):
    color="paleGreen2"
    fuente=("Verdana",24)
    fuente_negrita=("Verdana",22,"bold")

    arrastra=False
    fotografia_nro=0
    meGusta_nro=0
    noMeGusta_nro=0
    nombreImagenPNG=""
    leGusta=[]
    noLeGusta=[]

    #print("inicio")
    with open('json.txt', encoding='utf-8') as archivo:
      data = json.load(archivo)
    random.shuffle(data)
    #print("fin")

    def __init__(self,master):
        super(Application, self).__init__(master)
        self.pack(anchor=CENTER,expand=1,fill=BOTH)
        #self.createWidgets()

    def dameNombreImagen(self):
        return "img/Oficios/" + str(self.data[self.fotografia_nro]["id"]) + ".png"

    def dameNombreSmallImagen(self):
        return "img/Oficios/small/" + str(self.data[self.fotografia_nro]["id"]) + ".png"
         
    def my_callback(self,event):
            self.arrastra=True
            self.imagen=PhotoImage(file=self.dameNombreImagen())
            self.small_imagen=PhotoImage(file=self.dameNombreSmallImagen())
            
            if (event.y<=520):
                tope_y=event.y
            else:
                tope_y=520
            
            self.my_img=self.my_c.create_image(event.x,tope_y,image=self.imagen,tag="oficio")
            self.config(cursor=self.puntero_agarra) 

            if (event.x>=1000 and event.x<=1300 and event.y>=50 and event.y<=300):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(event.x,tope_y,image=self.small_imagen,tag="small_oficio")
            elif (event.x>=1000 and event.x<=1300 and event.y>=350 and event.y<=600):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(event.x,tope_y,image=self.small_imagen,tag="small_oficio")

    
    def solto(self,event):
        self.config(cursor=self.puntero_suelta)
        if (self.arrastra):
            self.arrastra=False
            if (event.x>=1000 and event.x<=1300 and event.y>=50 and event.y<=300):
                self.leGusta.append(self.data[self.fotografia_nro])
                self.fotografia_nro=self.fotografia_nro +1
                self.meGusta_nro=self.meGusta_nro +1
                self.my_c.delete("small_oficio")
            if (event.x>=1000 and event.x<=1300 and event.y>=350 and event.y<=600):
                self.noLeGusta.append(self.data[self.fotografia_nro])
                self.fotografia_nro=self.fotografia_nro +1
                self.noMeGusta_nro=self.noMeGusta_nro + 1
                self.my_c.delete("small_oficio")
            if (len(self.data)==self.fotografia_nro):
                #Fin  - repinto los totales de 'Me Gusta'
                self.meGusta=self.my_c.create_rectangle(1000,50,1300,300,fill='green', outline='black')
                self.noMeGusta=self.my_c.create_rectangle(1000,350,1300,600,fill='red', outline='black')
                self.imagenGusta=PhotoImage(file="img/gusta.png")
                self.my_imgGusta=self.my_c.create_image(1150,120,image=self.imagenGusta)
                self.imagenNoGusta=PhotoImage(file="img/nogusta.png")
                self.my_imgNoGusta=self.my_c.create_image(1150,450,image=self.imagenNoGusta)
                self.my_c.create_text(1150,270,font=self.fuente,text="Me Gusta (" + str(self.meGusta_nro) +")")
                self.my_c.create_text(1150,570,font=self.fuente,text="No Me Gusta ("+ str(self.noMeGusta_nro)+")")
                self.Final()
            else:    
                self.createWidgets()

    def masInfo(self):
            TInfo=Text(self.my_c,font=self.fuente_negrita,wrap=WORD,height=7,width=55,bg="lightyellow")
            TInfo.place(x=50,y=100)
            TInfo.insert(INSERT,"Foto: ","bold")
            TInfo.insert(INSERT,self.data[self.fotografia_nro]["nombre_profesion"],"nombreDelOficio")
            TInfo.insert(INSERT,"\nTipo: ","bold")
            TInfo.insert(INSERT,self.data[self.fotografia_nro]["area"])
            TInfo.insert(INSERT,"\nDescripción: ","bold")
            TInfo.insert(INSERT,self.data[self.fotografia_nro]["descripcion"])
            TInfo.tag_config("bold", font=self.fuente_negrita, foreground="blue")
            TInfo.tag_config("nombreDelOficio", font=self.fuente_negrita, foreground="red")
            self.after(5000,lambda: TInfo.destroy())

    def createWidgets(self):
        self.puntero_agarra = "@punteros/closedhand_100189.cur"                
        self.puntero_suelta = "@punteros/openhand_100161.cur"
        self.puntero_dedito = "@punteros/pointinghand_100160.cur"
        self.puntero_reloj = "@punteros/clock_history_icon_160238.cur" 
        root['cursor'] =  self.puntero_suelta , self.puntero_dedito,self.puntero_agarra, self.puntero_reloj 

        self.my_c=Canvas(self,width=2000,height=1500,bg=self.color)
        self.my_c.place(x=0,y=0)

        self.imagenAbout=PhotoImage(file="img/logo64.png")
        self.my_imgAbout=Label(self.my_c,image=self.imagenAbout,cursor="hand2")
        self.my_imgAbout.place(x=50,y=580)
        self.my_imgAbout.bind('<Button-1>',lambda event: webbrowser.open_new("https://github.com/pmileti/DarPye"))

        lblAbout = Label(self.my_c, text="Por Pablo Mileti, año 2023.",bg=self.color, fg="blue", cursor="hand2")
        lblAbout.place(x=20,y=650)
        lblAbout.bind("<Button-1>", lambda event: webbrowser.open_new("http://mileti.com.ar"))


        self.imagenCentro=PhotoImage(file="img/centro.png")
        self.my_imgCentro=self.my_c.create_image(490,300,image=self.imagenCentro)

        self.meGusta=self.my_c.create_rectangle(1000,50,1300,300,fill='green', outline='black')
        self.noMeGusta=self.my_c.create_rectangle(1000,350,1300,600,fill='red', outline='black')

        self.imagenGusta=PhotoImage(file="img/gusta.png")
        self.my_imgGusta=self.my_c.create_image(1150,120,image=self.imagenGusta)

        self.imagenNoGusta=PhotoImage(file="img/nogusta.png")
        self.my_imgNoGusta=self.my_c.create_image(1150,450,image=self.imagenNoGusta)

        self.my_c.create_text(1150,270,font=self.fuente,text="Me Gusta (" + str(self.meGusta_nro) +")")
        self.my_c.create_text(1150,570,font=self.fuente,text="No Me Gusta ("+ str(self.noMeGusta_nro)+")")
        
        l1=Label(self.my_c,text="  Arrastrá las fotos según tus intereses. Si no comprendés la foto presiona el botón   ",bg=self.color,font=self.fuente_negrita,fg="navy")
        l1.place(x=2,y=690) 

        b1=Button(self.my_c,text="¿Qué es eso?",command=self.masInfo,font=self.fuente,bg="lightblue",cursor=self.puntero_dedito)
        b1.place(x=400,y=570)
        
        self.imagen=PhotoImage(file=self.dameNombreImagen())
        self.my_img=self.my_c.create_image(500,300,image=self.imagen,tag="oficio")
     
        self.my_c.bind('<B1-Motion>',self.my_callback)
        self.my_c.bind('<ButtonRelease-1>',self.solto)

    def Final(self):
            self.config(cursor=self.puntero_reloj)
            TInfo=Text(self.my_c,font=self.fuente_negrita,wrap=WORD,height=3,width=60,bg="khaki",cursor=self.puntero_reloj)
            TInfo.place(x=80,y=300)
            if self.meGusta_nro>1:
                TInfo.insert("1.0","\n\tMuy bien! Pasamos a la siguiente etapa con " + str(self.meGusta_nro) + " fotos!")
            elif self.meGusta_nro==1:
                TInfo.insert("1.0","\n\tMuy bien! Pasamos a la siguiente etapa con " + str(self.meGusta_nro) + " sola foto =(")
            else:    
                TInfo.insert("1.0","\n\tGAME OVER - Ninguna foto te gusto =(")
                self.after(3000,lambda:root.destroy())

            self.after(3000,lambda: self.createWidgetsFinal())

    
    def createWidgetsFinal(self):
        self.config(cursor="left_ptr")
        pantalla2=Stage2(Frame, self.leGusta)
        pantalla2.mostrar()
        self.after(2000,lambda: root.withdraw())




if __name__ == '__main__':
    root = Tk()
    root.title("Dar Pye - Proyectando tu futuro")
    #app = Application(root)
    #app.configure(background="white")
    #root.geometry("1358x730+0+0")
    root.geometry("705x700+350+20")
    root.resizable(False,False)
    #root.state("zoomed")
    root.overrideredirect(True)
    root.protocol("WM_DELETE_WINDOW",pideSalir)
    icono_chico = PhotoImage(file="img/logo16.png")
    icono_grande = PhotoImage(file="img/logo32.png")
    root.iconphoto(False, icono_grande, icono_chico)
    imagenPortada=PhotoImage(file="img/portada.png")
    lblPortada=Label(root,image=imagenPortada)
    lblPortada.place(x=0,y=0)
    lblPortada.image=imagenPortada
    app=None
    root.after(3000,lambda: iniciar(app))

    root.mainloop()
