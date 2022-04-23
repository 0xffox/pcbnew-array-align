import wx
import string

class NumericValidator(wx.Validator):
    def __init__(self, criteria, default = ''):
        super().__init__()
        self.Bind(wx.EVT_TEXT, self.OnText)
        self.val = ''
        self.default = default
        self.criteria = criteria

    def OnText(self, event):
        new_val = event.GetString()
        try:
            self.criteria(new_val)
        except:
            if len(new_val) == 0:
                self.val = self.default
            self.GetWindow().ChangeValue(self.val)
        else:
            self.val = new_val
        event.Skip()

    def Clone(self):
        return self.__class__(self.criteria, self.default)

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def Validate(self, parent):
        return True

