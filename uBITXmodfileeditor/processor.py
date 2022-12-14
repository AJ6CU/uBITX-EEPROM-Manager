from tkinter import *
import tkinter as tk
#import os, sys
#import time
from printtolog import *
#from lxml import etree as ET
import serial.tools.list_ports              # Used to get a list of com ports
from globalvars import *
#from readEEPROMData import readEEPROMData
#from getters import getters
#from time import sleep
from com_portManager import com_portManager

import pathlib

from sourceselectorwidget import SourceselectorWidget

class Processor(SourceselectorWidget):
    def __init__(self, parent):
        super().__init__(parent)


        # put file selector in default state
        self.selectSaveFileFrame.forget()               #  Want to show the com port option  as default, hide safed file option
        self.savedFilePathChooserWidget.config(filetypes=[('uBITX Saved Files','.xml .btx')])         # Manually add restriction to only XML and btx files
        self.savedFilePathChooserWidget.config(initialdir=HOMEDIRECTORY)         # default to start off in users' home directory
        self.savedFilePathChooser.set(USERMODFILE)
        self.lastDir = HOMEDIRECTORY

        # create com port object
        self.comPortObj = com_portManager(self.com_portManager_frame, self)


    def setLog(self, log ):                     # this method is called to tell object where to write the log
        self.log = log

    def setNotebook(self, settingsNotebook):
        self.settingsNotebook = settingsNotebook


    def sourceSelected(self):                   # this method allows user to select comport vs file and loads the right UX to select
                                                # the desired object
                                                # also disables the goButtonWidget and allows downstream selection to re-enable once
                                                # a valid com port or file is selected.

        if self.sourceSelectorRadioButton.get() == "uBITX":
           # self.goButtonWidget.unbind("<Button-1>")            # Must explictly unbind button to prevent disabled button from being clickable
           # self.goButtonWidget.configure(state=DISABLED)       # Now fade it out
            self.goButtonWidget.bind("<Button-1>", self.processComPort)
            self.goButtonWidget.configure(state=NORMAL)

            # since a user can switch  back and forth, or have to correct errors. update initial directories to make their life easier
            # also reset default file name to a message to select one
            # USERMODFILE always has the text "Please Select File"
            #
            if (self.lastDir != HOMEDIRECTORY):
                self.lastDir = pathlib.Path(self.savedFilePathChooser.get()).parent
            self.savedFilePathChooserWidget.config(path=USERMODFILE, initialdir=self.lastDir)

            self.selectSaveFileFrame.forget()
            self.com_portManager_frame.pack()

            # pre-load com ports
            self.comPortObj.updateComPorts()                           # Fill in available Com Ports
            self.comPortObj.pack()                                      # make com it visible

        else:
          #  self.goButtonWidget.unbind("<Button-1>")            # In this case we have switched into file selection mode. Unbind and disable read button
          #  self.goButtonWidget.configure(state=DISABLED)       # If user selects a valid file, the button is re-enabled and callback connected
            self.com_portManager_frame.forget()                # In the on_path_changed event
            self.selectSaveFileFrame.pack()

    def on_path_changed(self, event=None):
        self.path=self.savedFilePathChooser.get()
        if (pathlib.Path(self.path).exists()):
            self.goButtonWidget.bind("<Button-1>", self.processFile)
            self.goButtonWidget.configure(state=NORMAL)
            self.lastDir = pathlib.Path(self.savedFilePathChooser.get()).parent


    def processFile(self, *args):
        pass


    def enableGoButtonComPort(self):
        self.goButtonWidget.bind("<Button-1>", self.processComPort)
        self.goButtonWidget.configure(state='normal')

    def disableGoButtonComPort(self):
        self.goButtonWidget.unbind("<Button-1>")            # In this case we have switched into file selection mode. Unbind and disable read button
        self.goButtonWidget.configure(state='disabled')       # If user selects a valid file, the button is re-enabled and callback connected

