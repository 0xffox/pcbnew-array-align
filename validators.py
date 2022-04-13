import wx
import string

class IntValidator(wx.PyValidator):
    def __init__(self):
        super().__init__()
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def OnChar(self, event):
        print(f'Cur value: {self.GetWindow().GetValue()}')
        # print(f'Event {dir(event)}({type(event)})')
        
        keycode = event.GetKeyCode()
        if keycode < 256:
            if chr(keycode) not in string.digits:
                return
        event.Skip()

    def Clone(self):
        return self.__class__()

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def Validate(self, parent):
        return True


class FloatValidator(wx.PyValidator):
    def __init__(self):
        super().__init__()
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def OnChar(self, event):
        try:
            prev_value = self.GetWindow().GetValue()
            new_char = chr(event.GetKeyCode())
            float(prev_value + new_char)

        except:
            return
        event.Skip()

    def Clone(self):
        return self.__class__()

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def Validate(self, parent):
        return True
