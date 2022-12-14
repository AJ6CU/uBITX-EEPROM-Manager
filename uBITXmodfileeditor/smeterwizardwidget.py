#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class SmeterwizardWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(SmeterwizardWidget, self).__init__(master, **kw)
        frame1 = ttk.Frame(self)
        frame1.configure(height=200, width=800)
        self.acquireADCValues_Frame = ttk.Frame(frame1)
        self.acquireADCValues_Frame.configure(
            height=200, relief="ridge", width=200)
        label3 = ttk.Label(self.acquireADCValues_Frame)
        label3.configure(
            justify="left",
            relief="raised",
            style="Heading3.TLabel",
            text='Define High/Low ADC Values')
        label3.pack(anchor="w", padx=10, pady=10, side="top")
        frame8 = ttk.Frame(self.acquireADCValues_Frame)
        frame8.configure(height=200, width=200)
        frame11 = ttk.Frame(frame8)
        frame11.configure(height=200, width=200)
        label4 = ttk.Label(frame11)
        label4.configure(style="Heading4.TLabel", text='ADC Manual Entry:')
        label4.grid(column=0, row=0)
        label5 = ttk.Label(frame11)
        label5.configure(style="Normal.TLabel", text='Min:')
        label5.grid(column=0, row=1, sticky="e")
        self.smeterWizardManualMin_Entry_WIDGET = ttk.Entry(frame11)
        self.smeterWizardManualMin = tk.StringVar()
        self.smeterWizardManualMin_Entry_WIDGET.configure(
            textvariable=self.smeterWizardManualMin, validate="focusout", width=5)
        self.smeterWizardManualMin_Entry_WIDGET.grid(column=2, row=1)
        _validatecmd = (
            self.smeterWizardManualMin_Entry_WIDGET.register(
                self.validate_smeterWizardManualMin), "%P", "%V")
        self.smeterWizardManualMin_Entry_WIDGET.configure(
            validatecommand=_validatecmd)
        label6 = ttk.Label(frame11)
        label6.configure(text='Max:')
        label6.grid(column=0, row=3, sticky="e")
        self.smeterWizardManualMax_Entry_WIDGET = ttk.Entry(frame11)
        self.smeterWizardManualMax = tk.StringVar()
        self.smeterWizardManualMax_Entry_WIDGET.configure(
            textvariable=self.smeterWizardManualMax, validate="focusout", width=5)
        self.smeterWizardManualMax_Entry_WIDGET.grid(column=2, row=3)
        _validatecmd = (
            self.smeterWizardManualMax_Entry_WIDGET.register(
                self.validate_smeterWizardManualMax), "%P", "%V")
        self.smeterWizardManualMax_Entry_WIDGET.configure(
            validatecommand=_validatecmd)
        frame11.grid(column=0, padx=10, row=0, sticky="n")
        separator1 = ttk.Separator(frame8)
        separator1.configure(orient="vertical")
        separator1.grid(column=3, padx=30, row=0, rowspan=3, sticky="ns")
        frame12 = ttk.Frame(frame8)
        frame12.configure(height=200, width=200)
        label7 = ttk.Label(frame12)
        label7.configure(style="Heading4.TLabel", text='Read from uBITX:')
        label7.grid(column=0, padx="0 15", row=0, sticky="w")
        self.com_portManager_frame = ttk.Frame(frame12)
        self.com_portManager_frame.configure(height=50, width=200)
        self.com_portManager_frame.grid(
            column=0, columnspan=8, pady=10, row=1, sticky="ew")
        label12 = ttk.Label(frame12)
        label12.configure(style="Heading4.TLabel", text='Found:')
        label12.grid(column=7, padx=15, row=2, sticky="e")
        self.ADCubitxReadMin_Label_WIDGET = ttk.Label(frame12)
        self.ADCubitxReadMin = tk.StringVar(value='N/A')
        self.ADCubitxReadMin_Label_WIDGET.configure(
            font="TkDefaultFont",
            style="Normal.TLabel",
            text='N/A',
            textvariable=self.ADCubitxReadMin)
        self.ADCubitxReadMin_Label_WIDGET.grid(column=7, row=3)
        self.ADCubitxReadMax_Label_WIDGET = ttk.Label(frame12)
        self.ADCubitxReadMax = tk.StringVar(value='N/A')
        self.ADCubitxReadMax_Label_WIDGET.configure(
            text='N/A', textvariable=self.ADCubitxReadMax)
        self.ADCubitxReadMax_Label_WIDGET.grid(column=7, row=4)
        self.sampleSizeADC = tk.IntVar(value=1)
        __values = ['1', '5', '10', '15', '20', '25']
        self.sampleSizeADC_OptionMenu = ttk.OptionMenu(
            frame12, self.sampleSizeADC, 1, *__values, command=None)
        self.sampleSizeADC_OptionMenu.grid(column=1, padx="0 25", row=3)
        label10 = ttk.Label(frame12)
        label10.configure(compound="top", justify="left", text='# of Samples')
        label10.grid(column=0, padx="0 15", row=3, sticky="e")
        self.sampleDelayADC = tk.IntVar(value=5)
        __values = ['5', '10', '50', '100', '500', '1000']
        self.sampleDelayADC_OptionMenu_WIDGET = ttk.OptionMenu(
            frame12, self.sampleDelayADC, 5, *__values, command=None)
        self.sampleDelayADC_OptionMenu_WIDGET.grid(
            column=1, padx="0 25", row=4)
        label11 = ttk.Label(frame12)
        label11.configure(
            compound="top",
            cursor="arrow",
            justify="right",
            text='Delay (ms) between Samples',
            width=16,
            wraplength=100)
        label11.grid(column=0, padx="0 15", row=4, sticky="e")
        self.sampleADCReadMin_Button_WIDGET = ttk.Button(frame12)
        self.sampleADCReadMin_Button_WIDGET.configure(
            style="Normal.TButton", text='Read Min')
        self.sampleADCReadMin_Button_WIDGET.grid(column=6, row=3)
        self.sampleADCReadMin_Button_WIDGET.configure(
            command=self.sampleADCReadMin)
        self.sampleADCReadMax_Button_WIDGET = ttk.Button(frame12)
        self.sampleADCReadMax_Button_WIDGET.configure(
            style="Normal.TButton", text='Read Max')
        self.sampleADCReadMax_Button_WIDGET.grid(column=6, row=4)
        self.sampleADCReadMax_Button_WIDGET.configure(
            command=self.sampleADCReadMax)
        frame12.grid(column=4, row=0)
        frame8.pack(expand="true", fill="both", padx=5, pady=5, side="top")
        self.acquireADCValues_Frame.pack(
            expand="true", fill="both", padx=5, pady=5, side="top")
        self.selectCurve_Frame = ttk.Frame(frame1)
        self.selectCurve_Frame.configure(height=200, relief="ridge", width=200)
        label1 = ttk.Label(self.selectCurve_Frame)
        label1.configure(
            justify="left",
            relief="flat",
            state="normal",
            style="Heading3.TLabel",
            text='Curve Style')
        label1.grid(column=0, padx="10 0", pady="10 0", row=0)
        self.adcCurve1_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve1_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve1_Button = ttk.Button(self.adcCurve1_Button_frame)
        self.img_sample1125x80 = tk.PhotoImage(
            file="images/sample1-125x80.png")
        self.adcCurve1_Button.configure(image=self.img_sample1125x80)
        self.adcCurve1_Button.pack(anchor="center")
        self.adcCurve1_Button.configure(command=self.apply_Sample1)
        self.adcCurve1_Button_frame.grid(column=0, padx="20 0", pady=15, row=1)
        self.adcCurve2_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve2_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve2_Button = ttk.Button(self.adcCurve2_Button_frame)
        self.img_sample2125x80 = tk.PhotoImage(
            file="images/sample2-125x80.png")
        self.adcCurve2_Button.configure(image=self.img_sample2125x80)
        self.adcCurve2_Button.pack(anchor="center", side="top")
        self.adcCurve2_Button.configure(command=self.apply_Sample2)
        self.adcCurve2_Button_frame.grid(column=1, padx="20 0", pady=15, row=1)
        self.adcCurve3_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve3_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve3_Button = ttk.Button(self.adcCurve3_Button_frame)
        self.img_sample3125x80 = tk.PhotoImage(
            file="images/sample3-125x80.png")
        self.adcCurve3_Button.configure(image=self.img_sample3125x80)
        self.adcCurve3_Button.pack()
        self.adcCurve3_Button.configure(command=self.apply_Sample3)
        self.adcCurve3_Button_frame.grid(column=2, padx="20 0", pady=15, row=1)
        self.adcCurve4_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve4_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve4_Button = ttk.Button(self.adcCurve4_Button_frame)
        self.img_sample4125x80 = tk.PhotoImage(
            file="images/sample4-125x80.png")
        self.adcCurve4_Button.configure(image=self.img_sample4125x80)
        self.adcCurve4_Button.pack()
        self.adcCurve4_Button.configure(command=self.apply_Sample4)
        self.adcCurve4_Button_frame.grid(column=3, padx="20 0", pady=15, row=1)
        self.adcCurve5_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve5_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve5_Button = ttk.Button(self.adcCurve5_Button_frame)
        self.img_sample5125x80 = tk.PhotoImage(
            file="images/sample5-125x80.png")
        self.adcCurve5_Button.configure(image=self.img_sample5125x80)
        self.adcCurve5_Button.pack()
        self.adcCurve5_Button.configure(command=self.apply_Sample5)
        self.adcCurve5_Button_frame.grid(padx="20 0", pady=15, row=2)
        self.adcCurve6_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve6_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve6_Button = ttk.Button(self.adcCurve6_Button_frame)
        self.img_sample6125x80 = tk.PhotoImage(
            file="images/sample6-125x80.png")
        self.adcCurve6_Button.configure(image=self.img_sample6125x80)
        self.adcCurve6_Button.pack()
        self.adcCurve6_Button.configure(command=self.apply_Sample6)
        self.adcCurve6_Button_frame.grid(column=1, padx="20 0", pady=15, row=2)
        self.adcCurve7_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcCurve7_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCurve7_Button = ttk.Button(self.adcCurve7_Button_frame)
        self.img_sample7125x80 = tk.PhotoImage(
            file="images/sample7-125x80.png")
        self.adcCurve7_Button.configure(image=self.img_sample7125x80)
        self.adcCurve7_Button.pack()
        self.adcCurve7_Button.configure(command=self.apply_Sample7)
        self.adcCurve7_Button_frame.grid(column=2, padx="20 0", pady=15, row=2)
        self.adcManual_Button_frame = ttk.Frame(self.selectCurve_Frame)
        self.adcManual_Button_frame.configure(
            borderwidth=4,
            height=200,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.adcCustom_Button = ttk.Button(self.adcManual_Button_frame)
        self.img_Custom125x80 = tk.PhotoImage(file="images/Custom-125x80.png")
        self.adcCustom_Button.configure(
            image=self.img_Custom125x80, state="disabled")
        self.adcCustom_Button.pack()
        self.adcCustom_Button.configure(command=self.apply_Custom)
        self.adcManual_Button_frame.grid(column=3, padx="20 0", pady=15, row=2)
        self.selectCurve_Frame.pack(
            expand="true",
            fill="both",
            padx=5,
            pady=5,
            side="top")
        self.smeterAdjustCurve_Frame = ttk.Frame(frame1)
        self.smeterAdjustCurve_Frame.configure(
            height=200, relief="ridge", width=200)
        self.adc_scale_S1 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S1 = tk.StringVar()
        self.adc_scale_S1.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S1',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S1)
        self.adc_scale_S1.grid(column=0, padx="33 0", pady="0 10", row=1)
        self.adc_scale_S1.configure(command=self.apply_Custom)
        self.adc_scale_S2 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S2 = tk.StringVar()
        self.adc_scale_S2.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S2',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S2)
        self.adc_scale_S2.grid(column=1, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S2.configure(command=self.apply_Custom)
        self.adc_scale_S3 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S3 = tk.StringVar()
        self.adc_scale_S3.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S3',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S3)
        self.adc_scale_S3.grid(column=2, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S3.configure(command=self.apply_Custom)
        self.adc_scale_S4 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S4 = tk.StringVar()
        self.adc_scale_S4.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S4',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S4)
        self.adc_scale_S4.grid(column=3, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S4.configure(command=self.apply_Custom)
        self.adc_scale_S5 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S5 = tk.StringVar()
        self.adc_scale_S5.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S5',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S5)
        self.adc_scale_S5.grid(column=4, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S5.configure(command=self.apply_Custom)
        self.adc_scale_S6 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S6 = tk.StringVar()
        self.adc_scale_S6.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S6',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S6)
        self.adc_scale_S6.grid(column=5, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S6.configure(command=self.apply_Custom)
        self.adc_scale_S7 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S7 = tk.StringVar()
        self.adc_scale_S7.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S7',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S7)
        self.adc_scale_S7.grid(column=6, padx="2 0", pady="0 10", row=1)
        self.adc_scale_S7.configure(command=self.apply_Custom)
        self.adc_scale_S8 = tk.Scale(self.smeterAdjustCurve_Frame)
        self.smeterWizard_S8 = tk.StringVar()
        self.adc_scale_S8.configure(
            font="{Arial} 10 {bold}",
            from_=1023,
            label='S8',
            length=300,
            orient="vertical",
            relief="raised",
            repeatinterval=0,
            resolution=1,
            to=0,
            variable=self.smeterWizard_S8)
        self.adc_scale_S8.grid(column=7, padx="2 33", pady="0 10", row=1)
        self.adc_scale_S8.configure(command=self.apply_Custom)
        label2 = ttk.Label(self.smeterAdjustCurve_Frame)
        label2.configure(
            justify="left",
            relief="flat",
            state="normal",
            style="Heading3.TLabel",
            text='Tunable Individual S-Values')
        label2.grid(
            column=0,
            columnspan=3,
            padx=10,
            pady="10 15",
            row=0,
            sticky="w")
        self.smeterAdjustCurve_Frame.pack(
            expand="true", fill="x", padx=5, pady=5, side="top")
        self.confirmCancelButton_Frame = ttk.Frame(frame1)
        self.confirmCancelButton_Frame.configure(height=200, width=200)
        self.smeterWizard_Apply_Button_WIDGET = ttk.Button(
            self.confirmCancelButton_Frame)
        self.smeterWizard_Apply_Button_WIDGET.configure(
            style="Button4.TButton", text='Apply')
        self.smeterWizard_Apply_Button_WIDGET.grid(
            column=0, padx="0 25", pady=15, row=0)
        self.smeterWizard_Apply_Button_WIDGET.configure(
            command=self.smeterWizard_Apply_Button)
        self.smeterWizard_Cancel_Button_WIDGET = ttk.Button(
            self.confirmCancelButton_Frame)
        self.smeterWizard_Cancel_Button_WIDGET.configure(
            style="Button4.TButton", text='Cancel')
        self.smeterWizard_Cancel_Button_WIDGET.grid(column=2, row=0)
        self.smeterWizard_Cancel_Button_WIDGET.configure(
            command=self.smeterWizard_Cancel_Button)
        self.button4 = ttk.Button(self.confirmCancelButton_Frame)
        self.button4.configure(style="Button4.TButton", text='Reset')
        self.button4.grid(column=1, padx="0 25", pady=15, row=0)
        self.button4.configure(command=self.resetADCAssistant)
        self.confirmCancelButton_Frame.pack(expand="false", side="top")
        frame1.pack(expand="true", fill="both", side="top")
        self.configure(height=200, width=800)
        self.title("S-Meter Helper")

        self.setup_ttk_styles()

    def setup_ttk_styles(self):
        # ttk styles configuration
        self.style = style = ttk.Style()
        optiondb = style.master
        # --------------------
        # This file is used for defining Ttk styles.
        # Use the 'style' object to define styles.

        # Pygubu Designer will need to know which style definition file
        # you wish to use in your project.

        # To specify a style definition file in Pygubu Designer:
        # Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

        # In Pygubu Designer:
        # Assuming that you have specified a style definition file,
        # - Use the 'style' combobox drop-down menu in Pygubu Designer
        #   to select a style that you have defined.
        # - Changes made to the chosen style definition file will be
        #   automatically reflected in Pygubu Designer.
        # --------------------

        # Example code:
        fontList = {'Heading1': ('Times New Roman', 24, 'bold', 'italic'),
                    'Heading2': ('Arial', 18, 'bold'),
                    'Heading3': ('Arial', 12, 'bold'),
                    'Heading4': ('Arial', 10, 'bold'),
                    'Normal': ('Default', 10),
                    'Emphasis': ('Default', 12, 'bold'),
                    'Symbol1': ('Symbol', 18, 'bold'),
                    'Symbol3': ('Symbol', 12, 'bold')}

        style.configure(
            'Heading1.TLabel',
            font=fontList['Heading1'],
            background='blue',
            foreground='white')
        style.configure('Heading2.TLabel', font=fontList['Heading2'])
        style.configure('Heading3.TLabel', font=fontList['Heading3'])
        style.configure('Heading4.TLabel', font=fontList['Heading4'])
        style.configure('Normal.TLabel', font=fontList['Normal'])
        style.configure('Symbol1.TLabel', font=fontList['Symbol1'])
        style.configure('Button3.TButton', font=fontList['Heading3'])
        style.configure('Button4.TButton', font=fontList['Heading4'])
        style.configure('Normal.TButton', font=fontList['Normal'])
        style.configure('Symbol1.TButton', font=fontList['Symbol1'])
        style.configure('Symbol3.TButton', font=fontList['Symbol3'])
        style.configure('ButtonEmphasis.TButton', font=fontList['Emphasis'])
        style.configure('RadioButton3.TRadiobutton', font=fontList['Heading3'])
        style.configure('RadioButton4.TRadiobutton', font=fontList['Heading4'])
        style.configure(
            'RadioButtonNormal.TRadiobutton',
            font=fontList['Normal'])
        style.configure(
            'RadioButtonEmphasis.TRadiobutton',
            font=fontList['Emphasis'])
        style.configure('Checkbox3.TCheckbutton', font=fontList['Heading3'])
        style.configure('Checkbox4.TCheckbutton', font=fontList['Heading4'])
        style.configure(
            'CheckboxEmphasis.TCheckbutton',
            font=fontList['Emphasis'])
        style.configure('ComboBox3.TCombobox', font=fontList['Heading3'])
        style.configure('ComboBox4.TCombobox', font=fontList['Heading4'])
        style.configure('Normal.TEntry', font=fontList['Normal'])
        style.configure(
            'NoBorder.TEntry',
            font=fontList['Normal'],
            highlightthickness=0,
            borderwidth=0,
            bd=0)
        style.configure('Title.TFrame', background='blue', foreground='white')
        style.configure(
            'Heading2.TLabelframe.Label',
            font=fontList['Heading3'])
        style.configure('Heading2.TLabelframe')
        style.configure('Normal.TText', font=fontList['Heading3'])

        style.configure('Highlight.TFrame', background='blue', bd=4)
        style.configure('Normal.TFrame', background='gray', bd=4)

    def validate_smeterWizardManualMin(self, p_entry_value, v_condition):
        pass

    def validate_smeterWizardManualMax(self, p_entry_value, v_condition):
        pass

    def sampleADCReadMin(self):
        pass

    def sampleADCReadMax(self):
        pass

    def apply_Sample1(self):
        pass

    def apply_Sample2(self):
        pass

    def apply_Sample3(self):
        pass

    def apply_Sample4(self):
        pass

    def apply_Sample5(self):
        pass

    def apply_Sample6(self):
        pass

    def apply_Sample7(self):
        pass

    def apply_Custom(self):
        pass

    def smeterWizard_Apply_Button(self):
        pass

    def smeterWizard_Cancel_Button(self):
        pass

    def resetADCAssistant(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = SmeterwizardWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
