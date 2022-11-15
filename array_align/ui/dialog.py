import wx
# from .validators import IntValidator, FloatValidator
from .validators import NumericValidator

        
class ArrayDialog(wx.Dialog): 
   
    def __init__(self, parent=None, title='Align array selected', user_units='mm'): 
        super(ArrayDialog, self).__init__(parent, title = title,size = (300,300)) 
        self.rows = 6
        self.elems = dict()
        self.user_units = user_units
             
        self.InitUI() 

        # self.Centre() 
        # self.Show()      

    def getValues(self):
        return { e: self.elems[e].GetValue() if e.startswith('tx_') else self.elems[e].GetSelection() for e in self.elems }
         
    def InitUI(self): 
        p = wx.Panel(self) 
        gs = wx.GridSizer(cols=2, rows=self.rows, vgap=5, hgap=5) 
        true_center = wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL
        is_int = lambda x: int(x)
        is_float = lambda x: float(x)
		
        # first row
        gs.Add(wx.StaticText(p, label='Element type:'), 0, true_center)
        # gs.Add(wx.ComboBox(p, choices=['Module', 'Label'], style=wx.CB_DROPDOWN),0,wx.EXPAND) 
        self.elems['ch_elem_type'] = wx.Choice(
            p, 
            choices=[
                'Footprints', 
                'Drawings',
                'Pads',
                'Tracks'
            ], 
            style=wx.CB_DROPDOWN
        )
        self.elems['ch_elem_type'].SetSelection(0)
        gs.Add(self.elems['ch_elem_type'],0,wx.EXPAND) 

        # second row
        gs.Add(wx.StaticText(p, label='Rows:'), 0, true_center)
        self.elems['tx_rows'] = wx.TextCtrl(p, validator=NumericValidator(is_int ))
        gs.Add(self.elems['tx_rows'],0,wx.EXPAND) 

        # third row
        gs.Add(wx.StaticText(p, label='Cols:'), 0, true_center)
        self.elems['tx_cols'] = wx.TextCtrl(p, validator=NumericValidator(is_int ))
        gs.Add(self.elems['tx_cols'],0,wx.EXPAND) 

        # fourth row
        gs.Add(wx.StaticText(p, label=f'Horisontal interval in {self.user_units}:'), 0, true_center)
        self.elems['tx_h_gap'] = wx.TextCtrl(p, validator=NumericValidator(is_float, '0'))
        gs.Add(self.elems['tx_h_gap'],0,wx.EXPAND) 

        # fifth row
        gs.Add(wx.StaticText(p, label=f'Vertical interval in {self.user_units}:'), 0, true_center)
        self.elems['tx_v_gap'] = wx.TextCtrl(p, validator=NumericValidator(is_float, '0'))
        gs.Add(self.elems['tx_v_gap'],0,wx.EXPAND) 

        # sixth row
        gs.Add(wx.StaticText(p, label='Align result:'), 0, true_center)
        # gs.Add(wx.ComboBox(p, choices=['Module', 'Label'], style=wx.CB_DROPDOWN),0,wx.EXPAND) 
        self.elems['ch_origin_type'] = wx.Choice(
            p, 
            choices=[
                'Center', 
                'Top Left', 
                'Bottom Left', 
                'Top Right', 
                'Bottom Right'
            ], 
            style=wx.CB_DROPDOWN
        )
        self.elems['ch_origin_type'].SetSelection(0)
        gs.Add(self.elems['ch_origin_type'],0,wx.EXPAND) 

        # seventh row
        ok_button, cancel_button = wx.Button(p, wx.ID_OK, 'Ok'), wx.Button(p, wx.ID_CANCEL, 'Cancel')
        gs.Add(ok_button, 0, wx.ALIGN_CENTER_HORIZONTAL) 
        gs.Add(cancel_button, 0, wx.ALIGN_CENTER_HORIZONTAL) 

        p.SetSizer(gs)  


if __name__ == '__main__':

    app = wx.App()
    ef = ArrayDialog(None, 'Align array')
    app.MainLoop()
