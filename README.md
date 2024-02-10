# Proyecto Alumnos

<br/>

![Logo carena](https://iscarena-cba.infd.edu.ar/sitio/wp-content/uploads/2018/07/logocarenacirculo.png)

<br/>

## **Instituto Superior Dr. Carlos Maria Carena**

<br/>

### Presentación
* Asignatura: Programación II
* Curso: Segundo
* Ciclo: 2023
* Alumno: Matias Nicolas Arregui
* Enlace al perfil del alumno: [**@MatiasAshegui**](https://gitlab.com/MatiasAshegui)
* Docente: [**@carlosmurua**](https://gitlab.com/carlosmurua)
* Enlace al repositorio: [Repositorio Iefi 2 Libros](https://gitlab.com/MatiasAshegui/iefi_prog2_c_arregui_matias)
* Autor: [@MatiasAshegui](https://gitlab.com/MatiasAshegui)


## Modulos componentes del proyecto

#### **Controler**
Administra la vista proprcionada por el modulo **view** y el modelo de tablas tomado del modulo **model**.

#### **Model**
Proporciona el formato que sera representado en la base de datos llamada **alumnos.sqlite3** mediante la utilizacion del modulo **dbConn**.

#### **View**
Modulo donde se proporcionaran las dimensiones y propiedades esteticas que se proyectaran en la ventana.

#### **Database**
Modulo encargado de crear, conectar y llevar a cabo las acciones CRUD en la base de datos establecida en el modulo **model**.


## Descripción de proposito y objetivos

El propósito del proyecto es establecer una comunicación con la base de datos llamada **libros.sqlite3**, lo que nos permite realizar el mantenimiento de datos, actualizarlos, eliminarlos y cargarlos. Esto se logra mediante la carga de libros a través de la interfaz proporcionada por el módulo **Views**, todo gracias a la gestión del módulo **Model** y el mencionado anteriormente, a través del módulo **Controler**. El objetivo es la persistencia de datos en la base de datos. Además, otro objetivo es contar con un código capaz de adaptarse a futuras modificaciones que nos permitan agregar nuevas funcionalidades.

## Arquitectura

Utilizamos la arquitectura llamada MVC (Modelo Vista Controlador). Mediante esta, dividimos la estructura en tres pilares: **Model**, **View** y **Controler**. **Model** se encarga de manejar los datos de la base de datos mediante el uso del módulo **dbConn**. **View** se encarga de proporcionar una interfaz gráfica que permite visualizar los datos y manipularlos mediante el módulo **Controler**, que como hemos escrito anteriormente, actúa como puente entre el módulo **Model** y **View**. En resumen, podemos decir que el módulo **View** se encarga de la vista. El módulo **Model** nos permite interactuar con la base de datos. El módulo **Controler** permite la interacción de la interfaz gráfica y el manejo de acciones CRUD de la base de datos

## Como clonar el repositorio
Primero, abrir la consola CMD del sistema:
    * Presiona la tecla Windows + R, lo que abrirá un cuadro de diálogo ejecutar. Escribe “cmd” y presiona Enter.
    * Esto abrirá la consola de comandos. Una vez allí, escribe la ruta de la carpeta donde clonarás el repositorio. Por ejemplo: cd usuario\Matias\carpetaRepositorio. Recuerda usar el comando “cd”, que te permite navegar a la ruta especificada después de la ruta.
Segundo, escribir el siguiente comando:
    -git clone https://gitlab.com/MatiasAshegui/iefi_prog2_c_arregui_matias.git

Te dejamos videos complementarios.
* [Como configurar mi Git](https://www.youtube.com/watch?v=yVh5UwTZUKs)
* [Como clonar el repositorio](https://youtu.be/yVh5UwTZUKs?si=tYcca6Fz_zNcmscT&t=286)

## Requisitos, instalación, configuración y uso

#### Realizaremos las siguientes importaciones:

**dbConn**
* import sqlite3

**Model**
* from datetime import date

**View**
* import tkinter as tk
* from tkinter import ttk, messagebox
* from datetime import datetime, date
* from ttkbootstrap import Style

#### Pre-requisitos

* [Visual Studio Code: Instrucciones de instalación y extensiones](https://docs.google.com/document/d/1t895ZZOT0VsJzn9VYbaolQj6FZcLf9OL4CPLc2mAiRs/edit?usp=sharing)
* [Python: Instrucciones de instalación, paquetes y extensiones para visual code](https://www.python.org/)

#### Necesitaras instalar el siguiente paquete mediante el uso de **pip**:

**Tener actualizado el pip es fundamental para instalar los paquetes. A continuacion te dejamos el comando y material de apoyo.**

* python -m pip install --upgrade pip
* [Material de apoyo en español](https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=56&codigo=56&inicio=45)
* [Material de apoyo suplementario en ingles](https://codedamn.com/news/python/upgrade-pip-python)

**Instalacion paquete ttkbootstrap**

* pip install ttkbootstrap
* [Link de ayuda en instalacion](https://pypi.org/project/ttkbootstrap/)

#### Requisitos

**Software**

El código fue desarrollado utilizando la versión 3.12.0 de Python. Para poder descargar esta versión, necesitarás tener instalado Windows 10 o una versión superior. Sin embargo, se recomienda tener al menos la versión 3.11 de Python para garantizar la compatibilidad.

Aquí te dejo el enlace directo al sitio oficial de Python, donde podrás descargar la versión más reciente del lenguaje de programación:

* [Link de descarga](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)
* [Link del sitio web](https://www.python.org/)

**Las extensiones recomendadas para trabajar con el código en visual code son las siguientes:**

* [Compilador de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* En caso de no utilizar la extensión mencionada anteriormente, puedes abrir una terminal pulsando las teclas Ctrl + Shift + ñ. Una vez abierta la terminal, escribe: python main.py para ejecutar el archivo directamente desde la consola. No olvides asegurarte de estar en la ruta correcta, de lo contrario, el archivo no se ejecutará.

* El siguiente paquete de extensiones nos permite manejarnos en un entorno mas favorable y propicio para el desarrollo.
* [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)

* La siguiente extensión nos permite documentar de manera ordenada el código.
* [Autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

**Hardware**

Para un rendimiento óptimo al manipular datos, se recomienda tener al menos 4GB de RAM, ya que se procesan muchos datos en segundo plano. En cuanto al procesador, el mínimo requerido es un Pentium. Aunque el programa en sí no ocupa mucho espacio, es aconsejable tener al menos 10GB de almacenamiento disponible en la ROM. Esto se debe a que necesitarás instalar el entorno de desarrollo, el paquete Python y las extensiones recomendadas.

## Estructura Carpetas

* controlers\libros_controler.py
    * class Libros_controler()
* database\dbConn.py
    * dbConn()
* image
    * libro-abierto.png
    * logocarena.png
* models\libros_model.py
    * Libros_model()
* views\libros_view.py
    * Libros_view()
    * modalWindow
* centrar_ventana.py
    * centrar()
* main.py
    * mainView
    * main()

## Construido con

[Editor Markdown](https://editormarkdown.com/) - Utilizado para escribir Readme.md

## Versionado

Usamos [GitLab](http://gitlab.com/) para el versionado.

## Autor ✒️

**Matias Arregui Nicolas** - [@MatiasAshegui](https://gitlab.com/MatiasAshegui)

## Te interesaría aprender Python?

Puede haberte resultado un poco confuso ó inentendible el código, por eso te proporcionare canales de YouTube y material de lectura que me han ayudado en el aprendizaje. Espero que te resulten útiles.

Estos canales me han ayudado de gran manera a entender conceptos claves.
* [Canal "HolaMundo"](https://www.youtube.com/watch?v=tQZy0U8s9LY&t=16907s&pp=ygUPYXByZW5kZXIgcHl0aG9u)
* [Canal "MoureDev"](https://www.youtube.com/watch?v=Kp4Mvapo5kc&pp=ygUPYXByZW5kZXIgcHl0aG9u)

Libro de gran ayuda para uso del modulo Tkinter.
* [Tkinter guide](https://drive.google.com/file/d/1wt5dDbBM1Ms0cynCzl-tM4OWqKaBLCOB/view?usp=sharing)

Paginas web de mucha ayuda.
* [El libro de python](https://ellibrodepython.com/)
* [Programiz](https://www.programiz.com/python-programming/first-program)
* [Recursos Python Tkinter](https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/)
