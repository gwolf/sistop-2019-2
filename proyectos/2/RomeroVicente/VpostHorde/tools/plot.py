import wx
from wx.lib.plot import PlotCanvas
class plot(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self, grafica):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Grafica de resultados')
        panel = wx.Panel(self, wx.ID_ANY)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.canvas = PlotCanvas(panel)
        self.canvas.SetShowScrollbars(True)
        self.canvas.SetEnableZoom(True)
        self.canvas.Draw(grafica)
        toggleGrid = wx.CheckBox(panel, label="Ver cuadricula")
        toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Ver leyenda")
        toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)
        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 5)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 5)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)
    def onToggleGrid(self, event):
        self.canvas.Reset()
        self.canvas.SetEnableGrid(event.IsChecked())
    
    def onToggleLegend(self, event):
        self.canvas.SetEnableLegend(event.IsChecked())
    def dibujar(self):
        app = wx.App(False)
 
        self.Show()
        app.MainLoop()