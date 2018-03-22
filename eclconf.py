# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import configparser
import re
###########################################################################
## Class MyDialog1
###########################################################################

class exlconf( wx.Dialog ):
    def __init__(self, parent):
        wx.Dialog.__init__( self, parent, id=wx.ID_ANY, title=u"显示&报表", pos=wx.DefaultPosition,
                            size=wx.Size( 586, 571 ), style=wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetMaxSize( wx.Size( -1, 230 ) )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"显示设置" ), wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"使能显示设置", wx.DefaultPosition,
                                        wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"{title1,4,6,7,8,3}\n{title2,2,5,9}",
                                        wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.TE_MULTILINE )
        self.m_textCtrl2.SetMinSize( wx.Size( 600, 300 ) )

        sbSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_panel2.SetSizer( sbSizer1 )
        self.m_panel2.Layout()
        sbSizer1.Fit( self.m_panel2 )
        bSizer2.Add( self.m_panel2, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel3.SetMinSize( wx.Size( -1, 60 ) )
        self.m_panel3.SetMaxSize( wx.Size( -1, 100 ) )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"报表设置" ), wx.HORIZONTAL )

        self.m_checkBox2 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"每天一报", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        sbSizer2.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        self.m_spinCtrl1 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 0 )
        self.m_spinCtrl1.SetMaxSize( wx.Size( 50, -1 ) )

        sbSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

        self.m_staticText1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"时", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        sbSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u" ", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        sbSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"报表项目", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        sbSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

        m_checkList2Choices = [u"1", u"2", u"3", u"4"]
        self.m_checkList2 = wx.CheckListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             m_checkList2Choices, wx.LB_ALWAYS_SB | wx.LB_HSCROLL )
        sbSizer2.Add( self.m_checkList2, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"       ", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        sbSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"每隔", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        sbSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        self.m_textCtrl3.SetMaxSize( wx.Size( 30, -1 ) )

        sbSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"行插入表头", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        sbSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_panel3.SetSizer( sbSizer2 )
        self.m_panel3.Layout()
        sbSizer2.Fit( self.m_panel3 )
        bSizer2.Add( self.m_panel3, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.SetMinSize( wx.Size( -1, 100 ) )
        self.m_panel4.SetMaxSize( wx.Size( -1, 100 ) )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        self.m_checkBox5 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"每小时一报（正点）", wx.DefaultPosition,
                                        wx.DefaultSize, 0 )
        sbSizer3.Add( self.m_checkBox5, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"报表项目", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        sbSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

        m_checkList4Choices = [u"1", u"2", u"3", u"4"]
        self.m_checkList4 = wx.CheckListBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             m_checkList4Choices, wx.LB_ALWAYS_SB | wx.LB_HSCROLL )
        sbSizer3.Add( self.m_checkList4, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"       ", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        sbSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"每隔", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        sbSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        self.m_textCtrl4.SetMaxSize( wx.Size( 30, -1 ) )

        sbSizer3.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"行插入表头", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        sbSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_panel4.SetSizer( sbSizer3 )
        self.m_panel4.Layout()
        sbSizer3.Fit( self.m_panel4 )
        bSizer2.Add( self.m_panel4, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        self.m_button4 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_OK, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer4.Add( self.m_button4, 0, wx.ALL, 5 )

        self.m_button5 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"退出界面", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer4.Add( self.m_button5, 0, wx.ALL, 5 )

        self.m_panel5.SetSizer( sbSizer4 )
        self.m_panel5.Layout()
        sbSizer4.Fit( self.m_panel5 )
        bSizer2.Add( self.m_panel5, 1, wx.EXPAND | wx.ALL, 5 )

        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button5.Bind( wx.EVT_BUTTON, self.closebtn )
        self.conf = configparser.ConfigParser()
        self.conf.read( "conf.ini" )
        if self.conf.getboolean("excel","disp_set"):
            self.m_checkBox1.SetValue(True)
        elif self.conf.getboolean("excel","disp_set") is False:
            self.m_checkBox1.SetValue( False )
        self.m_textCtrl2.Clear()
        self.m_textCtrl2.write(self.conf.get("excel","disp_fmt"))
        if self.conf.getboolean("excel","each_day_set"):
            self.m_checkBox2.SetValue(True)
        elif self.conf.getboolean("excel","each_day_set") is False:
            self.m_checkBox2.SetValue( False )
        self.m_spinCtrl1.SetValue(self.conf.getint("excel","each_day"))
        # self.m_textCtrl3.SetValue(80)
        self.m_textCtrl3.SetValue(self.conf.get("excel","excel_day_fmt"))
        name = self.conf.get("ser","name")
        namelist=name.split('#')
        self.m_checkList2.Set(namelist)
        self.m_checkList4.Set(namelist)#m_checkBox5
        li=self.conf.get("excel","each_list")
        lis = self.conf.get( "excel", "each_ho_list" )
        # for i in li[1:-1]:
            # #SetChecked([])
        i=re.findall( r"\d", li )
        q = [int(x) for x in i]
        self.m_checkList2.SetCheckedItems(q)
        ib = re.findall( r"\d", lis )
        qb = [int( x ) for x in ib]
        self.m_checkList4.SetCheckedItems( qb )
        if self.conf.getboolean("excel","each_ho"):
            self.m_checkBox5.SetValue(True)
        elif self.conf.getboolean("excel","each_ho") is False:
            self.m_checkBox5.SetValue( False )
        self.m_textCtrl4.SetValue(self.conf.get("excel","excel_h_fmt"))
    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def closebtn(self, event):
        event.Skip()
        self.Destroy()


