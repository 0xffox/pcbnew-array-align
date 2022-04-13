import wx
from validators import IntValidator, FloatValidator

class ExFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ExFrame, self).__init__(*args, **kwargs)
        self.panel = wx.Panel(self)

        
class ArrayDialog(wx.Frame): 
   
    def __init__(self, parent, title): 
        super(ArrayDialog, self).__init__(parent, title = title,size = (300,200)) 
        self.rows = 6

             
        self.InitUI() 

        self.Centre() 
        self.Show()      
         
    def InitUI(self): 
        p = wx.Panel(self) 
        gs = wx.GridSizer(cols=2, rows=self.rows, vgap=5, hgap=5) 
		
        # first row
        gs.Add(wx.StaticText(p, label='Element type:'), 0, wx.EXPAND)
        gs.Add(wx.ComboBox(p, choices=['Module', 'Label'], style=wx.CB_DROPDOWN),0,wx.EXPAND) 

        # second row
        gs.Add(wx.StaticText(p, label='Rows:'), 0, wx.EXPAND)
        gs.Add(wx.TextCtrl(p, validator=IntValidator()),0,wx.EXPAND) 

        # third row
        gs.Add(wx.StaticText(p, label='Cols:'), 0, wx.EXPAND)
        gs.Add(wx.TextCtrl(p, validator=IntValidator()),0,wx.EXPAND) 

        # fourth row
        gs.Add(wx.StaticText(p, label='Horisontal interval in mm:'), 0, wx.EXPAND)
        gs.Add(wx.TextCtrl(p, validator=FloatValidator()),0,wx.EXPAND) 

        # fifth row
        gs.Add(wx.StaticText(p, label='Vertical interval in mm:'), 0, wx.EXPAND)
        gs.Add(wx.TextCtrl(p, validator=FloatValidator()),0,wx.EXPAND) 

        p.SetSizer(gs)  

if __name__ == '__main__':

    app = wx.App()
    ef = ArrayDialog(None, 'Align array')
    app.MainLoop()