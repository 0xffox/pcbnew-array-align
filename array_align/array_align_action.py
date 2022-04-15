import pcbnew
import os
from .ui.dialog import ArrayDialog
import wx

class ArrayAlignAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Array Align"
        self.category = "align"
        self.description = "Align element in the grid"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

    def Run(self):
        # The entry function of the plugin that is executed on user action

        dlg = ArrayDialog()
        
        dlg.Center()
        if dlg.ShowModal() == wx.ID_OK:
            print("Hello World")
        dlg.Destroy()

    # def __del__(self):
    #     self.dialog.Destroy()
