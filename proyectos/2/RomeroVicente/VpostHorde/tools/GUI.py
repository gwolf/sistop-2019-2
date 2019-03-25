import wx
import tools.Estres as Estres
import mimetypes
import os.path
import threading
from wx.lib.plot import PlotCanvas
from tools.plot import plot
import math

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class Grid(wx.Dialog):
    def __init__(self, gridSize, matrix, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        self.gridSize = gridSize
        wx.Dialog.__init__(self, *args, **kwds)
        grid = wxgrid.Grid(self, -1)
        grid.CreateGrid(self.gridSize,self.gridSize)
        self.Show()



class GUI(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: GUI.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.test = Estres.Estres(hilos = 1 ,tiempo = None, url = None, payload = None, tipo = "GET", headers = None,auth = None, archivo = None, archivoRespuestas ="./out")
        self.fileDatos = False
        self.fileHeader = False
        self.datos = None
        self.header = None
        self.timeChecked = False
        self.multipartChecked = False
        self.datosArchChecked = False 
        self.headerArchChecked = False 
        self.testEnProceso = False
        self.SetSize((1000, 400))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.btnArchivoSalida = wx.Button(self.panel_1, wx.ID_ANY, "archivo", style=wx.BU_EXACTFIT)
        self.cmbxTipo = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"], value="GET" , style=wx.CB_DROPDOWN)
        self.txtUrl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.spnTiempo = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=360000)
        self.chkBxTiempo = wx.CheckBox(self.panel_1, wx.ID_ANY, "Activar Tiempo")
        self.spnHilos = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "1", min=0, max=10000, style=wx.SP_ARROW_KEYS | wx.SP_WRAP)
        self.txtHeader = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.rdboxHeader = wx.RadioBox(self.panel_1, wx.ID_ANY, "Opciones Headers", choices=["Usar Texto", "Usar Archivo"], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.btnHeader = wx.Button(self.panel_1, wx.ID_ANY, "Archivo")
        self.txtDatos = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.rdoBoxEntrada = wx.RadioBox(self.panel_1, wx.ID_ANY, "Opciones Entrada", choices=["Usar Texto", "Usar Archivo"], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.btnArchivoEnviar = wx.Button(self.panel_1, wx.ID_ANY, "Archivo")
        self.btnEntrada = wx.Button(self.panel_1, wx.ID_ANY, "Entrada", style=wx.BU_EXACTFIT)
        self.chkbMultiPart = wx.CheckBox(self.panel_1, wx.ID_ANY, "Enviar Multipart")
        self.txtAuth = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.btnReset = wx.Button(self.panel_1, wx.ID_ANY, "Resetear Datos")
        self.btnIniciarTest = wx.Button(self.panel_1, wx.ID_ANY, "Iniciar Test")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.guardarSalida, self.btnArchivoSalida)
        self.Bind(wx.EVT_COMBOBOX, self.getTipo, self.cmbxTipo)
        self.Bind(wx.EVT_TEXT, self.getUrl, self.txtUrl)
        self.Bind(wx.EVT_SPINCTRL, self.getTiempo, self.spnTiempo)
        self.Bind(wx.EVT_TEXT, self.getTiempo, self.spnTiempo)
        self.Bind(wx.EVT_SPINCTRL, self.getHilos, self.spnHilos)
        self.Bind(wx.EVT_TEXT, self.getHilos, self.spnHilos)
        self.Bind(wx.EVT_TEXT, self.getHeader, self.txtHeader)
        self.Bind(wx.EVT_RADIOBOX, self.optHeader, self.rdboxHeader)
        self.Bind(wx.EVT_BUTTON, self.abrirHeader, self.btnHeader)
        self.Bind(wx.EVT_RADIOBOX, self.optDatos, self.rdoBoxEntrada)
        self.Bind(wx.EVT_BUTTON, self.abrirMultipart, self.btnArchivoEnviar)
        self.Bind(wx.EVT_BUTTON, self.abrirDatos, self.btnEntrada)
        self.Bind(wx.EVT_CHECKBOX, self.optMultipart, self.chkbMultiPart)
        self.Bind(wx.EVT_TEXT, self.getAuth, self.txtAuth)
        self.Bind(wx.EVT_BUTTON, self.resetForm, self.btnReset)
        self.Bind(wx.EVT_BUTTON, self.iniciarTest, self.btnIniciarTest)
        self.Bind(wx.EVT_CHECKBOX, self.usarTiempo, self.chkBxTiempo)
        self.Bind(wx.EVT_TEXT, self.getDatos, self.txtDatos)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Ventana.__set_properties
        self.SetTitle("VpostHorde")
        self.rdboxHeader.SetSelection(0)
        self.rdoBoxEntrada.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Ventana.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(0, 6, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblArchivoSalida = wx.StaticText(self.panel_1, wx.ID_ANY, "Archivo Salida:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblArchivoSalida, 5, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 2)
        grid_sizer_1.Add(self.btnArchivoSalida, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblTipo = wx.StaticText(self.panel_1, wx.ID_ANY, "Tipo:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblTipo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cmbxTipo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblUrl = wx.StaticText(self.panel_1, wx.ID_ANY, "URL:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblUrl, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txtUrl, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblTiempo = wx.StaticText(self.panel_1, wx.ID_ANY, "Tiempo:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblTiempo, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.spnTiempo, 3, wx.ALL | wx.EXPAND, 3)
        grid_sizer_1.Add(self.chkBxTiempo, 0, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblHilos = wx.StaticText(self.panel_1, wx.ID_ANY, "Numero de Hilos:")
        grid_sizer_1.Add(lblHilos, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.spnHilos, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblHeader = wx.StaticText(self.panel_1, wx.ID_ANY, "Header:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblHeader, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txtHeader, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.rdboxHeader, 0, wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.btnHeader, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblDatos = wx.StaticText(self.panel_1, wx.ID_ANY, "Datos:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblDatos, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.txtDatos, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.rdoBoxEntrada, 0, 0, 0)
        lblArchivoEnviar = wx.StaticText(self.panel_1, wx.ID_ANY, "Archivo a Enviar:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblArchivoEnviar, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.btnArchivoEnviar, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblArchivoEntrada = wx.StaticText(self.panel_1, wx.ID_ANY, "Seleccionar Archivo:",style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblArchivoEntrada, 0, 0, 0)
        grid_sizer_1.Add(self.btnEntrada, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.chkbMultiPart, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        lblAuth = wx.StaticText(self.panel_1, wx.ID_ANY, "Auth:", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(lblAuth, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txtAuth, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.btnReset, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.btnIniciarTest, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        self.panel_1.SetSizer(grid_sizer_1)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_1.Add((0, 0), 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def guardarSalida(self, event):
        with wx.FileDialog(self, "Guardar salida", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                self.test.archivoRespuestas = "out"
                return
            self.test.archivoRespuestas = fileDialog.GetPath()


    def getTipo(self, event):  # wxGlade: Ventana.<event_handler>
        self.test.tipo = self.cmbxTipo.GetStringSelection()

    def getUrl(self, event):  # wxGlade: Ventana.<event_handler>
        self.test.url = self.txtUrl.GetLineText(0)


    def getTiempo(self, event):  # wxGlade: Ventana.<event_handler>
        if self.timeChecked == True:
            self.test.tiempo = self.spnTiempo.GetValue()

    def getHilos(self, event):  # wxGlade: Ventana.<event_handler>
        self.test.hilos = self.spnHilos.GetValue()

    def getHeader(self, event):  # wxGlade: Ventana.<event_handler>
        if self.headerArchChecked == False:
            self.test.setHeader(self.txtHeader.GetLineText(0))
        else:
            self.header = self.txtHeader.GetLineText(0)

    def optHeader(self, event):  # wxGlade: Ventana.<event_handler>
        if self.rdboxHeader.GetSelection() == 1:
            self.headerArchChecked = True
        else:
            self.headerArchChecked = False

    def abrirHeader(self, event):  # wxGlade: Ventana.<event_handler>
        with wx.FileDialog(self, "Abrir archivo de headers",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            filename = fileDialog.GetFilename()
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as payload:
                    self.test.payload = ''
                    for line in payload:
                        self.test.payload = self.test.payload.replace('\n','') + line
            except IOError:
                wx.LogError("no se puede abrir el archivo '%s'." % newfile)

    def optDatos(self, event):  # wxGlade: Ventana.<event_handler>
        if self.rdoBoxEntrada.GetSelection() == 1:
            self.datosArchChecked = True
        else:
            self.datosArchChecked = False

    def abrirMultipart(self, event):  # wxGlade: Ventana.<event_handler>
        with wx.FileDialog(self, "Abrir archivo multipart",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            filename = fileDialog.GetFilename()
            pathname = fileDialog.GetPath()
            try:
                self.test.file = open(pathname, 'rb')
            except IOError:
                wx.LogError("no se puede abrir el archivo '%s'." % newfile)

    def abrirDatos(self, event):  # wxGlade: Ventana.<event_handler>
        with wx.FileDialog(self, "Abrir archivo de datos",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            filename = fileDialog.GetFilename()
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as payload:
                    self.test.payload = ''
                    for line in payload:
                        self.test.payload = self.test.payload.replace('\n','') + line
            except IOError:
                wx.LogError("no se puede abrir el archivo '%s'." % newfile)

    def optMultipart(self, event):  # wxGlade: Ventana.<event_handler>
        self.multipartChecked = self.chkbMultiPart.IsChecked()

    def getAuth(self, event):  # wxGlade: Ventana.<event_handler>
        self.test.auth = self.txtAuth.GetLineText(0)

    def resetForm(self, event):  # wxGlade: Ventana.<event_handler>
        Estres.Estres(hilos = 1 ,tiempo = None, url = None, payload = None, tipo = "GET", headers = None,auth = None, archivo = None, archivoRespuestas ="./out")

    def iniciarTest(self, event):  # wxGlade: Ventana.<event_handler>
        if self.test.url == None or self.test.url == "":
            with wx.MessageDialog(self, "No introducistes URL","Aviso") as dialog:
                dialog.ShowModal()
                return
        elif self.test.headers == "no Dict":
            with wx.MessageDialog(self, "No introducistes bien el header","Aviso") as dialog:
                dialog.ShowModal()
                return
        else:
            mutex = threading.Semaphore(0)
            thread = threading.Thread(target = self.test.iniciarHilos,args=(mutex,))
            thread.start()
            self.espera(thread)
            mutex.acquire()
            analisis = self.test.crearAnalisis()
            with wx.MessageDialog(self, str(analisis.exitosVSFallos)+" tiempo promedio: "+str(analisis.tiempo_promedio)+"\nCodigos de estado devueltos: "+str(analisis.state_codes_dict) + "\nLos resultados crudos se pueden consular en: " + self.test.archivoRespuestas+".txt" ,"Resultados") as dialog:
                dialog.ShowWindowModal()
            graficque = analisis.dibujar_state_codes()
            print(graficque)
            grafica = plot(graficque)
            grafica.dibujar() 

    def espera(self,hilo):
        if hilo.is_alive() == False:
            with wx.MessageDialog(self,"El test ya termino","Aviso") as finished:
                val = finished.ShowWindowModal()
        else:
            with wx.MessageDialog(self,"El test esta en proceso","Aviso") as espera:
                val = espera.ShowWindowModal()

    def usarTiempo(self, event):
        self.timeChecked = self.chkBxTiempo.IsChecked()
        if self.timeChecked == True:
            self.test.tiempo = self.spnTiempo.GetValue()
        else:
            self.test.tiempo = None
    
    def getDatos(self, event):
        if self.fileDatos == False:
            self.test.setPayload(self.txtDatos.GetLineText(0))
        else:
            self.datos = self.txtDatos.GetLineText(0)

# end of class Ventana

class MyApp(wx.App):
    def OnInit(self):
        self.frame = GUI(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
