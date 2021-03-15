# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Frameku
###########################################################################

class Frameku ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tugas 1 PBO_2 Yusrian", pos = wx.DefaultPosition, size = wx.Size( 662,605 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 40, 123 ) )

		boxSizer = wx.BoxSizer( wx.VERTICAL )

		self.panelku = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		boxSixer2 = wx.BoxSizer( wx.VERTICAL )

		self.labelText = wx.StaticText( self.panelku, wx.ID_ANY, u"\"HELLO WX\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelText.Wrap( -1 )

		self.labelText.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )
		self.labelText.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		boxSixer2.Add( self.labelText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.labelNama = wx.StaticText( self.panelku, wx.ID_ANY, u"Nama : Yusrian Darus Syifa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNama.Wrap( -1 )

		self.labelNama.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )
		self.labelNama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		boxSixer2.Add( self.labelNama, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.labelNim = wx.StaticText( self.panelku, wx.ID_ANY, u"NIM : 192410101083", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNim.Wrap( -1 )

		self.labelNim.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Black" ) )
		self.labelNim.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		boxSixer2.Add( self.labelNim, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gridSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.aye = wx.adv.AnimationCtrl( self.panelku, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.aye.LoadFile( u"D:\\semester 4\\Pemrograman Berorientasi Obyek 2\\wxformbuilder\\aye.gif" )
		self.aye.SetBackgroundColour( wx.Colour( 0, 40, 123 ) )

		gridSizer.Add( self.aye, 0, wx.ALL, 5 )

		self.uye = wx.adv.AnimationCtrl( self.panelku, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		self.uye.LoadFile( u"D:\\semester 4\\Pemrograman Berorientasi Obyek 2\\wxformbuilder\\uye.gif" )
		self.uye.SetBackgroundColour( wx.Colour( 0, 40, 123 ) )

		gridSizer.Add( self.uye, 0, wx.ALL, 5 )


		boxSixer2.Add( gridSizer, 1, wx.EXPAND, 5 )


		self.panelku.SetSizer( boxSixer2 )
		self.panelku.Layout()
		boxSixer2.Fit( self.panelku )
		boxSizer.Add( self.panelku, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( boxSizer )
		self.Layout()
		self.menuBarKu = wx.MenuBar( 0 )
		self.menuDataDiri = wx.Menu()
		self.m_menuItem_nama = wx.MenuItem( self.menuDataDiri, wx.ID_ANY, u"Nama : Yusrian Darus Syifa", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuDataDiri.Append( self.m_menuItem_nama )

		self.menuDataDiri.AppendSeparator()

		self.m_menuItem_nim = wx.MenuItem( self.menuDataDiri, wx.ID_ANY, u"NIM : 192410101083", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuDataDiri.Append( self.m_menuItem_nim )

		self.menuDataDiri.AppendSeparator()

		self.m_menuItem_kelas = wx.MenuItem( self.menuDataDiri, wx.ID_ANY, u"Kelas : PBO 2 C", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuDataDiri.Append( self.m_menuItem_kelas )

		self.menuDataDiri.AppendSeparator()

		self.m_menuItem_prodi = wx.MenuItem( self.menuDataDiri, wx.ID_ANY, u"Program Studi : Sistem Informasi", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuDataDiri.Append( self.m_menuItem_prodi )

		self.menuDataDiri.AppendSeparator()

		self.m_menuItem_fakultas = wx.MenuItem( self.menuDataDiri, wx.ID_ANY, u"Fakultas : Fakultas Ilmu Komputer", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuDataDiri.Append( self.m_menuItem_fakultas )

		self.menuBarKu.Append( self.menuDataDiri, u"Data Diri" )

		self.menuNama = wx.Menu()
		self.m_menu1 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"YUSRIAN DARUS SYIFA", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem8 )

		self.menuNama.AppendSubMenu( self.m_menu1, u"Nama saya" )

		self.menuBarKu.Append( self.menuNama, u"Nama" )

		self.menuNim = wx.Menu()
		self.m_menu2 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"192410101083", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem6 )

		self.menuNim.AppendSubMenu( self.m_menu2, u"NIM saya " )

		self.menuBarKu.Append( self.menuNim, u"NIM" )

		self.menuText = wx.Menu()
		self.m_menu3 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"WX", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem7 )

		self.menuText.AppendSubMenu( self.m_menu3, u"HELLO" )

		self.menuBarKu.Append( self.menuText, u"text" )

		self.SetMenuBar( self.menuBarKu )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


