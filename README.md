# Dar Pye
Dar Pye es una aplicación de orientación vocacional desarrollada en Python junto con herramientas de inteligencia artificial.

![Portada](https://github.com/pmileti/DarPye/blob/main/capturas/0.png)

**Origen de Dar Pye:**

Durante muchos años, junto con el Equipo de Orientación Escolar (EOE) de la escuela, utilizamos Dar Pie, un software de orientación vocacional con el que nuestros estudiantes proyectaban su futuro en función de sus gustos. En el año 2022 intentamos utilizarlo en las netbooks de Conectar Igualdad con Windows 10 y descubrimos que no está preparado para correr en ese sistema operativo, así que decidí hacer una nueva versión de cero inspirada en el Dar Pie original, pero con los cambios que consideramos fundamentales junto a las EOE: Viviana Labonia, Sandra Pérez y Mailén Pacheco, a quienes agradezco su valioso aporte :+1:

# Modo de uso para devs:

Esta aplicación utiliza Tkinter como GUI junto a otros módulos que deberán ser instalados: matplotlib, numpy, pandas, pillow y openai. Las dependencias están indicadas en el correspondiente archivo requeriments.txt y podrán ser instaladas mediante el comando:

```
pip install -r requirements.txt
```

**Importante:** Esta aplicación utiliza el chat GPT-3 de OpenAI para generar un cuento final. En la línea 188 de stage4.py cada dev deberá colocar su propia API Key:

```
openai.api_key = "INGRESE SU API KEY AQUI"

```

Finalmente para lanzar la aplicación se ejecuta desde consola:

```
python DarPye.pyw
```

# Acerca de la aplicación Dar Pye

**Pantalla Inicial:** Aquí el usuario verá 100 fotografías que irán apareciendo de forma aleatoria. Cada fotografía deberá arrastrarse a "Me Gusta" o a "No Me Gusta".

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/1.png)

En caso de no comprender de qué trata una fotografía se puede presionar el botón "¿Qué es eso?" para obtener mayor información:

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/2.png)


**2da Etapa**: En esta etapa el usuario deberá categorizar las fotografías seleccionadas en la etapa anterior. Puede asociar una foto con un futuro trabajo, con un proyecto de vida o con pasatiempos. En caso que ya no le despierte interés una fotografía la podrá descartar depositandola en "Ya no me gusta"

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/3.png)

**3ra Etapa**: Aquí el usuario podrá planificar cuando concretar sus proyectos, si a corto plazo, a mediano o a largo plazo. 

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/4.png)

**Conclusiones:** Para finalizar se mostrarán en pantalla estadísticas y propuestas de continuidad de estudios en función de los gustos del usuario. Es importante destacar que esta aplicación está contextualizada en un ámbito escolar específico, por lo tanto se proponen universidades, terciarios, centros de formación profesional y escuelas de artes y oficios localizados en el distrito de Merlo de la provincia de Buenos Aires.

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/5.png)

Finalmente, mientras las concluisiones son presentadas en pantalla, un cuento es generado mediante inteligencia artificial. Este cuento demorará unos minutos en aparecer y está profundamente relacionado a los gustos y proyectos del usuario:

![Pantalla Inicial](https://github.com/pmileti/DarPye/blob/main/capturas/6.png)


# Créditos fotografías

Las fotografías son de uso libre y ellos son quienes las tomaron:


Familia:
Foto de <a href="https://unsplash.com/@dahianawsz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dahiana Waszaj</a> en <a href="https://unsplash.com/es/fotos/fiuevg1aZ4c?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

Abogado:
Image by <a href="https://pixabay.com/users/advogadoaguilar-18212864/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4703938">LEANDRO AGUILAR</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4703938">Pixabay</a>

Médico:
Image by <a href="https://pixabay.com/users/outsideclick-16930317/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6018388">Daniel Dan outsideclick</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6018388">Pixabay</a>

Enfermero:
Image by <a href="https://pixabay.com/users/dimhou-5987327/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4967171">Dim Hou</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4967171">Pixabay</a>

Profesor:
Image by <a href="https://pixabay.com/users/giovannacco-1276399/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1352613">Giovanna Cornelio</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1352613">Pixabay</a>

Ingeniero:
Image by <a href="https://pixabay.com/users/borevina-9505414/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3979490">Borko Manigoda</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3979490">Pixabay</a>

Periodista:
Image by <a href="https://pixabay.com/users/borevina-9505414/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3979490">Borko Manigoda</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3979490">Pixabay</a>

Chef:
Image by <a href="https://pixabay.com/users/marcelavillegas10-9753695/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3975835">Marcela Villegas</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3975835">Pixabay</a>

Arquitecto:
Image by <a href="https://pixabay.com/users/mwitt1337-889520/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2284501">Malachi Witt</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2284501">Pixabay</a>

Contador:
Image by <a href="https://pixabay.com/users/ronaldcandonga-17383039/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5382501">Ronald Carreño</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5382501">Pixabay</a>

Dentista:
Image by <a href="https://pixabay.com/users/luzybarua-19922436/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5925761">luzybarua</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5925761">Pixabay</a>

Psicologo:
Image by <a href="https://pixabay.com/users/olegsturm-20250654/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6008048">Олег Безруков</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6008048">Pixabay</a>

Físico:
Image by <a href="https://pixabay.com/users/pulvermeister-4526766/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5540406">Matthias Bader</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5540406">Pixabay</a>

Arqueólogo:
Image by <a href="https://pixabay.com/users/jamesdemers-3416/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=59150">JamesDeMers</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=59150">Pixabay</a>

Astrónomo:
Image by <a href="https://pixabay.com/users/nasa-imagery-10/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=991">NASA-Imagery</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=991">Pixabay</a>

Biólogo:
Image by <a href="https://pixabay.com/users/sindhudigital-31905036/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7650647">sindhu digital</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7650647">Pixabay</a>

Músico:
Image by <a href="https://pixabay.com/users/stocksnap-894430/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2606347">StockSnap</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2606347">Pixabay</a>

Artista plástico:
Image by <a href="https://pixabay.com/users/uroburos-325152/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=517689">Bronisław Dróżka</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=517689">Pixabay</a>

Actor:
Image by <a href="https://pixabay.com/users/delphinmedia-348407/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=408254">Jens P. Raak</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=408254">Pixabay</a>

Escritor:
Image by <a href="https://pixabay.com/users/gaganmasoun-437970/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2720486">Gagan Masoun</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2720486">Pixabay</a>

Ingeniero en sistemas:
Image by <a href="https://pixabay.com/users/diggitymarketing-12123926/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4165307">Diggity Marketing</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4165307">Pixabay</a>


Ingeniero civil:
Image by <a href="https://pixabay.com/users/dimitrisvetsikas1969-1857980/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1895691">Dimitris Vetsikas</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1895691">Pixabay</a>

Ingeniero electrónico:
Image by <a href="https://pixabay.com/users/jatinderjeetu-28157561/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7632287">Jatinder Jeetu</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7632287">Pixabay</a>

Barman:
Image by <a href="https://pixabay.com/users/radu_floryn22-13702785/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4586277">Florin Radu</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4586277">Pixabay</a>

Cura:
Image by <a href="https://pixabay.com/users/12019-12019/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=79607">David Mark</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=79607">Pixabay</a>

Diseñador de moda:
Image by <a href="https://pixabay.com/users/whirligigtop-3147017/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1611902">whirligigtop</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1611902">Pixabay</a>

Peluquero:
Image by <a href="https://pixabay.com/users/vahidkanani-16386189/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5194406">Vahid Kanani</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5194406">Pixabay</a>

Maquillador:
Image by <a href="https://pixabay.com/users/sarah2708-3399914/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1728358">sarah dolbeau</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1728358">Pixabay</a>

Esteticista:
Image by <a href="https://pixabay.com/users/spabielenda-15378103/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5529815">spabielenda</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5529815">Pixabay</a>

Veterinaria:
Image by <a href="https://pixabay.com/users/12019-12019/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=85925">David Mark</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=85925">Pixabay</a>

Farmacéutica:
Image by <a href="https://pixabay.com/users/maruf_rahman-19661338/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6008806">Maruf Rahman</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6008806">Pixabay</a>

Fisioterapeuta:
Image by <a href="https://pixabay.com/users/elvisclth-448505/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1778029">Cedric Clth</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1778029">Pixabay</a>

Albañil:
Image by <a href="https://pixabay.com/users/rgwarpd-12410814/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4396006">Ricardo Gatica</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4396006">Pixabay</a>

Electricista:
Image by <a href="https://pixabay.com/users/jarmoluk-143740/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1080554">Michal Jarmoluk</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1080554">Pixabay</a>

Carpintero:
Image by <a href="https://pixabay.com/users/e2omedia-13114627/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4805038">E2OMedia</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4805038">Pixabay</a>

Pintor:
Image by <a href="https://pixabay.com/users/jp26jp-308026/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438059">John R Perry</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438059">Pixabay</a>

Muralista:
Image by <a href="https://pixabay.com/users/qimono-1962238/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1380106">Arek Socha</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1380106">Pixabay</a>

Programador:
Image by <a href="https://pixabay.com/users/startupstockphotos-690514/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=593312">StartupStockPhotos</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=593312">Pixabay</a>

Bailarín:
Image by <a href="https://pixabay.com/users/katerina1103990-1287389/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=882940">katerina</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=882940">Pixabay</a>

Escultor:
Image by <a href="https://pixabay.com/users/ottawagraphics-3815775/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4622221">Ana Krach</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4622221">Pixabay</a>

Fotógrafo:
Image by <a href="https://pixabay.com/users/trinhkien91-2878579/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1927265">Kiên Trịnh</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1927265">Pixabay</a>

Diseñador gráfico:
Image by <a href="https://pixabay.com/users/startupstockphotos-690514/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=593299">StartupStockPhotos</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=593299">Pixabay</a>

Futbolista:
Image by <a href="https://pixabay.com/users/keithjj-2328014/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1457988">Keith Johnston</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1457988">Pixabay</a>

Tatuador:
Image by <a href="https://pixabay.com/users/favoritesunfl-1678215/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1062140">favoritesunfl</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1062140">Pixabay</a>

Locutor:
Image by <a href="https://pixabay.com/users/andrzejrembowski-2775184/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4245029">Andrzej Rembowski</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4245029">Pixabay</a>

Ilustrador:
Image by <a href="https://pixabay.com/users/peggy_marco-1553824/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1143686">Peggy und Marco Lachmann-Anke</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1143686">Pixabay</a>

Mozo:
Image by <a href="https://pixabay.com/users/igorsaveliev-50922/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=705881">Igor Saveliev</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=705881">Pixabay</a>

Jardinero:
Image by <a href="https://pixabay.com/users/germanslat-9358457/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3623282">Germans Aļeņins</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3623282">Pixabay</a>

Camarógrafo:
Image by <a href="https://pixabay.com/users/rottonara-596655/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3794634">Mario</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3794634">Pixabay</a>

Bombero:
Image by <a href="https://pixabay.com/users/12019-12019/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=115800">David Mark</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=115800">Pixabay</a>

Mecánico:
Image by <a href="https://pixabay.com/users/dokaryan-9003441/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3691962">Ryan Doka</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3691962">Pixabay</a>

Hockey:
Image by <a href="https://pixabay.com/users/keithjj-2328014/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1537470">Keith Johnston</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1537470">Pixabay</a>

Buzo:
Image by <a href="https://pixabay.com/users/joakant-313743/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=668777">joakant</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=668777">Pixabay</a>

Bibliotecaria:
Image by <a href="https://pixabay.com/users/engin_akyurt-3656355/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2701154">Engin Akyurt</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2701154">Pixabay</a>

Telemarketers:
Image by <a href="https://pixabay.com/users/snehaltechnotery-23061521/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6573021">snehaltechnotery</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6573021">Pixabay</a>

Diputado:
Image by <a href="https://pixabay.com/users/harrystueber-5485086/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3116131">Harry</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3116131">Pixabay</a>

Melómano:
Image by <a href="https://pixabay.com/users/victoria_watercolor-6314823/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7097824">Victoria_Watercolor</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7097824">Pixabay</a>

Repartidor:
Image by <a href="https://pixabay.com/users/bilderwelt68-27027720/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7355135">Bernhard Rauch</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7355135">Pixabay</a>

Conserje:
Image by <a href="https://pixabay.com/users/rodrigo_salomonhc-20127871/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5975962">Rodrigo Salomón Cañas</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5975962">Pixabay</a>

Cajera: 
Foto de <a href="https://unsplash.com/@sql?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">sq lim</a> en <a href="https://unsplash.com/es/fotos/HaZhm6xIUgs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Campesino:
Foto de <a href="https://unsplash.com/@dotjpg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jennifer Griffin</a> en <a href="https://unsplash.com/es/fotos/2vJ-fXZFgz0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Artesano:
Image by <a href="https://pixabay.com/users/orhanyunus18-7628115/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3511239">orhan ç</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3511239">Pixabay</a>

Empresaria:
Foto de <a href="https://unsplash.com/@danedeaner?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dane Deaner</a> en <a href="https://unsplash.com/es/fotos/iJ1lw8iNIy8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Militar:
Image by <a href="https://pixabay.com/users/barskefranck-6433778/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4509265">Franck Barske</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4509265">Pixabay</a>

Editor de video:
Image by <a href="https://pixabay.com/users/thearkow-2526946/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5638146">TheArkow</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5638146">Pixabay</a>

Boxeador:
Image by <a href="https://pixabay.com/users/nbelokonskaya-10929901/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6771969">Natalya</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6771969">Pixabay</a>

Policia:
Image by <a href="https://pixabay.com/users/utility_inc-1078771/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=794111">BodyWorn by Utility</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=794111">Pixabay</a>

Matemático:
Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2820672">Gerd Altmann</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2820672">Pixabay</a>

Reparador PC:
Foto de <a href="https://unsplash.com/@jeshoots?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">JESHOOTS.COM</a> en <a href="https://unsplash.com/es/fotos/sMKUYIasyDM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Secretaria:
Image by <a href="https://pixabay.com/users/claudio_scott-4913238/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2199013">Claudio_Scott</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2199013">Pixabay</a>

Remisero:
Foto de <a href="https://unsplash.com/@romassay?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Rolando Garrido</a> en <a href="https://unsplash.com/es/fotos/R4y4_dvpYXU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Agrimensor:
Foto de <a href="https://unsplash.com/it/@sunburned_surveyor?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Scott Blake</a> en <a href="https://unsplash.com/es/fotos/bGmx6NxEVAU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Modelo:
Image by <a href="https://pixabay.com/users/ahmadardity-3112014/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1746590">Ahmad Ardity</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1746590">Pixabay</a>

Operador sonido:
Foto de <a href="https://unsplash.com/@techivation?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Techivation</a> en <a href="https://unsplash.com/es/fotos/WHTq-xyU40o?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Lavaautos:
Foto de <a href="https://unsplash.com/@fantasyflip?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Philipp Katzenberger</a> en <a href="https://unsplash.com/es/fotos/_DSom3ySpow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Forense:
Image by <a href="https://pixabay.com/users/jp26jp-308026/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438068">John R Perry</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438068">Pixabay</a>

Turista:
Foto de <a href="https://unsplash.com/@imakemyday23?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">imakemyday23</a> en <a href="https://unsplash.com/es/fotos/jSdNbsw3zjs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Nadador:
Foto de <a href="https://unsplash.com/@marcusxsnapz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marcus Ng</a> en <a href="https://unsplash.com/es/fotos/ZbbhkQ0M2AM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Publicista:
Foto de <a href="https://unsplash.com/@jasongoodman_youxventures?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jason Goodman</a> en <a href="https://unsplash.com/es/fotos/Oalh2MojUuk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Escalador:
Image by <a href="https://pixabay.com/users/erikamarcialm-814907/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2101262">Erika Marcial</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2101262">Pixabay</a>

Mago:
Foto de <a href="https://unsplash.com/@roinuj16?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Edson Junior</a> en <a href="https://unsplash.com/es/fotos/YlgnX_ISPLo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Tenista:
Image by <a href="https://pixabay.com/users/andremcenroe-650035/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=934841">Andre Mcenroe</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=934841">Pixabay</a>

Ferretero:
Foto de <a href="https://unsplash.com/@oksdesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Oxana Melis</a> en <a href="https://unsplash.com/es/fotos/OqJ_YPwRAXY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Azafata:
Image by <a href="https://pixabay.com/users/lukasbieri-4664461/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2104594">Lukas Bieri</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2104594">Pixabay</a>

Maestra:
Foto de <a href="https://unsplash.com/@nci?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">National Cancer Institute</a> en <a href="https://unsplash.com/es/fotos/N_aihp118p8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Paseador de perros:
Image by <a href="https://pixabay.com/users/surprising_shots-11873433/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7377662">Mircea - See my collections</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7377662">Pixabay</a>

Director de cine:
Foto de <a href="https://unsplash.com/@bencollins?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ben Collins</a> en <a href="https://unsplash.com/es/fotos/ve79oYQfssw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Ecologista:
Foto de <a href="https://unsplash.com/@oceancleanupgroup?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">OCG Saving The Ocean</a> en <a href="https://unsplash.com/es/fotos/xch7jXAaqqo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Camionero:
Foto de <a href="https://unsplash.com/ja/@averieclaire?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">averie woodard</a> en <a href="https://unsplash.com/es/fotos/j4nBSqFf08U?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Recolector de residuos:
Foto de <a href="https://unsplash.com/@zibik?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">zibik</a> en <a href="https://unsplash.com/es/fotos/iR4mClggzEU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Horticultor:
Foto de <a href="https://unsplash.com/@dirtjoy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Zoe Schaeffer</a> en <a href="https://unsplash.com/es/fotos/W_ISm5LwKHQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Estatua viviente:
Foto de <a href="https://unsplash.com/@diywm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Elizabeth Jamieson</a> en <a href="https://unsplash.com/es/fotos/bMIvS7rTs-A?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Activista:
Foto de <a href="https://unsplash.com/@clemono?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Clem Onojeghuo</a> en <a href="https://unsplash.com/es/fotos/DoA2duXyzRM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Amigos:
Foto de <a href="https://unsplash.com/@masondahl?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mason Dahl</a> en <a href="https://unsplash.com/es/fotos/-7AxXbZekDE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Mochilero:
Foto de <a href="https://unsplash.com/@jamie_fenn?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jamie Fenn</a> en <a href="https://unsplash.com/es/fotos/UhaEl12gyo0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Técnico en alimentos:
Foto de <a href="https://unsplash.com/es/@beenaturalles?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bee Naturalles</a> en <a href="https://unsplash.com/es/fotos/0liWd-xi1v4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
DJ:
Foto de <a href="https://unsplash.com/@piiiiine?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Muhammadh Saamy</a> en <a href="https://unsplash.com/es/fotos/GO1i2timuug?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Basket:
Foto de <a href="https://unsplash.com/@markusspiske?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Markus Spiske</a> en <a href="https://unsplash.com/es/fotos/oXS1f0uZYV4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Verdulero:
Foto de <a href="https://unsplash.com/@yusronell?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Yusron El Jihan</a> en <a href="https://unsplash.com/es/fotos/J0Ug1eCZXFE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
Piloto:
Foto de <a href="https://unsplash.com/@kristopher_allison?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kristopher Allison</a> en <a href="https://unsplash.com/es/fotos/KU4zYj4u0mo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

