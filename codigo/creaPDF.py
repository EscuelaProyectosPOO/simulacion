import jinja2
import pdfkit
import os
from pathlib import Path



def crear_pdf(ruta_template, informacion,rutacss=''):
    # dividimos la ruta por /, nos devuelve una lista, le indicamos que nos de el ultimo
    # elemento de la lista indicado con un [-1]
    nombre_template = ruta_template.split("/")[-1]
    # obtenemos la ruta del template remplazando en la cadena el nombre del template con 
    # un espacio vacio
    ruta_template = ruta_template.replace(nombre_template,'')

    
    # le decimos donde esta el template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))

    #le decimos cual template vamoa usar
    template = env.get_template(nombre_template)

    # procedemos a remplazar el valor de las variables
    html = template.render(informacion)

    # diccionario de configuracion para el documento de pdf
    options = {'page-size': 'Letter',
                'margin-top':'0.05in',
                'margin-right': '0.05in',
                'margin-bottom': '0.05in',
                'margin-left': '0.05in',
                'encoding': 'UTF-8',
                "enable-local-file-access": "",}

    # crear el pdf
    configuracion = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    # nos da la ruta de downloads del sistema en donde estamos
    path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
    ruta_salida = path_to_download_folder + "/Informe.pdf"
    pdfkit.from_string(html,ruta_salida,css=rutacss,options=options,configuration=configuracion)

if(__name__=="__main__"):

    #nos da la ruta absoluta del template 
    directorio = os.getcwd()
    ruta_template =  directorio +'/template.html'

    # el diccionario debe tener las keys con el mismo nombre que tenemos las variables en el html
    informacion ={"minimo": 234,
                "maximo": "567",
                "promedio":"23.45",
                "tipos": "ron<br>345<br>354",
                "precios":"67<br>34<br>1234",
                "ventas": "125<br>123<br>12",
                "ganancia": "12000<br>345<br>234",
                "ganancia_total": 12346
    }
    crear_pdf(ruta_template=ruta_template, informacion=informacion)