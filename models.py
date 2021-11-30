from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class Principal():

    def __init__(self,root):
        self.ventana = root
        self.ventana.title('Página Principal')
        self.ventana.resizable(1,1)
        self.ventana.wm_iconbitmap("recursos/icon.ico")

        # Creación del contenedor Frame principal
        frame = LabelFrame(self.ventana, text='Seleccione una opción', bg = '#B3D0F2', fg = 'black',  font = ('Century gotic', 20), width = 50, height = 2, relief = 'sunken')
        frame.grid(columnspan=50, pady=40)

        # Boton para clientes
        self.boton_cliente = ttk.Button(frame, text='Área Cliente',command=self.area_cliente)
        self.boton_cliente.grid(row = 1, column = 2, sticky= N+S+E+W)

        # Boton para proveedores
        self.boton_proveedor = ttk.Button(frame, text='Área Proveedor')
        self.boton_proveedor.grid(row= 2, column = 2, sticky=N+E+S+W)

        # Boton para Administradores


    def db_consulta(self,consulta,parametros=()):
        with sqlite3.connect(self.ventana_inventario) as con:
            cursor=con.cursor()
            resultado = cursor.execute(consulta,parametros)
            con.commit()
        return resultado


    def area_cliente(self):
        # Nueva Ventana
        self.ventana_cliente = Toplevel()
        self.ventana_cliente.title = 'Espacio Cliente'
        self.ventana_cliente.resizable(1,1)
        self.ventana_cliente.geometry('800x800')
        self.ventana_cliente.wm_iconbitmap('recursos/cliente.ico')

        titulo = Label(self.ventana_cliente, text='Bienvenido a su Espacio Cliente', bg = '#B3D0F2', fg = 'black',  font = ('Century gotic', 20), width = 50 , height = 2, relief = 'sunken')
        titulo.grid(row=0,column =0, columnspan= 50)
        frame_cliente = LabelFrame(self.ventana_cliente, text= 'Categorias', bg = '#B3D0F2', fg = 'black',  font = ('Century gotic', 20), width = 20 , height = 2, relief = 'sunken')
        frame_cliente.grid(row=2,column=3,columnspan=60, pady=20)

        # Boton para las gráficas
        self.boton_graficas_venta = ttk.Button(frame_cliente, text='Gráficas de Ventas')
        self.boton_graficas_venta.grid(row=0,column=0,sticky= N+E+S+W)

        # Boton para ver el inventario
        self.boton_inventario_cliente = ttk.Button(frame_cliente, text='Inventario',command=self.inventario)
        self.boton_inventario_cliente.grid(row=1,column=0,sticky=N+E+S+W)

    def inventario(self):

        db = "database/inventario.db"

        #Nueva Ventana
        self.ventana_inventario = Toplevel()
        self.ventana_inventario.title='Inventario'
        self.ventana_inventario.resizable(1,1)
        self.ventana_inventario.geometry('800x800')
        self.ventana_inventario.wm_iconbitmap('recursos/inventario.ico')

        frame = LabelFrame(self.ventana_inventario, bg='#CBF5ED')
        frame.grid(columnspan=2,column=0,row=0)

        frame2 = LabelFrame(self.ventana_inventario, bg='#B3E4F2')
        frame2.grid(column=0,row=1)

        frame3 = LabelFrame(self.ventana_inventario,bg='#B3D0F2')
        frame3.grid(rowspan=2,column=1,row=1)

        frame4 = LabelFrame(self.ventana_inventario,bg='#B6B3F2')
        frame4.grid(column=0, row=2)

        # def create_widgets(self):
        self.titulo = Label(frame, text='INVENTARIO')
        self.titulo.grid(column=0,row=0)

        self.datos_titulo = Label(frame2,text='DATOS')
        self.datos_titulo.grid(columnspan=2,column=0,row=0,pady=5)

        self.datos_codigo = Label(frame2, text ='Código')
        self.datos_codigo.grid(column = 0, row = 1, pady = 15)
        self.datos_ncodigo = Entry(frame2)
        self.datos_ncodigo.grid(column=1,row=1,pady=15)

        self.datos_producto = Label(frame2,text='Producto')
        self.datos_producto.grid(column=0,row=2,pady=15)
        self.datos_nproducto = Entry(frame2)
        self.datos_nproducto.grid(column=1,row=2,pady=15)

        self.datos_precio = Label(frame2,text='Precio')
        self.datos_precio.grid(column=0,row=3,pady=15)
        self.datos_nprecio = Entry(frame2)
        self.datos_nprecio.grid(column=1,row=3)

        self.datos_cantidad = Label(frame2, text='Cantidad')
        self.datos_cantidad.grid(column=0,row=4,pady=15)
        self.datos_ncantidad = Entry(frame2)
        self.datos_ncantidad.grid(column=1,row=4)

        boton_agregar = ttk.Button(frame4, text= 'Guardar')
        boton_agregar.grid(column=0,row=1,pady=1)




    def login(self):
        with sqlite3.connect('proveedores.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM proveedores WHERE usuario = ? AND clave = ?')
        cursor.execute(find_user[(self.usuario.get()),(self.clave.get())])
        results = cursor.fetchall()
        if results:
            self.logf.pack_forget()
            self.head['text'] = self.usuario.get()
            self.head['pady'] = 150
        else:
            ms.showerror('¡Ha habido un error!')

    def widgets_prov(self):
        self.head = Label(self.ventana_prov,text='Inicie Sesión',font = ('Century gotic', 22, 'bold'))
        self.head.grid(columnspan=4)

        self.text_user = Label(self.ventana_prov, text = 'Usuario')
        self.text_user.grid(column=0,row=1)
        self.text_user_n = Entry(self.ventana_prov)
        self.text_user_n.grid(column=1,row=1)

        self.pass_user = Label(self.ventana_prov,text = 'Clave')
        self.pass_user.grid(column=0,row=2)
        self.pass_user_n = Entry(self.ventana_prov)
        self.pass_user_n.grid(column=1,row=2)






