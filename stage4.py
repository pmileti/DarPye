from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
from PIL import Image, ImageTk
from tkinter import messagebox 
import openai
import threading




def open_url(event,url):
    webbrowser.open_new(url)

class Stage4(Frame):
    def __init__(self, Frame, leGusta,dataTrabajo,dataProyecto,dataOcio,dataAnio,dataSiete,dataQuince):
        self.color="#90EE90"
        self.fuente=("Verdana",20)
        self.fuente_negrita=("Verdana",18,"bold")
        self.padre = Frame
        self.leGusta=leGusta
        self.dataTrabajo = dataTrabajo
        self.dataProyecto=dataProyecto
        self.dataOcio=dataOcio
        self.dataUnAnio=dataAnio
        self.dataSieteAnios=dataSiete
        self.dataQuinceAnios=dataQuince

    def pideSalir(self):
        if (messagebox.askyesno("Finalizar?","¿Querés salir del programa realmente?")):
            self.ventana.destroy()
            exit()



    def mostrar(self):
        self.ventana=Toplevel()
        #ventana.deiconify()
        self.ventana.title("Dar Pye - Proyectando tu futuro")
        self.ventana.geometry("1358x730+0+0")
        self.ventana.resizable(False,False)
        self.ventana.state("zoomed")
        self.ventana.configure(background=self.color)
        self.ventana.protocol("WM_DELETE_WINDOW",self.pideSalir)
        icono_chico = PhotoImage(file="img/logo16.png")
        icono_grande = PhotoImage(file="img/logo32.png")
        self.ventana.iconphoto(False, icono_grande, icono_chico)

        self.my_c=Canvas(self.ventana,width=2000,height=1500,bg=self.color)
        self.my_c.place(x=0,y=0)  
        df = pd.DataFrame(self.leGusta)
        counts = df.groupby('area').size().to_dict()
        labels = list(counts.keys())
        sizes = list(counts.values())
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        txtArtesYOficio="\n\tA continuación verás un enlace a cursos cortos relacionados con tus gustos que brinda el municipio de Merlo\t\n\n\n"
        lblCursos=Label(self.ventana, text=txtArtesYOficio, bg="white",height=3, bd=2, relief="solid")
        lblCursos.place(x=650,y=10)
        lblArtesYOficios = Label(self.ventana, text="Escuela Municipal de Artes y Oficios",bg="white", fg="blue", cursor="hand2")
        lblArtesYOficios.bind("<Button-1>", lambda event:open_url(event,"https://www.merlo.gob.ar/artesyoficios/"))
        lblArtesYOficios.place(x=880,y=30)
        textoCFP=" Podés acceder a cursos de los CFP (Centro de Formación Profesional) para concretar tus proyectos en el corto plazo. \nEn Merlo hay 3 Centros de Formación Profesional: CFP401, CFP402 y CFP403. \nPuedes ver la ubicación de ellos en el mapa y hacer clic para mas información."
        lblCFP=Label(self.ventana,text= textoCFP,heigh=4, bg="white", bd=2, relief="solid")
        lblCFP.place(x=680,y=70)
        self.imagenCFP=PhotoImage(file="img/Establecimientos/cfp.gif")
        self.my_imgCFP=Label(self.ventana,image=self.imagenCFP)
        self.my_imgCFP.place(x=720,y=140)
        self.my_imgCFP.image=self.imagenCFP

        imagenCFP403=PhotoImage(file="img/Establecimientos/403.png")
        my_imgCFP403=Label(self.ventana,image=imagenCFP403,cursor="hand2")
        my_imgCFP403.place(x=967,y=263)
        my_imgCFP403.image=imagenCFP403
        my_imgCFP403.bind('<Button-1>',lambda event:open_url(event,"http://catalogo.inet.edu.ar/institucion/referer:148/centro-de-formacia-n-profesional-n-403-5123"))

        textoSuperior="   En Merlo podés formarte a mediano y largo plazo por medio de esta Universidad y este terciario, haz clic en ellos   "
        lblSuperior=Label(self.ventana,text= textoSuperior,heigh=2, bg="white", bd=2, relief="solid")
        lblSuperior.place(x=690,y=540)
 
        imagenISFT177=PhotoImage(file="img/Establecimientos/ISFT177.png")
        my_imgISFT177=Label(self.ventana,image=imagenISFT177,cursor="hand2")
        my_imgISFT177.place(x=1040,y=580)
        my_imgISFT177.image=imagenISFT177
        my_imgISFT177.bind('<Button-1>',lambda event:open_url(event,"https://isft177.edu.ar/"))


        imagenUNO=PhotoImage(file="img/Establecimientos/UNO.png")
        my_imgUNO=Label(self.ventana,image=imagenUNO,cursor="hand2")
        my_imgUNO.place(x=710,y=590)
        my_imgUNO.image=imagenUNO
        my_imgUNO.bind('<Button-1>',lambda event:open_url(event,"http://www.uno.edu.ar"))


        imagenCFP402=PhotoImage(file="img/Establecimientos/402.png")
        my_imgCFP402=Label(self.ventana,image=imagenCFP402,cursor="hand2")
        my_imgCFP402.place(x=731,y=426)
        my_imgCFP402.image=imagenCFP402
        my_imgCFP402.bind('<Button-1>',lambda event:open_url(event,"http://catalogo.inet.edu.ar/institucion/referer:660/centro-de-formacia-n-profesional-n-402-1120"))

        imagenCFP401=PhotoImage(file="img/Establecimientos/401.png")
        my_imgCFP401=Label(self.ventana,image=imagenCFP401,cursor="hand2")
        my_imgCFP401.place(x=1032,y=385)
        my_imgCFP401.image=imagenCFP401
        my_imgCFP401.bind('<Button-1>',lambda event:open_url(event,"http://catalogo.inet.edu.ar/institucion/centro-de-formacion-profesional-n-401-san-jose-1119"))

        if len(self.dataTrabajo)==0:
            txtResumen="\tNinguna de las fotos te identifican con un futuro trabajo. "  
        elif len(self.dataTrabajo)==1:
            txtResumen="\tEl trabajo que te gustaria tener es " + self.dataTrabajo[0]  
        else:
            trabajos=""
            for t in self.dataTrabajo:
                if t==self.dataTrabajo[-1]:
                    if self.dataTrabajo[-1][0]!='I' :
                        trabajos=trabajos + " y " + t
                    else:
                        trabajos=trabajos + " e " + t
                elif t==self.dataTrabajo[0]:
                    trabajos=trabajos + " " + t
                else:
                    trabajos=trabajos + ", " + t
            txtResumen="\tTu aspiración es acceder a estos trabajos: \n-"+ trabajos +"\t"

  

        txtResumen=txtResumen + "\n\nTus gustos se relacionan en mayor medida con:"
      #  print("ESTADISTICAS:")
      #  print(counts) 
        maximo=counts[0][1]
        for elemento in counts:
            if elemento[1]==maximo:
                txtResumen =txtResumen + "\n\t - " + elemento[0]
            else:
                break

        lblResumen=Label(self.ventana, text=txtResumen,font=("Verdana",10,"bold"), bg="white",height=10,width=70, bd=2, relief="solid")
        lblResumen.place(x=30,y=550)
  
        fig, ax = plt.subplots()
        fig.patch.set_facecolor(self.color)
        ax.pie(sizes, labels=labels, autopct="%0.1f %%")

        canvas = FigureCanvasTkAgg(fig, master=self.ventana)
        canvas.get_tk_widget().place(x=10,y=7)
        
        #pack(side=TOP, fill=BOTH, expand=1.0)
        ax.set_title('Visualización gráfica de áreas de interés')
        


        index=0
        #for oficio in self.dataTrabajo:
        #    print(index,oficio)
        #    index=index + 1

        #print(    
        #self.leGusta,
        #self.dataTrabajo,
        #self.dataProyecto,
        #self.dataOcio,
        #self.dataUnAnio,
        #self.dataSieteAnios,
        #self.dataQuinceAnios
        #)

        self.l1=Label(self.my_c,height=2,text=" Comparte estas conclusiones con tus profesores\n o Equipo de Orientación Escolar   ",bg=self.color,font=self.fuente_negrita,fg="navy")
        self.l1.place(x=5,y=480)
        hiloCuento=threading.Thread(target=self.cuento)
        self.ventana.after(1000,lambda: hiloCuento.start())

    def cuento(self):
        pedir="Escribe un cuento optimista sobre un estudiante que sueña con "
        if(len(self.dataTrabajo)>0):
            pedir+="trabajar de "+",".join(self.dataTrabajo)
        if(len(self.dataTrabajo)>0):
            pedir+=" su pasatiempo favorito se basa en ser "+",".join(self.dataOcio)
        if(len(self.dataProyecto)>0):
            pedir+=" tiene como proyecto de vida ser "+",".join(self.dataProyecto)
        if(len(self.dataUnAnio)>0):
            pedir+=" El año proximo le gustaria ser "+",".join(self.dataUnAnio)
        if(len(self.dataSieteAnios)>0):
            pedir+=" En siete años le gustaria lograr ser "+",".join(self.dataSieteAnios)
        if(len(self.dataQuinceAnios)>0):
            pedir+=" En quince años le gustaria llegar a ser "+",".join(self.dataQuinceAnios)
        #print(pedir)
        openai.api_key = "INGRESE SU API KEY AQUI"
        completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=pedir,
                                          max_tokens=2048)
        respuesta=completion.choices[0].text
        
        self.ventanaCuento=Toplevel()
        self.ventanaCuento.title("Dar Pye - Proyectando tu futuro - Inventamos una historia a partir de tus gustos")
        self.ventanaCuento.geometry("800x600+300+50")
        self.ventanaCuento.resizable(False,False)
        self.ventana.state("zoomed")
        self.ventanaCuento.configure(background=self.color)
        #self.ventana.protocol("WM_DELETE_WINDOW",pideSalir)
        icono_chico = PhotoImage(file="img/logo16.png")
        icono_grande = PhotoImage(file="img/logo32.png")
        self.ventanaCuento.iconphoto(False, icono_grande, icono_chico)
        lblTitulo=Label(self.ventanaCuento,text="Un cuento para tí...",font=self.fuente,bg=self.color)
        lblTitulo.place(x=200,y=5)
        txt = Text(self.ventanaCuento, height=22, width=60,font=("Verdana",14),wrap=WORD)
        scroll = Scrollbar(self.ventanaCuento)
        txt.configure(yscrollcommand=scroll.set)
        txt.pack(side=LEFT,padx=(30,30))
        scroll.config(command=txt.yview)
        scroll.pack(side=RIGHT, fill=Y)
        txt.insert(END, respuesta )
        self.ventanaCuento.focus_set()

    def Final(self):
            #self.imagenGusta=PhotoImage(file="img/gusta.png")
            #self.my_imgGusta=self.my_c.create_image(200,310,image=self.imagenGusta)
            TInfo=Text(self.my_c,font=self.fuente,wrap=WORD,height=3,width=45,bg="Khaki")
            TInfo.place(x=320,y=300)
            TInfo.insert("1.0","\n  Felicitaciones, terminamos! Ahora a enfocarte en alcanzar tus sueños! Éxitos!")
            self.ventana.after(3000,lambda: self.createWidgetsFinal())

    def createWidgetsFinal(self):
     #   pantalla4=Stage4(Frame, self.leGusta,self.categoriaTrabajo,self.categoriaProyecto,self.categoriaOcio,self.dataUnAnio,self.dataSieteAnios,self.dataQuinceAnios)
      #  pantalla4.mostrar()
        self.ventana.after(2000,lambda: exit())


