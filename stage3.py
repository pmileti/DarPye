from tkinter import *
import time
import numpy as np
from PIL import Image, ImageDraw
from stage4 import Stage4
from tkinter import messagebox 


def redondear(nombre):
    img=Image.open(nombre).convert("RGB")
    npImage=np.array(img)
    #h,w=foto.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,150,150],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('img/temp.png')

class Stage3(Frame):
    def __init__(self, Frame, leGusta,dataTrabajo,dataProyecto,dataOcio):
        self.color="paleGreen2"
        self.fuente=("Verdana",20)
        self.fuente_negrita=("Verdana",22,"bold")
        self.padre = Frame
        self.origen=""
        self.leGusta=leGusta
        self.dataTrabajo = dataTrabajo
        self.dataProyecto=dataProyecto
        self.dataOcio=dataOcio
        self.arrastra=False
        self.dataUnAnio=[]
        self.dataUnAnio_nro=0
        self.dataSieteAnios=[]
        self.dataSieteAnios_nro=0
        self.dataQuinceAnios=[]
        self.dataQuinceAnios_nro=0
        self.puntero_agarra = "@punteros/closedhand_100189.cur"     
        self.puntero_suelta = "@punteros/openhand_100161.cur"
        self.puntero_dedito = "@punteros/pointinghand_100160.cur"
        self.puntero_reloj = "@punteros/clock_history_icon_160238.cur" 

    def pideSalir(self):
        if (messagebox.askyesno("Finalizar?","¿Querés salir del programa realmente?")):
            self.ventana.destroy()
            exit()

    def my_callback(self,event,origen):
            posx=event.x
            posy=event.y
            if str(type(event.widget)) =="<class 'tkinter.Listbox'>":
                self.arrastra=False
                self.ventana.config(cursor=self.puntero_suelta)
                posx=posx+650
                posy=posy+330
                indice=origen.curselection()
                if str(indice)!='()':
                    self.origen=origen
                    self.my_c.bind('<B1-Motion>',lambda event:self.my_callback(event, self.origen))
                else:
                    return
            else:
                self.arrastra=True
            indice=self.origen.curselection()
            self.nombreProfesion=self.origen.get(indice)
            self.indiceActual=indice
            for elemento in self.leGusta:
                if elemento["nombre_profesion"]==self.nombreProfesion:
                    imagenProfesion=elemento["id"]
                    break
            self.imagen=PhotoImage(file="img/Oficios/" + str(imagenProfesion) + ".png")
            self.small_imagen=PhotoImage(file="img/Oficios/small/" + str(imagenProfesion) + ".png")
            
            if (event.y<=550): 
                tope_y=event.y
            else:
                tope_y=550
            
            self.my_img=self.my_c.create_image(posx,posy,image=self.small_imagen,tag="small_oficio")

            if ((event.x>=150 and event.x<=350 and event.y>=450 and event.y<=650) or(event.x>=550 and event.x<=750 and event.y>=450 and event.y<=650) or (event.x>=950 and event.x<=1150 and event.y>=450 and event.y<=650)):
                self.ventana.config(cursor=self.puntero_agarra)
                redondear("img/Oficios/small/" + str(imagenProfesion) + ".png")
                self.small_imagen=PhotoImage(file="img/temp.png")
                self.my_img=self.my_c.create_image(posx+40,posy,image=self.small_imagen,tag="small_oficio")
                
   #         elif (event.x>=550 and event.x<=750 and event.y>=450 and event.y<=650):
   #             self.ventana.config(cursor="hand2")
   #         elif (event.x>=950 and event.x<=1150 and event.y>=450 and event.y<=650):
   #             self.ventana.config(cursor="hand2")
            else:
                if self.arrastra:
                    self.ventana.config(cursor=self.puntero_agarra)
                else:
                   self.ventana.config(cursor=self.puntero_suelta)

    
    def solto(self,event):
        self.ventana.config(cursor=self.puntero_suelta)                
        if (self.arrastra):
            self.arrastra=False
            if (event.x>=150 and event.x<=350 and event.y>=450 and event.y<=650):
                self.dataUnAnio.append(self.nombreProfesion)
                self.origen.delete(self.indiceActual)
                self.dataUnAnio_nro=self.dataUnAnio_nro +1
                self.unAnio=self.my_c.create_oval(150,450,350,650,fill='white', outline='black')
                self.my_c.create_text(250,550,font=self.fuente,text="En 1 año (" + str(self.dataUnAnio_nro) + ")" )
                self.my_c.delete("small_oficio")

            elif (event.x>=550 and event.x<=750 and event.y>=450 and event.y<=650):
                self.dataSieteAnios.append(self.nombreProfesion)
                self.origen.delete(self.indiceActual)
                self.dataSieteAnios_nro=self.dataSieteAnios_nro +1
                self.sieteAnios=self.my_c.create_oval(550,450,750,650,fill='white', outline='black')
                self.my_c.create_text(650,550,font=self.fuente,text="En 7 años (" + str(self.dataSieteAnios_nro) + ")")
                self.my_c.delete("small_oficio")

            elif (event.x>=950 and event.x<=1150 and event.y>=450 and event.y<=650):
                self.dataQuinceAnios.append(self.nombreProfesion)
                self.origen.delete(self.indiceActual)
                self.dataQuinceAnios_nro=self.dataQuinceAnios_nro +1
                self.quinceAnios=self.my_c.create_oval(950,450,1150,650,fill='white', outline='black')
                self.my_c.create_text(1050,550,font=self.fuente,text="En 15 años (" + str(self.dataQuinceAnios_nro) + ")")
                self.my_c.delete("small_oficio")

            if (self.list_1.size()==0 and self.list_2.size()==0 and self.list_3.size()==0):
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
        self.ventana['cursor'] = self.puntero_suelta , self.puntero_dedito,self.puntero_agarra, self.puntero_reloj 
        self.ventana.protocol("WM_DELETE_WINDOW",self.pideSalir)
        icono_chico = PhotoImage(file="img/logo16.png")
        icono_grande = PhotoImage(file="img/logo32.png")
        self.ventana.iconphoto(False, icono_grande, icono_chico)

        self.my_c=Canvas(self.ventana,width=2000,height=1500,bg=self.color)
        self.my_c.place(x=0,y=0)  
        self.my_c.bind('<B1-Motion>',lambda event:self.my_callback(event, None))
        self.my_c.bind('<ButtonRelease-1>',self.solto)

        self.frameListTrabajo=Frame(self.ventana) 
        self.scrollbar = Scrollbar(self.frameListTrabajo,cursor="left_ptr",orient="vertical")
        self.list_1 = Listbox(self.frameListTrabajo,cursor="left_ptr", selectmode=SINGLE,width=17, height=5, yscrollcommand=self.scrollbar.set, font=("Verdana", 22))
        self.list_1.pack(side="left", fill="y")
        self.scrollbar.config(command=self.list_1.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.my_c.create_text(170,30,font=self.fuente,text="Trabajo")
        self.frameListTrabajo.place(x=30,y=50)
        #self.scrollbar.pack( side = RIGHT, fill = Y )
        self.list_1.bind('<<ListboxSelect>>', lambda event:self.my_callback(event, self.list_1))

        index=0
        for oficio in self.dataTrabajo:
            self.list_1.insert(index,oficio)
            index=index + 1


        self.frameListProyecto=Frame(self.ventana) 
        self.scrollbar2 = Scrollbar(self.frameListProyecto,cursor="left_ptr",orient="vertical")
        self.list_2 = Listbox(self.frameListProyecto,cursor="left_ptr", selectmode=SINGLE,width=17, height=5, yscrollcommand=self.scrollbar2.set, font=("Verdana", 22))
        self.list_2.pack(side="left", fill="y")
        self.scrollbar2.config(command=self.list_2.yview)
        self.scrollbar2.pack(side="right", fill="y")
        self.my_c.create_text(650,30,font=self.fuente,text="Proyecto de vida")
        self.frameListProyecto.place(x=480,y=50)
        #self.scrollbar2.pack( side = RIGHT, fill = Y )
        self.list_2.bind('<<ListboxSelect>>', lambda event:self.my_callback(event, self.list_2))

        index=0
        for oficio in self.dataProyecto:
            self.list_2.insert(index,oficio)
            index=index + 1


        self.frameListOcio=Frame(self.ventana) 
        self.scrollbar3 = Scrollbar(self.frameListOcio,cursor="left_ptr",orient="vertical")
        self.list_3 = Listbox(self.frameListOcio,cursor="left_ptr", selectmode=SINGLE,width=17, height=5, yscrollcommand=self.scrollbar3.set, font=("Verdana", 22))
        self.list_3.pack(side="left", fill="y")
        self.scrollbar3.config(command=self.list_3.yview)
        self.scrollbar3.pack(side="right", fill="y")
        self.my_c.create_text(1050,30,font=self.fuente,text="Pasatiempo")
        self.frameListOcio.place(x=930,y=50)
        self.scrollbar3.pack( side = RIGHT, fill = Y )
        self.list_3.bind('<<ListboxSelect>>', lambda event:self.my_callback(event, self.list_3))

        index=0
        for oficio in self.dataOcio:
            self.list_3.insert(index,oficio)
            index=index + 1



        self.l1=Label(self.my_c,text="    Proyectando tu futuro deberás arrastrar cada foto elegida a la línea de tiempo     ",bg=self.color,font=self.fuente_negrita,fg="navy")
        self.l1.place(x=2,y=690)

        self.my_c.create_line(15, 570, 1300, 570,dash=(5,2))
        self.unAnio=self.my_c.create_oval(150,450,350,650,fill='white', outline='black')
        self.sieteAnios=self.my_c.create_oval(550,450,750,650,fill='white', outline='black')

        self.quinceAnios=self.my_c.create_oval(950,450,1150,650,fill='white', outline='black')
        self.my_c.create_text(250,550,font=self.fuente,text="En 1 año" )
        self.my_c.create_text(650,550,font=self.fuente,text="En 7 años")
        self.my_c.create_text(1050,550,font=self.fuente,text="En 15 años")


    def Final(self):
            self.ventana.config(cursor=self.puntero_reloj)
            self.imagenGusta=PhotoImage(file="img/gusta.png")
            self.my_imgGusta=self.my_c.create_image(200,310,image=self.imagenGusta)
            TInfo=Text(self.my_c,font=self.fuente,wrap=WORD,height=3,width=45,bg="Khaki",cursor=self.puntero_reloj)
            TInfo.place(x=320,y=300)
            TInfo.insert("1.0","\n  Finalizamos! Aguardá que procesemos tus gustos! ")
            self.ventana.after(3000,lambda: self.createWidgetsFinal())

    def createWidgetsFinal(self):
        self.ventana.config(cursor=self.puntero_dedito)
        pantalla4=Stage4(Frame, self.leGusta,self.dataTrabajo,self.dataProyecto,self.dataOcio,self.dataUnAnio,self.dataSieteAnios,self.dataQuinceAnios)
        pantalla4.mostrar()
        self.ventana.after(2000,lambda: self.ventana.destroy())
