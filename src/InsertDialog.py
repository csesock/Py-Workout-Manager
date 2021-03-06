## Written by: Chris Sesock
## on March 13th, 2020
##
import sqlite3, wx

class MyDialog(wx.Dialog):

    def __init__(self, title):
        wx.Dialog.__init__(self, None, title=title, size=(320, 750))

        con = sqlite3.connect('workout.sqlite')
        cur = con.cursor()

        self.date = wx.TextCtrl(self, -1, pos = (50, 40))
        wx.StaticText(self, -1, 'Date', pos = (180, 40))
        self.pushups = wx.TextCtrl(self, -1, pos = (50, 90))
        wx.StaticText(self, -1, 'Pushups', pos = (180, 90))
        self.chest_press = wx.TextCtrl(self, -1, pos = (50, 130))
        wx.StaticText(self, -1, 'Chest Press', pos = (180, 130))
        self.squats = wx.TextCtrl(self, -1, pos = (50, 170))
        wx.StaticText(self, -1, 'Squats', pos = (180, 170))
        self.lunges = wx.TextCtrl(self, -1, pos = (50, 210))
        wx.StaticText(self, -1, 'Lunges', pos = (180, 210))
        self.vertical_press = wx.TextCtrl(self, -1, pos = (50, 250))
        wx.StaticText(self, -1, 'Vertical Press', pos = (180, 250))
        self.pullups = wx.TextCtrl(self, -1, pos = (50, 290))
        wx.StaticText(self, -1, 'Pullups', pos = (180, 290))
        self.dumbell_row = wx.TextCtrl(self, -1, pos = (50, 330))
        wx.StaticText(self, -1, 'Dumbell Rows', pos = (180, 330))
        self.bicep_curls = wx.TextCtrl(self, -1, pos = (50, 370))
        wx.StaticText(self, -1, 'Bicep Curls', pos = (180, 370))
        self.preacher_curls = wx.TextCtrl(self, -1, pos = (50, 410))
        wx.StaticText(self, -1, 'Hammer Curls', pos = (180, 410))
        self.tricep_lifts = wx.TextCtrl(self, -1, pos = (50, 450))
        wx.StaticText(self, -1, 'Tricep Lifts', pos = (180, 450))
        self.tricep_pushups = wx.TextCtrl(self, -1, pos = (50, 490))
        wx.StaticText(self, -1, 'Tricep Pushups', pos = (180, 490))
        self.situps = wx.TextCtrl(self, -1, pos = (50, 530))
        wx.StaticText(self, -1, 'Situps', pos = (180, 530))
        self.crunches = wx.TextCtrl(self, -1, pos = (50, 570))
        wx.StaticText(self, -1, 'Crunches', pos = (180, 570))
        self.planks = wx.TextCtrl(self, -1, pos = (50, 610))
        wx.StaticText(self, -1, 'Planks', pos = (180, 610))

        self.pushups.SetValue('0')
        self.chest_press.SetValue('0')
        self.squats.SetValue('0')
        self.lunges.SetValue('0')
        self.vertical_press.SetValue('0')
        self.pullups.SetValue('0')
        self.dumbell_row.SetValue('0')
        self.bicep_curls.SetValue('0')
        self.preacher_curls.SetValue('0')
        self.tricep_lifts.SetValue('0')
        self.tricep_pushups.SetValue('0')
        self.situps.SetValue('0')
        self.crunches.SetValue('0')
        self.planks.SetValue('0')

        ok_button = wx.Button(self, id=wx.ID_OK, pos=(50, 670))
