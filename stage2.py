from tkinter import *
import time
from stage3 import Stage3
from tkinter import messagebox 


class Stage2(Frame):
    def __init__(self, Frame, leGusta):
        self.color="paleGreen3"
        self.fuente=("Verdana",22)
        self.fuente_negrita=("Verdana",22,"bold")
        self.padre = Frame
        self.leGusta = leGusta
        self.arrastra=False
        self.categoriaTrabajo=[]
        self.categoriaTrabajo_nro=0
        self.categoriaProyecto=[]
        self.categoriaProyecto_nro=0
        self.categoriaOcio=[]
        self.categoriaOcio_nro=0
        self.puntero_agarra = "@punteros/closedhand_100189.cur"     
        self.puntero_suelta = "@punteros/openhand_100161.cur"
        self.puntero_dedito = "@punteros/pointinghand_100160.cur"
        self.puntero_reloj = "@punteros/clock_history_icon_160238.cur"

    def pideSalir(self):
        if (messagebox.askyesno("Finalizar?","¿Querés salir del programa realmente?")):
            self.ventana.destroy()
            exit()
            

    def my_callback(self,event):
            posx=event.x
            posy=event.y
            if str(type(event.widget)) =="<class 'tkinter.Listbox'>":
                self.arrastra=False
                self.ventana.config(cursor=self.puntero_dedito)
                posx=posx+700
                posy=posy+230
            else:
                self.arrastra=True

            indice=self.list_1.curselection()
            self.nombreProfesion=self.list_1.get(indice)
            self.indiceActual=indice
            for elemento in self.leGusta:
                if elemento["nombre_profesion"]==self.nombreProfesion:
                    imagenProfesion=elemento["id"]
                    break
            self.imagen=PhotoImage(file="img/Oficios/" + str(imagenProfesion) + ".png")
            self.small_imagen=PhotoImage(file="img/Oficios/small/" + str(imagenProfesion) + ".png")
            
            if (event.y<=520): 
                tope_y=event.y
            else:
                tope_y=520
            
            self.my_img=self.my_c.create_image(posx,posy,image=self.imagen,tag="oficio")

            if (event.x>=1050 and event.x<=1350 and event.y>=10 and event.y<=200):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(posx,posy,image=self.small_imagen,tag="small_oficio")
                self.ventana.config(cursor=self.puntero_agarra)
            elif (event.x>=1050 and event.x<=1350 and event.y>=230 and event.y<=420):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(posx,posy,image=self.small_imagen,tag="small_oficio")
                self.ventana.config(cursor=self.puntero_agarra)
            elif (event.x>=1050 and event.x<=1350 and event.y>=450 and event.y<=640):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(posx,posy,image=self.small_imagen,tag="small_oficio")
                self.ventana.config(cursor=self.puntero_agarra)
            elif (event.x>=550 and event.x<=850 and event.y>=450 and event.y<=640):
                self.my_c.delete("oficio")
                self.my_img=self.my_c.create_image(posx,posy,image=self.small_imagen,tag="small_oficio")
                self.ventana.config(cursor=self.puntero_agarra)
            else:
                if self.arrastra:
                    self.ventana.config(cursor=self.puntero_agarra)
                else:
                   self.ventana.config(cursor=self.puntero_suelta)
 
    
    def solto(self,event):
        self.ventana.config(cursor=self.puntero_suelta)
        if (self.arrastra):
            self.arrastra=False
            if (event.x>=1050 and event.x<=1350 and event.y>=10 and event.y<=200):
                self.categoriaTrabajo.append(self.nombreProfesion)
                self.list_1.delete(self.indiceActual)
                self.categoriaTrabajo_nro=self.categoriaTrabajo_nro +1
                self.trabajo=self.my_c.create_rectangle(1050,10,1350,200,fill='SlateGray1', outline='black')
                self.my_c.create_text(1200,180,font=self.fuente,text="Trabajo (" + str(self.categoriaTrabajo_nro) + ")" )
                #self.imagenTrabajo=PhotoImage(file="trabajo.png")
                self.my_imgTrabajo=self.my_c.create_image(1200,85,image=self.imagenTrabajo)
                self.my_c.delete("small_oficio")

            elif (event.x>=1050 and event.x<=1350 and event.y>=230 and event.y<=420):
                self.categoriaProyecto.append(self.nombreProfesion)
                self.list_1.delete(self.indiceActual)
                self.categoriaProyecto_nro=self.categoriaProyecto_nro +1
                self.hogar=self.my_c.create_rectangle(1050,230,1350,420,fill='SlateGray2', outline='black')
                self.my_c.create_text(1200,400,font=self.fuente,text="Proyecto de vida (" + str(self.categoriaProyecto_nro) + ")" )
                #self.imagenProyecto=PhotoImage(file="proyecto.png")
                self.my_imgProyecto=self.my_c.create_image(1200,280,image=self.imagenProyecto)
                self.my_c.delete("small_oficio")

            elif (event.x>=1050 and event.x<=1350 and event.y>=450 and event.y<=640):
                self.categoriaOcio.append(self.nombreProfesion)
                self.list_1.delete(self.indiceActual)
                self.categoriaOcio_nro=self.categoriaOcio_nro +1
                self.pasatiempo=self.my_c.create_rectangle(1050,450,1350,640,fill='SlateGray3', outline='black')
                self.my_c.create_text(1200,620,font=self.fuente,text="Pasatiempo (" + str(self.categoriaOcio_nro) + ")" )
                #self.imagenPasatiempo=PhotoImage(file="pasatiempo.png")
                self.my_imgPasatiempo=self.my_c.create_image(1225,515,image=self.imagenPasatiempo)
                self.my_c.delete("small_oficio")

            elif (event.x>=550 and event.x<=850 and event.y>=450 and event.y<=640):
                self.list_1.delete(self.indiceActual)
                self.borrar=self.my_c.create_rectangle(550,450,850,640,fill='red', outline='black')
                self.my_c.create_text(700,620,font=self.fuente,text="Ya no me gusta")
                self.my_imgBorrar=self.my_c.create_image(725,515,image=self.imagenBorrar)
                self.my_c.delete("small_oficio")
                for elemento in self.leGusta:
                    if elemento["nombre_profesion"]==self.nombreProfesion:
                        self.leGusta.remove(elemento)
                        break  

            if (self.list_1.size()==0):
                #Fin  - repinto los totales de 'Me Gusta'
                self.Final()

    def mostrar(self):
        self.ventana=Toplevel()
        #ventana.deiconify()
        self.ventana.title("Dar Pye - Proyectando tu futuro")
        self.ventana.geometry("1358x730+0+0")
        self.ventana.resizable(False,False)
        self.ventana.state("zoomed")
        self.ventana.configure(background=self.color)
        self.ventana['cursor'] = self.puntero_suelta , self.puntero_dedito,self.puntero_agarra,  self.puntero_reloj 
        self.ventana.protocol("WM_DELETE_WINDOW",self.pideSalir)
        icono_chico = PhotoImage(file="img/logo16.png")
        icono_grande = PhotoImage(file="img/logo32.png")
        self.   ventana.iconphoto(False, icono_grande, icono_chico)


        self.my_c=Canvas(self.ventana,width=2000,height=1500,bg=self.color)
        self.my_c.place(x=0,y=0)  
        self.my_c.bind('<B1-Motion>',self.my_callback)
        self.my_c.bind('<ButtonRelease-1>',self.solto)
        self.frameListOficios=Frame(self.ventana) 
        self.scrollbar = Scrollbar(self.frameListOficios,orient="vertical",cursor="left_ptr")
        self.list_1 = Listbox(self.frameListOficios,cursor="left_ptr", selectmode=SINGLE,width=17, height=15, yscrollcommand=self.scrollbar.set, font=("Verdana", 22))
        self.list_1.pack(side="left", fill="y")
        self.scrollbar.config(command=self.list_1.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frameListOficios.place(x=30,y=50)
        self.scrollbar.pack( side = RIGHT, fill = Y )
        self.list_1.bind('<<ListboxSelect>>', self.my_callback)


        index=0
        for oficio in self.leGusta:
            self.list_1.insert(index,oficio["nombre_profesion"])
            index=index + 1
        self.l1=Label(self.my_c,text="   Arrastrá cada uno de tus gustos del listado a las categorías que le correspondan    ",bg=self.color,font=self.fuente_negrita,fg="navy")
        self.l1.place(x=2,y=690)

        self.trabajo=self.my_c.create_rectangle(1050,10,1350,200,fill='SlateGray1', outline='black')
        self.hogar=self.my_c.create_rectangle(1050,230,1350,420,fill='SlateGray2', outline='black')
        self.pasatiempo=self.my_c.create_rectangle(1050,450,1350,640,fill='SlateGray3', outline='black')
        self.borrar=self.my_c.create_rectangle(550,450,850,640,fill='red', outline='black')

        self.imagenTrabajo=PhotoImage(file="img/trabajo.png")
        self.my_imgTrabajo=self.my_c.create_image(1200,85,image=self.imagenTrabajo)

        self.imagenProyecto=PhotoImage(file="img/proyecto.png")
        self.my_imgProyecto=self.my_c.create_image(1200,280,image=self.imagenProyecto)

        self.imagenPasatiempo=PhotoImage(file="img/pasatiempo.png")
        self.my_imgPasatiempo=self.my_c.create_image(1225,515,image=self.imagenPasatiempo)

        self.imagenBorrar=PhotoImage(file="img/nogusta.png")
        self.my_imgBorrar=self.my_c.create_image(725,515,image=self.imagenBorrar)

        self.my_c.create_text(1200,180,font=self.fuente,text="Trabajo" )
        self.my_c.create_text(1200,400,font=self.fuente,text="Proyecto de vida")
        self.my_c.create_text(1200,620,font=self.fuente,text="Pasatiempo")
        self.my_c.create_text(700,620,font=self.fuente,text="Ya no me gusta")

    def Final(self):
            self.ventana.config(cursor=self.puntero_reloj)
            self.imagenGusta=PhotoImage(file="img/gusta.png")
            self.my_imgGusta=self.my_c.create_image(550,150,image=self.imagenGusta)
            TInfo=Text(self.my_c,font=self.fuente_negrita,wrap=WORD,height=3,width=30,bg="Khaki",cursor=self.puntero_reloj)
            TInfo.place(x=380,y=300)
            TInfo.insert("1.0","\n  Muy bien, pasamos a la última etapa!")
            self.ventana.after(3000,lambda: self.createWidgetsFinal())

    def createWidgetsFinal(self):
        self.ventana.config(cursor=self.puntero_dedito)
        pantalla3=Stage3(Frame, self.leGusta,self.categoriaTrabajo,self.categoriaProyecto,self.categoriaOcio)
        pantalla3.mostrar()
        self.ventana.after(2000,lambda: self.ventana.destroy())
