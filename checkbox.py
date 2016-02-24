#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   

        pnl = wx.Panel(self)

        cb = wx.CheckBox(pnl, label='Show title', pos=(20, 20))
        cb.SetValue(True)

        cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)

        self.SetSize((250, 170))
        self.SetTitle('wx.CheckBox')
        self.Centre()
        self.Show(True)    

    def ShowOrHideTitle(self, e):
        
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        
        if isChecked:
            self.SetTitle('wx.CheckBox')            
        else: 
            self.SetTitle('')        
                       
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main() 