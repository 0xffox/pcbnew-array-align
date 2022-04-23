import pcbnew
import os
from .ui.dialog import ArrayDialog
import wx
from functools import reduce


class ArrayAlignAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Array Align"
        self.category = "align"
        self.description = "Align selected elements in the grid"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

    def Run(self):
        # The entry function of the plugin that is executed on user action

        user_units = pcbnew.GetUserUnits()
        fromUnits = lambda u: pcbnew.FromMM(u) if user_units else pcbnew.FromMils(u)
        dlg = ArrayDialog(user_units = 'mm' if user_units else 'minch')
        
        dlg.Center()
        if dlg.ShowModal() == wx.ID_OK:
            params = dlg.getValues()
            self._alignElems(
                selection_type=params['ch_elem_type'],
                origin_type=params['ch_origin_type'],
                rows=int(params['tx_rows']),
                cols=int(params['tx_cols']),
                hgap=fromUnits(float(params['tx_h_gap'])),
                vgap=fromUnits(float(params['tx_v_gap']))
            )
        dlg.Destroy()


    def _getOrigins(self, elems, new_width, new_height):
        center = reduce(lambda x, y: x + y.GetPosition(), elems, pcbnew.wxPoint(0, 0))
        center = pcbnew.wxPoint(center.x/len(elems), center.y/len(elems))
        left = min( m.GetPosition().x for m in elems )
        right = max( m.GetPosition().x for m in elems )
        top = min( m.GetPosition().y for m in elems )
        bot = max( m.GetPosition().y for m in elems )

        height, width = abs(top - bot), abs(right - left)
        return {
            0: pcbnew.wxPoint(    # center mass
                    left + width/2 - new_width/2, 
                    top + height/2 - new_height/2
                ),
            1: pcbnew.wxPoint(    # top left
                    left, 
                    top
                ),
            2: pcbnew.wxPoint(    # bottom left
                    left, 
                    top + height - new_height
                ),
            3: pcbnew.wxPoint(    # top right
                    left + width - new_width, 
                    top
                ),
            4: pcbnew.wxPoint(    # bottom right
                    left + width - new_width, 
                    top + height - new_height
                ),
        }

    
    def _sortElems(self, elems, rows, cols):
        elems = sorted(elems, key=lambda x: x.GetPosition().y)
        for r in range(rows):
            start, end = r*cols, (r + 1)*cols
            elems[start:end] = sorted(elems[start:end], key=lambda x: x.GetPosition().x)
        return elems


    def _alignElems(self, selection_type=0, origin_type=1, rows=1, cols=1, hgap=0.0, vgap=0.0):
        board = pcbnew.GetBoard()
        selection_types = {
            0: board.GetModules,
            1: board.GetDrawings,
            2: board.GetPads,
            3: board.GetTracks,
        }
        selected = self._sortElems(
            [ m for m in selection_types[selection_type]() if m.IsSelected() ],
            rows, cols
        )
        if len(selected) > 0:
            origins = self._getOrigins(selected, (cols-1)*hgap, (rows-1)*vgap)
            for r in range(rows):
                for c in range(cols):
                    idx = r*cols + c
                    if idx < len(selected):
                        selected[idx].SetPosition(pcbnew.wxPoint(c*hgap, r*vgap) + origins[origin_type])

            pcbnew.Refresh()

