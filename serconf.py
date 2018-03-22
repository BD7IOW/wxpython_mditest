import wx
import serial.tools.list_ports
import configparser
class sercom(wx.Dialog):
    def __init__(self, parent,title):
        wx.Dialog.__init__( self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size( 580, 500 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.Size( 580,500))

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer1.SetMinSize( wx.Size(200, 100 )  )
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1, -1 ), wx.TAB_TRAVERSAL )
        self.m_panel1.SetMinSize( wx.Size( 450, 50 ) )
        self.m_panel1.SetMaxSize( wx.Size( -1, 50 ) )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"串口A", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox1Choices, 0 )
        self.m_comboBox1.SetMaxSize( wx.Size( 60, -1 ) )

        bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"波特率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

        m_comboBox2Choices = [u"2400", u"4800", u"9600", u"115200"]
        self.m_comboBox2 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"9600", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox2Choices, 0 )
        bSizer3.Add( self.m_comboBox2, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"搜索串口", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_staticText101 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"功能码", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )
        bSizer3.Add( self.m_staticText101, 0, wx.ALL, 5 )

        m_comboBox4Choices = [u"03", u"04"]
        self.m_comboBox4 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"04", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox4Choices, 0 )
        self.m_comboBox4.SetMaxSize( wx.Size( 50, -1 ) )

        bSizer3.Add( self.m_comboBox4, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"数据格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

        m_comboBox5Choices = [u"float", u"u16", u"int16"]
        self.m_comboBox5 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"float", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox5Choices, 0 )
        self.m_comboBox5.SetMaxSize( wx.Size( 60, -1 ) )

        bSizer3.Add( self.m_comboBox5, 0, wx.ALL, 5 )

        self.m_panel1.SetSizer( bSizer3 )
        self.m_panel1.Layout()
        bSizer3.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetMinSize( wx.Size( 450, 70 ) )
        self.m_panel2.SetMaxSize( wx.Size( -1, 70 ) )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"串口A设备寄存器地址：", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"0#1#2#3#256", wx.DefaultPosition,
                                        wx.Size( 600, -1 ), 0 )
        bSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel6.SetMinSize( wx.Size( 450, 70 ) )
        self.m_panel6.SetMaxSize( wx.Size( -1, 70 ) )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText12 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"串口A设备寄存器别名：", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.m_textCtrl7 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, u"电量#电流#电压#温度#功率", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        self.m_textCtrl7.SetMinSize( wx.Size( 600, -1 ) )

        bSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

        self.m_panel6.SetSizer( bSizer5 )
        self.m_panel6.Layout()
        bSizer5.Fit( self.m_panel6 )
        bSizer1.Add( self.m_panel6, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel7.SetMinSize( wx.Size( 450, 40 ) )
        self.m_panel7.SetMaxSize( wx.Size( -1, 40 ) )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"串口A设备地址范围：", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 40, -1 ), 0 )
        bSizer6.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"到（<=256）", wx.DefaultPosition, wx.DefaultSize,
                                             0 )
        self.m_staticText14.Wrap( -1 )
        bSizer6.Add( self.m_staticText14, 0, wx.ALL, 5 )

        self.m_textCtrl10 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 40, -1 ), 0 )
        bSizer6.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

        self.m_panel7.SetSizer( bSizer6 )
        self.m_panel7.Layout()
        bSizer6.Fit( self.m_panel7 )
        bSizer1.Add( self.m_panel7, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5 )

        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450, -1 ), wx.TAB_TRAVERSAL )
        self.m_panel8.SetMinSize( wx.Size( 450, 40 ) )
        self.m_panel8.SetMaxSize( wx.Size( -1, 40 ) )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText19 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"串口B（波特率和A组一样）", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer7.Add( self.m_staticText19, 0, wx.ALL, 5 )

        m_comboBox17Choices = []
        self.m_comboBox17 = wx.ComboBox( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox17Choices, 0 )
        self.m_comboBox17.SetMaxSize( wx.Size( 60, -1 ) )

        bSizer7.Add( self.m_comboBox17, 0, wx.ALL, 5 )

        self.m_checkBox1 = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"使能串口B", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        self.m_panel8.SetSizer( bSizer7 )
        self.m_panel8.Layout()
        bSizer1.Add( self.m_panel8, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel9.SetMinSize( wx.Size( 450, 50 ) )
        self.m_panel9.SetMaxSize( wx.Size( -1, 50 ) )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText21 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"串口B设备地址范围：", wx.DefaultPosition,
                                             wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        bSizer8.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.m_textCtrl11 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl11.SetMinSize( wx.Size( 40, -1 ) )

        bSizer8.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

        self.m_staticText24 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"到（<=256）", wx.DefaultPosition, wx.DefaultSize,
                                             0 )
        self.m_staticText24.Wrap( -1 )
        bSizer8.Add( self.m_staticText24, 0, wx.ALL, 5 )

        self.m_textCtrl12 = wx.TextCtrl( self.m_panel9, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl12.SetMinSize( wx.Size( 40, -1 ) )
        self.m_textCtrl12.SetMaxSize( wx.Size( 40, -1 ) )

        bSizer8.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

        self.m_panel9.SetSizer( bSizer8 )
        self.m_panel9.Layout()
        bSizer8.Fit( self.m_panel9 )
        bSizer1.Add( self.m_panel9, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel10.SetMinSize( wx.Size( 450, 40 ) )
        self.m_panel10.SetMaxSize( wx.Size( -1, 40 ) )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self.m_panel10, wx.ID_OK, u"保存设置", wx.Point( -1, 40 ), wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.m_panel10, wx.ID_ANY, u"退出当前界面", wx.Point( -1, 60 ), wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )

        self.m_panel10.SetSizer( bSizer9 )
        self.m_panel10.Layout()
        bSizer9.Fit( self.m_panel10 )
        bSizer1.Add( self.m_panel10, 1, wx.EXPAND | wx.ALL, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        # Connect Events m_comboBox1
        self.m_button1.Bind( wx.EVT_BUTTON, self.openser )
        self.m_button2.Bind( wx.EVT_BUTTON, self.saveconf )
        self.m_button3.Bind( wx.EVT_BUTTON, self.closebtn )
        self.conf = configparser.ConfigParser()
        self.conf.read( "conf.ini" )
        self.m_comboBox1.SetValue(self.conf.get("ser","sera"))
        self.m_comboBox17.SetValue( self.conf.get("ser","serb"))
        self.m_comboBox2.SetValue(self.conf.get("ser","bord"))
        self.m_comboBox4.SetValue(self.conf.get("ser","func"))
        self.m_comboBox5.SetValue(self.conf.get("ser","dfmt"))
        self.m_textCtrl6.SetValue(self.conf.get("ser","regadd"))
        self.m_textCtrl7.SetValue(self.conf.get("ser","name"))
        self.m_textCtrl8.SetValue(self.conf.get("ser","Astart"))
        self.m_textCtrl10.SetValue(self.conf.get("ser","Aend"))
        self.m_textCtrl11.SetValue(self.conf.get("ser","Bstart"))
        self.m_textCtrl12.SetValue(self.conf.get("ser","Bend"))
        if self.conf.getboolean("ser","B_ischeck") is True:
            self.m_checkBox1.SetValue(True)
        elif self.conf.getboolean("ser","B_ischeck") is False:
            self.m_checkBox1.SetValue(False)




    def __del__(self):
        pass


        # Virtual event handlers, overide them in your derived class
        # 获取COM号列表
    def Port_List(self):
        Com_List = []
        port_list = list( serial.tools.list_ports.comports() )
        for port in port_list:
             Com_List.append( port[0] )
        return Com_List


    def closebtn(self, event):
        event.Skip()
        self.Destroy()

    def openser(self, event):
        event.Skip()
        print("AMMM")
        com = self.Port_List()
        self.m_comboBox1.Clear()
        self.m_comboBox1.Append(com)
        self.m_comboBox17.Clear()
        self.m_comboBox17.Append( com )


    def saveconf(self, event):
        event.Skip()



