import wx
from .validators import IntValidator, FloatValidator

        
class ArrayDialog(wx.Dialog): 
   
    def __init__(self, parent=None, title='Align array'): 
        super(ArrayDialog, self).__init__(parent, title = title,size = (300,300)) 
        self.rows = 6
             
        self.InitUI() 

        # self.Centre() 
        # self.Show()      
         
    def InitUI(self): 
        p = wx.Panel(self) 
        gs = wx.GridSizer(cols=2, rows=self.rows, vgap=5, hgap=5) 
        true_center = wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL
		
        # first row
        gs.Add(wx.StaticText(p, label='Element type:'), 0, true_center)
        # gs.Add(wx.ComboBox(p, choices=['Module', 'Label'], style=wx.CB_DROPDOWN),0,wx.EXPAND) 
        choice = wx.Choice(p, choices=['Module', 'Label'], style=wx.CB_DROPDOWN)
        choice.SetSelection(0)
        gs.Add(choice,0,wx.EXPAND) 

        # second row
        gs.Add(wx.StaticText(p, label='Rows:'), 0, true_center)
        gs.Add(wx.TextCtrl(p, validator=IntValidator()),0,wx.EXPAND) 

        # third row
        gs.Add(wx.StaticText(p, label='Cols:'), 0, true_center)
        gs.Add(wx.TextCtrl(p, validator=IntValidator()),0,wx.EXPAND) 

        # fourth row
        gs.Add(wx.StaticText(p, label='Horisontal interval in mm:'), 0, true_center)
        gs.Add(wx.TextCtrl(p, validator=FloatValidator()),0,wx.EXPAND) 

        # fifth row
        gs.Add(wx.StaticText(p, label='Vertical interval in mm:'), 0, true_center)
        gs.Add(wx.TextCtrl(p, validator=FloatValidator()),0,wx.EXPAND) 

        # sixth row
        gs.Add(wx.StaticText(p, label='Vertical interval in mm:'), 0, true_center)
        gs.Add(wx.TextCtrl(p, validator=FloatValidator()),0,wx.EXPAND) 

        # seventh row
        ok_button, cancel_button = wx.Button(p, wx.ID_OK, 'Ok'), wx.Button(p, wx.ID_CANCEL, 'Cancel')
        gs.Add(ok_button, 0, wx.ALIGN_CENTER_HORIZONTAL) 
        gs.Add(cancel_button, 0, wx.ALIGN_CENTER_HORIZONTAL) 

        p.SetSizer(gs)  


if __name__ == '__main__':

    app = wx.App()
    ef = ArrayDialog(None, 'Align array')
    app.MainLoop()
