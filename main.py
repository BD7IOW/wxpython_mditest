import wx
import re
import wx.grid as grid
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import configparser
from serconf import sercom
from eclconf import exlconf
# print instrument.read_register(289, 1)  # Remember to use print() for Python3

import time
import threading
from queue import Queue
from wx.lib.pubsub import pub
class serThread(threading.Thread):
    def __init__(self,eve,quent,quent1,conf):
        super( serThread, self).__init__()
        self.data=quent
        self.data1 = quent1
        self.conf=conf
        self.com=""
        self.com1=""
        self.fun=0
        self.bard=9600

        self.fmt=""
        self.regs=1
        self.rege=1
        self.devs=1
        self.deve=1
        self.bsers=1
        self.bsere=1
        self.err=False
        self.timout1=False
        self.timout2 = False
        self.cnt = 0
        self.cnt1 = 0
        self.eve=eve
        self.dat_init()
    def dat_init(self):
        regas = self.conf.get( "ser", "regadd" )
        reg = regas.split( '#' )
        regnum = [int( x ) for x in reg]
        fmt = ">"
        if self.conf.get( "ser", "dfmt" ) == "float":
            for i in range( 5 ):
                fmt = fmt + "f"
        elif self.conf.get( "ser", "dfmt" ) == "int16":
            for i in range( max( regnum ) ):
                fmt = fmt + "h"
        elif self.conf.get( "ser", "dfmt" ) == "u16":
            for i in range( max( regnum ) ):
                fmt = fmt + "H"
        self.fmt = fmt
        # self.logger = modbus_tk.utils.create_logger( "console" )
        self.com = self.conf.get( "ser", "sera" )
        self.com1 = self.conf.get( "ser", "serb" )
        self.bard = self.conf.getint( "ser", "bord" )
        if self.conf.get( "ser", "func" ) == "03":
           self.fun=cst.READ_HOLDING_REGISTERS
        elif self.conf.get( "ser", "func" ) == "04":
            self.fun=cst.READ_INPUT_REGISTERS
        self.regs = min( regnum )
        self.rege =max( regnum )
        self.devs = self.conf.getint( "ser", "Astart" )
        self.deve = self.conf.getint( "ser", "Aend" )
        self.bsers = self.conf.getint("ser", "Bstart" )
        self.bsere = self.conf.getint( "ser", "Bend" )
        try:
            # Connect to the slave
            self.master = modbus_rtu.RtuMaster(
                serial.Serial( port=self.com, baudrate=self.bard, bytesize=8, parity='N', stopbits=1, xonxoff=0 )
            )
            self.master.set_timeout( 0.2 )
            self.master.set_verbose( True )
            # self.logger.info( "connected" )

        except :
            self.dlg = wx.MessageDialog( None, u"Modbus串口打开失败！", u"Warning", wx.YES_NO | wx.ICON_WARNING )
            if self.dlg.ShowModal() == wx.ID_YES or self.dlg.ShowModal() == wx.ID_NO:
                self.dlg.Destroy()

            # if dlg.ShowModal() == wx.ID_YES:
            #    dlg.Destroy()
            # self.logg "%s- Code=%d", exc, exc.get_exception_code() )
        self.serBiScheck = self.conf.getboolean( "ser", "B_ischeck" )
        if self.serBiScheck:
            try:
                # Connect to the slave
                self.master1 = modbus_rtu.RtuMaster(
                    serial.Serial( port=self.com1, baudrate=self.bard, bytesize=8, parity='N', stopbits=1, xonxoff=0 )
                )
                self.master1.set_timeout( 1.0 )
                self.master1.set_verbose( True )
                # self.logger.info( "connected" )

            except:
                self.dlg = wx.MessageDialog( None, u"Modbus串口打开失败！", u"Warning", wx.YES_NO | wx.ICON_WARNING )
                if self.dlg.ShowModal() == wx.ID_YES or self.dlg.ShowModal() == wx.ID_NO:
                    self.dlg.Destroy()
                # self.err = True

        # self.start()
    def run(self):
      while True:
        if not self.eve.is_set():
            self.eve.wait()
        try:
           if self.data1.get(block=False)=="update":
               self.master.__del__()
               if self.serBiScheck:
                  self.master1.__del__()
               self.dat_init()
        except:pass
        if self.err is False:#self.devs+self.cnt
           try:
             dat = self.master.execute( self.devs+self.cnt, self.fun, self.regs, self.rege, data_format=self.fmt )
           except: self.timout1=True
               # self.dlg = wx.MessageDialog( None, u"Modbus读数据超时！", u"Warning", wx.YES_NO | wx.ICON_WARNING )
               # if self.dlg.ShowModal() == wx.ID_YES or self.dlg.ShowModal() == wx.ID_NO:
               #     self.dlg.Destroy()
           if  self.timout1:
               num=(self.cnt+self.devs,)
               self.data.put(num+())
               self.timout1 = False
           else:
               num = (self.cnt + self.devs,)
               self.data.put( num + dat )
           # dat=
           # print(num+dat)
           # wx.CallAfter(pub.sendMessage,'update', msg=dat)
           if self.serBiScheck:
               try:
                   dat1 = self.master1.execute( self.bsers + self.cnt1, self.fun, self.regs, self.rege,
                                              data_format=self.fmt )
               except:self.timout2 = True
                   # self.dlg = wx.MessageDialog( None, u"Modbus读数据超时！", u"Warning", wx.YES_NO | wx.ICON_WARNING )
                   # if self.dlg.ShowModal() == wx.ID_YES or self.dlg.ShowModal() == wx.ID_NO:
                   #     self.dlg.Destroy()
               if self.timout2:
                  num1 = (self.cnt1 + self.bsers+self.deve,)
                  self.data.put( num1 + () )
                  self.timout2 = False
               else:
                   num1 = (self.cnt1 + self.bsers + self.deve,)
                   self.data.put( num1 + dat1 )
               # dat1=[]
               self.cnt1 += 1
               if self.cnt1 + self.bsers > self.bsere:
                   self.cnt1 = 0
           self.cnt+=1
           if self.cnt+self.devs > self.deve:
               self.cnt=0

        time.sleep(0.01)
class ser1Thread(threading.Thread):
    def __init__(self,eve,quent,conf):
        super( ser1Thread,self ).__init__()
        self.data=quent
        self.conf=conf
        self.data_temp=[]
        self.devBischeck=self.conf.getboolean("ser","B_ischeck")
        self.regas = int(self.conf.get( "ser", "Astart"))
        self.regae = int(self.conf.get( "ser", "Aend"))
        self.Anum=self.regae-self.regas+1
        self.cnt=0
        self.regbs = int( self.conf.get( "ser", "Bstart" ) )
        self.regbe = int( self.conf.get( "ser", "Bend" ) )
        self.Bnum = self.regbe - self.regbs + 1
        if self.devBischeck:
           self.cnt= self.Anum+self.Bnum
        else: self.cnt= self.Anum
        self.num=0
        # self.start()
        self.eve=eve
    def run(self):
      while True:
        if not self.eve.is_set():
            self.eve.wait()
        #     break
        val = self.data.get()
        self.data_temp.append(list(val))
        self.num+=1
        if self.num>=self.cnt:
            self.num=0
            wx.CallAfter( pub.sendMessage,'update', msg=self.data_temp )
            self.data_temp=[]

        time.sleep(0.01)


class MainWindow(wx.Frame):
    def __init__(self, parent,title):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size( 652, 490 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )
        self.modbus_cnt = False#用于线程更新配置
        self.modbus_run = False
        self.swit = 0
        self.localtime=""
        self.redad=[]
        self.dis_fmt=[]
        self.dis_fmt_name=[]
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel6.SetMinSize( wx.Size( -1, 30 ) )
        self.m_panel6.SetMaxSize( wx.Size( -1, 30 ) )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText12 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"数据采集", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont(
            wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
        self.m_staticText12.SetMinSize( wx.Size( 300, 30 ) )

        bSizer6.Add( self.m_staticText12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button8 = wx.Button( self.m_panel6, wx.ID_ANY, u"运行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button8, 0, wx.ALL, 5 )

        self.m_button9 = wx.Button( self.m_panel6, wx.ID_ANY, u"切换", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button9, 0, wx.ALL, 5 )

        # self.m_button10 = wx.Button( self.m_panel6, wx.ID_ANY, u"切换", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bSizer6.Add( self.m_button10, 0, wx.ALL, 5 )

        self.m_panel6.SetSizer( bSizer6 )
        self.m_panel6.Layout()
        bSizer6.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 1, wx.EXPAND | wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid2 = wx.grid.Grid( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 256, 20 )
        # self.m_grid2.EnableEditing( True )
        # self.m_grid2.EnableGridLines( True )
        # self.m_grid2.EnableDragGridSize( False )
        # self.m_grid2.SetMargins( 0, 0 )

        self.m_grid2.SetDefaultColSize( 60 )
        self.m_grid2.SetDefaultRowSize( 20 )
        self.m_grid2.SetDefaultCellOverflow(False)
        # Columns

        # self.m_grid2.SetColSize( 0, 58 )
        # self.m_grid2.SetColSize( 1, 30 )
        # self.m_grid2.SetColSize( 2, 30 )
        # self.m_grid2.SetColSize( 3, 31 )
        # self.m_grid2.SetColSize( 4, 29 )
        # self.m_grid2.AutoSizeColumns()
        # self.m_grid2.EnableDragColMove( False )
        # self.m_grid2.EnableDragColSize( True )
        # self.m_grid2.SetColLabelSize( 30 )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        # self.m_grid2.AutoSizeRows()
        # self.m_grid2.EnableDragRowSize( True )
        # self.m_grid2.SetRowLabelSize( 30 )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        bSizer7.Add( self.m_grid2, 0, wx.EXPAND, 5 )

        self.m_panel7.SetSizer( bSizer7 )
        self.m_panel7.Layout()
        bSizer7.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 1, wx.EXPAND | wx.ALL, 5 )

        self.SetSizer( bSizer5 )
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_statusBar2.SetFieldsCount( 2 )
        self.m_statusBar2.SetStatusText( u"软件状态：" +"欢迎使用", 0 )
        self.localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.m_statusBar2.SetStatusText(  self.localtime,1)


        self.m_menubar3 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"通信参数设置", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"报表参数设置", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"通信", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem3 )

        self.m_menubar3.Append( self.m_menu1, u"选项" )

        self.SetMenuBar( self.m_menubar3 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button8.Bind( wx.EVT_BUTTON, self.run )
        self.m_button9.Bind( wx.EVT_BUTTON, self.switch )
        # self.m_button10.Bind( wx.EVT_BUTTON, self.switch )
        self.Bind( wx.EVT_MENU, self.serconf, id=self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.exlconf, id=self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.communication, id=self.m_menuItem3.GetId() )
        self.conf = configparser.ConfigParser()
        self.conf.read( "conf.ini" )

        # 建立各种事件
        self.ser_clc_event = threading.Event()#数据采集线程事件
        self.ser_event = threading.Event()#数据采集线程与主线程桥梁线程事件
        #数据缓存
        self.dis_dat=[[],]
        self.timer = wx.Timer( self )  # 创建定时器
        self.Bind( wx.EVT_TIMER, self.OnTimer, self.timer )  # 绑定一个定时器事件
        self.timer.Start( 500 )  # 设定时间间隔为1000毫秒,并启动定时器
        self.queue = Queue()  # 队列实例化
        self.queue1 = Queue()  # 队列实例化
        self.drawcollable()
        self.update_redad()
        self.dis_fmt_update()
    def OnTimer(self, evt):  # 显示时间事件处理函数
        self.localtime = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )
        self.m_statusBar2.SetStatusText( self.localtime, 1 )
    def serconf(self,event):
        print("AAA")
        dig = sercom( self, u'ModBus配置' )
        if dig.ShowModal()== wx.ID_OK:

            try:
               print( self.conf.items( "ser" ) )
            except:
                print("cant read conf.ini")
            co=self.conf.sections()
            if "ser" not in co:
                self.conf.add_section("ser")

            self.conf.set("ser","sera",dig.m_comboBox1.GetValue())#串口a
            self.conf.set("ser","bord",dig.m_comboBox2.GetValue())#波特率
            self.conf.set("ser","func",dig.m_comboBox4.GetValue())#功能码
            self.conf.set("ser","dfmt",dig.m_comboBox5.GetValue())#数据格式
            self.conf.set("ser","regadd",dig.m_textCtrl6.GetValue())#寄存器地址
            self.conf.set("ser","name",dig.m_textCtrl7.GetValue())#别名
            self.conf.set("ser","Astart",dig.m_textCtrl8.GetValue())#A起始
            self.conf.set("ser","Aend",dig.m_textCtrl10.GetValue())#A尾
            self.conf.set( "ser","serb", dig.m_comboBox17.GetValue())  # 串口b
            self.conf.set("ser","Bstart",dig.m_textCtrl11.GetValue())#B起
            self.conf.set("ser","Bend",dig.m_textCtrl12.GetValue())#B尾
            self.conf.set("ser","B_ischeck",str(dig.m_checkBox1.GetValue()))#checkbox
            print(u"保存参数")
            print(self.conf.items("ser"))

            self.conf.write(open("conf.ini","w"))
            dig.Destroy()
            self.drawcollable()
            self.update_redad()


    def exlconf(self,event):
        di = exlconf(self)
        if di.ShowModal() == wx.ID_OK:
            try:
                print( self.conf.items( "excel" ) )
            except:
                print( "cant read conf.ini" )
            co = self.conf.sections()
            if "excel" not in co:
                self.conf.add_section( "excel" )
            self.conf.set( "excel", "disp_set",str(di.m_checkBox1.GetValue()))
            self.conf.set("excel","disp_fmt",di.m_textCtrl2.GetValue())
            self.conf.set("excel","each_day_set",str(di.m_checkBox2.GetValue()))
            self.conf.set("excel","each_day",str(di.m_spinCtrl1.GetValue()))
            self.conf.set("excel","each_list",str(di.m_checkList2.GetChecked()))
            self.conf.set("excel","excel_day_fmt",str(di.m_textCtrl3.GetValue()))
            self.conf.set("excel","each_ho",str(di.m_checkBox5.GetValue()))
            self.conf.set("excel","each_ho_list",str(di.m_checkList4.GetChecked()))
            self.conf.set("excel","excel_h_fmt",str(di.m_textCtrl4.GetValue()))
            print( u"保存参数" )
            print( self.conf.items( "excel" ) )
            self.conf.write( open( "conf.ini", "w" ) )

            di.Destroy()
        self.dis_fmt_update()
    def drawcollable(self):
        r=2
        colt1 = self.conf.get( "ser", "name" )
        colt = colt1.split( '#' )
        self.m_grid2.SetColLabelValue( 0, u"设备名称" )
        self.m_grid2.SetColLabelValue( 1, u"设备ID" )
        for i in colt:
          self.m_grid2.SetColLabelValue(r,i)
          r+=1
    def update_redad(self):
        #
        ad=self.conf.get("ser","regadd" )
        self.redad=ad.split('#')
        self.redad = [int(x) for x in self.redad]

    def data_filter(self,s):
        out=[0, ]
        # t=1
        # print( self.redad )
        out[0]=s[0]

        try:
           for i in self.redad:
               out.append(s[i])
               # print(i)
               # t+=1
        except:pass
        return out
    def update_oneLine(self,d):
        # self.m_grid2.SetCellValue( i,0, self.dev[i][0] )
        t=1
        for i in d:
            self.m_grid2.SetCellValue(d[0]-1 , t, str(i) )
            t+=1
    def data_extraction(self,c,s):#根据分类进行数据抽取
        m=[]
        for i in s:
            if i[0] in c:
                m.append(i)
        return m

    def fmt_dis_update(self,d,r):
        t = 1
        for i in d:
            self.m_grid2.SetCellValue( 0+r, t, str( i ) )
            t += 1
    def ser_data_update(self,msg=None):
        print(msg)
        # devnum=0

        # if self.conf.getboolean("ser","B_ischeck"):
        #     devnum= self.conf.getint("ser","Aend")-self.conf.getint("ser","Astart")+2+self.conf.getint("ser","Bend")-self.conf.getint("ser","Bstart")
        # else: devnum= self.conf.getint("ser","Aend")-self.conf.getint("ser","Astart")+1
        if self.conf.getboolean("excel","disp_set") is False:
            self.m_staticText12.SetLabelText( "数据采集" )
            for i in msg:
                 # print(self.data_filter(i))
                 self.update_oneLine(self.data_filter(i))
            # self.m_grid2.SetCellValue( 1, 0, "222")
            # self.m_grid2.CreateGrid(devnum, 10 )
            # pass
        else:
            dis_ord=self.dis_fmt[self.swit]#已分类的地址
            indata = self.data_extraction(dis_ord, msg )
            print(indata)
            r=0
            for i in indata:
                self.fmt_dis_update( self.data_filter(i),r )
                r+=1


    def run(self, event):
        event.Skip()


        # print( max(regnum))
        if self.modbus_run is not True:
            self.modbus_run=True
            self.m_button8.SetLabel(u"停止")
            self.m_statusBar2.SetStatusText( u"软件状态：" + "运行中", 0 )
            #self,quent,conf,com,com1,bard,func,fmt,regs,rege,devs,deve,bsers,bsere


            if self.modbus_cnt is not True:
                self.serial1Thread = serThread(self.ser_clc_event,self.queue,self.queue1,self.conf)#self.conf.getint( "ser", "bord" )self.conf.get("ser","bord")self.conf.get("ser","serb")

                self.clcThread = ser1Thread(self.ser_event,self.queue,self.conf)
                self.serial1Thread.setDaemon( True )
                self.clcThread.setDaemon( True )
                self.serial1Thread.start()
                self.clcThread.start()
            if self.modbus_cnt:
                self.queue1.put("update")
            self.modbus_cnt=True

            self.ser_clc_event.set()
            self.ser_event.set()
            # self.ser_clc_event.set()
            # self.ser_event.set()
            # self.serial2Thread = ser1Thread( )__init__(self,com,bard,func,fmt,regs,rege,devs,deve):
            # create a pubsub receiver
            pub.subscribe( self.ser_data_update, 'update' )


        elif self.modbus_run is True:
            self.modbus_run = False

            self.m_button8.SetLabel(u"运行")
            self.m_statusBar2.SetStatusText( u"软件状态：" + "数据采集停止", 0 )

            self.ser_clc_event.clear()
            self.ser_event.clear()
            # self.stop_thread(self.serial1Thread)
            # self.stop_thread( self.clcThread )
            # self.serial1Thread.join()
            # self.clcThread.join()


            # print( fmt )
    def stop(self, event):
        event.Skip()


    def communication(self, event):
        event.Skip()
    def dis_fmt_update(self):
        #self.dis_fmt[地址]
        #self.dis_fmt_name[对应名称]
        title_str = self.conf.get( "excel", "disp_fmt" )
        print( title_str )
        str_title = re.findall( r"{.+}", title_str )
        title = [i.replace( '{', '' ).replace( '}', '' ) for i in str_title]
        print( title )
        for i in title:
            temp1 = i.split( ',' )
            self.dis_fmt_name.append( temp1[0] )
            t=[int(x) for x in temp1[1:]]
            self.dis_fmt.append(t)
        # print(self.dis_fmt)



    def switch(self, event):
        event.Skip()
        if self.conf.getboolean( "excel", "disp_set" ) is True:
          self.dis_fmt_update()#数据采集
          self.m_grid2.ClearGrid()
          self.m_staticText12.SetLabelText(self.dis_fmt_name[self.swit])
          self.swit += 1
          if self.swit >= len(self.dis_fmt_name):
              self.swit=0





app = wx.App()
frame = MainWindow(None,"modbus数据监控")
frame.Show()
app.MainLoop()