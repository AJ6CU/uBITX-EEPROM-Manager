#ENUMS#####################################################
INTERNAL_FIRMWARE_VERSION = ["NA", "V1.061", "V1.07", "V1.08", "V1.09", "V2.0"]
MODE_SELECT = ["DEFAULT","xxx","LSB","USB","CWL","CWU"]
BOOL_SELECT = ["NO","YES"]
TUNE_RESTRICT_SELECT = ["NONE","BAND"]
TX_RESTRICT_SELECT = ["NONE", "HAM"]
TX_RESTRICT_MINIMUM = 100
CW_KEY_SELECT = ["STRAIGHT","IAMBICA","IAMBICB"]
MAIN_MENU_SELECT = ["DEFAULT","CW"]
BOOT_MODE = ["NORMAL", "SDR"]
SDR_OFFSET_MODE = ["NONE","FIXED", "MHZ", "KHZ"]
SHOW_CHANNEL_NAME = 0x03
HIDE_CHANNEL_NAME = 0x00
FTN_KEY_SELECT = ["NONE", "MODE", "BAND-UP", "BAND-DN", "TUNE-STEP", "VFO-A/B", "SPLIT", "TX", "SDR-MODE", "RIT"]
LPF_MODE_SELECT = ["OFF", "STANDARD", "EXTENDED"]
LPF_MODE_SETTING = [0x00, 0x57, 0x58]
LPF_CTRL_SELECT = ["TX_LPF_A", "TX_LPF_B", "TX_LPF_C", "D10", "D11", "D12", "D13","NONE"]
#end ENUMS#################################################

READCOMMAND=0xDB
WRITECOMMAND=0xDC

OK=0x77
ACK = 0x00
RETRIES=3


EEPROMSIZE=1024
BACKUPFILESIZE=2048


CHANNELNAMELENGTH = 5                               #Number of characters in the Channel Name
WSPRNAMELENGTH = 5                                  #Number of characters in the Channel Name
WSPRREG1LENGTH = 5
WSPRREG2LENGTH = 3
TOTALCWMESSAGES=10                                  #assumption on number of CW message elements to be provided
SIZEOFWSPRMESSAGES=41                               #size in bytes of wspr messages
MAXCALLSIGNLEN = 18                                 #Max length of callsign and alt callsign

#application required files################################################


EEPROMMEMORYMAP="eeprommemorymap.xml"               #Maps EEPROM locations to settings
USERMODFILETEMPLACE="usermodfiletemplate.xml"       #Template file used to fill in with data from EEPROM

#COM_PORT = "/dev/tty.usbserial-1410"            # format for macos
COM_PORT = "COM PORT"                             # format for windows
BAUD = 38400
USERMODFILE="usermodfile.xml"                       #Output of process - file that User can customize

#   Dictionary to hold current values of usermodfile and whether dirty or not
userModFileValues = {}
userModFileDirty = {}
userModFileToolTips = {}

clearErrorMessages = ['MASTER_CAL_INVALID_WIDGET', 'USB_CAL_INVALID_WIDGET', 'CW_CAL_INVALID_WIDGET', 'CW_SIDETONE_INVALID_WIDGET',
                    'CW_SPEED_WPM_INVALID_WIDGET', 'CW_DELAY_MS_INVALID_WIDGET','CW_START_MS_INVALID_WIDGET', 'USER_CALLSIGN_INVALID_WIDGET', 'CW_ADC_ST_INVALID_WIDGET',
                    'CW_ADC_DOT_INVALID_WIDGET', 'CW_ADC_DASH_INVALID_WIDGET', 'CW_ADC_BOTH_INVALID_WIDGET',
                    'CHANNEL_FREQ1_INVALID_WIDGET', 'CHANNEL_FREQ2_INVALID_WIDGET', 'CHANNEL_FREQ3_INVALID_WIDGET',
                    'CHANNEL_FREQ4_INVALID_WIDGET', 'CHANNEL_FREQ5_INVALID_WIDGET', 'CHANNEL_FREQ6_INVALID_WIDGET',
                    'CHANNEL_FREQ7_INVALID_WIDGET', 'CHANNEL_FREQ8_INVALID_WIDGET', 'CHANNEL_FREQ9_INVALID_WIDGET',
                    'CHANNEL_FREQ10_INVALID_WIDGET', 'CHANNEL_FREQ11_INVALID_WIDGET', 'CHANNEL_FREQ12_INVALID_WIDGET',
                    'CHANNEL_FREQ13_INVALID_WIDGET', 'CHANNEL_FREQ14_INVALID_WIDGET', 'CHANNEL_FREQ15_INVALID_WIDGET',
                    'CHANNEL_FREQ16_INVALID_WIDGET', 'CHANNEL_FREQ17_INVALID_WIDGET', 'CHANNEL_FREQ18_INVALID_WIDGET',
                    'CHANNEL_FREQ19_INVALID_WIDGET', 'CHANNEL_FREQ20_INVALID_WIDGET', 'Extended_Channel_Frame',
                    'HAM_BAND_COUNT_INVALID_WIDGET',
                    'HAM_BAND_RANGE1_INVALID_WIDGET', 'HAM_BAND_RANGE2_INVALID_WIDGET', 'HAM_BAND_RANGE3_INVALID_WIDGET', 'HAM_BAND_RANGE4_INVALID_WIDGET',
                    'HAM_BAND_RANGE5_INVALID_WIDGET', 'HAM_BAND_RANGE6_INVALID_WIDGET', 'HAM_BAND_RANGE7_INVALID_WIDGET', 'HAM_BAND_RANGE8_INVALID_WIDGET',
                    'HAM_BAND_RANGE9_INVALID_WIDGET', 'HAM_BAND_RANGE10_INVALID_WIDGET']
readyToGo = ['FACTORY_VALUES_MASTER_CAL', 'FACTORY_VALUES_USB_CAL',
             'MASTER_CAL', 'USB_CAL', 'CW_CAL', 'VFO_A', 'VFO_A_MODE', 'VFO_B', 'VFO_B_MODE', 'CW_KEY_TYPE',
            'CW_SIDETONE',  'CW_SPEED_WPM', 'CW_DELAY_MS','CW_START_MS', 'USER_CALLSIGN', 'CW_ADC_ST_FROM', 'CW_ADC_ST_TO',
            'CW_ADC_DOT_FROM', 'CW_ADC_DOT_TO', 'CW_ADC_DASH_FROM', 'CW_ADC_DASH_TO', 'CW_ADC_BOTH_FROM', 'CW_ADC_BOTH_TO',
            'CHANNEL_FREQ1', 'CHANNEL_FREQ1_MODE', 'CHANNEL_FREQ1_SHOW_NAME', 'CHANNEL_FREQ1_NAME',
            'CHANNEL_FREQ1', 'CHANNEL_FREQ1_MODE', 'CHANNEL_FREQ1_SHOW_NAME', 'CHANNEL_FREQ1_NAME',
            'CHANNEL_FREQ2', 'CHANNEL_FREQ2_MODE', 'CHANNEL_FREQ2_SHOW_NAME', 'CHANNEL_FREQ2_NAME',
            'CHANNEL_FREQ3', 'CHANNEL_FREQ3_MODE', 'CHANNEL_FREQ3_SHOW_NAME', 'CHANNEL_FREQ3_NAME',
            'CHANNEL_FREQ4', 'CHANNEL_FREQ4_MODE', 'CHANNEL_FREQ4_SHOW_NAME', 'CHANNEL_FREQ4_NAME',
            'CHANNEL_FREQ5', 'CHANNEL_FREQ5_MODE', 'CHANNEL_FREQ5_SHOW_NAME', 'CHANNEL_FREQ5_NAME',
            'CHANNEL_FREQ6', 'CHANNEL_FREQ6_MODE', 'CHANNEL_FREQ6_SHOW_NAME', 'CHANNEL_FREQ6_NAME',
            'CHANNEL_FREQ7', 'CHANNEL_FREQ7_MODE', 'CHANNEL_FREQ7_SHOW_NAME', 'CHANNEL_FREQ7_NAME',
            'CHANNEL_FREQ8', 'CHANNEL_FREQ8_MODE', 'CHANNEL_FREQ8_SHOW_NAME', 'CHANNEL_FREQ8_NAME',
            'CHANNEL_FREQ9', 'CHANNEL_FREQ9_MODE', 'CHANNEL_FREQ9_SHOW_NAME', 'CHANNEL_FREQ9_NAME',
            'CHANNEL_FREQ10', 'CHANNEL_FREQ10_MODE', 'CHANNEL_FREQ10_SHOW_NAME', 'CHANNEL_FREQ10_NAME',
            'CHANNEL_FREQ11', 'CHANNEL_FREQ11_MODE',  'CHANNEL_FREQ12', 'CHANNEL_FREQ12_MODE',
            'CHANNEL_FREQ13', 'CHANNEL_FREQ13_MODE',  'CHANNEL_FREQ14', 'CHANNEL_FREQ14_MODE',
            'CHANNEL_FREQ15', 'CHANNEL_FREQ15_MODE',  'CHANNEL_FREQ16', 'CHANNEL_FREQ16_MODE',
            'CHANNEL_FREQ17', 'CHANNEL_FREQ17_MODE',  'CHANNEL_FREQ18', 'CHANNEL_FREQ18_MODE',
            'CHANNEL_FREQ19', 'CHANNEL_FREQ19_MODE',  'CHANNEL_FREQ20', 'CHANNEL_FREQ20_MODE',
            'HAM_BAND_COUNT', 'HAM_BAND_RANGE1_START', 'HAM_BAND_RANGE1_END', 'HAM_BAND_RANGE2_START', 'HAM_BAND_RANGE2_END',
            'HAM_BAND_RANGE3_START', 'HAM_BAND_RANGE3_END', 'HAM_BAND_RANGE4_START', 'HAM_BAND_RANGE4_END', 'HAM_BAND_RANGE5_START',
            'HAM_BAND_RANGE5_END', 'HAM_BAND_RANGE6_START', 'HAM_BAND_RANGE6_END', 'HAM_BAND_RANGE7_START', 'HAM_BAND_RANGE7_END',
            'HAM_BAND_RANGE8_START', 'HAM_BAND_RANGE8_END', 'HAM_BAND_RANGE9_START', 'HAM_BAND_RANGE9_END', 'HAM_BAND_RANGE10_START',
            'HAM_BAND_RANGE10_END',  'HAM_BAND_FREQS1', 'HAM_BAND_FREQS2','HAM_BAND_FREQS3','HAM_BAND_FREQS4','HAM_BAND_FREQS5',
            'HAM_BAND_FREQS6','HAM_BAND_FREQS7','HAM_BAND_FREQS8','HAM_BAND_FREQS9','HAM_BAND_FREQS10', 'HAM_BAND_FREQS1_MODE',
            'HAM_BAND_FREQS2_MODE', 'HAM_BAND_FREQS3_MODE', 'HAM_BAND_FREQS4_MODE', 'HAM_BAND_FREQS5_MODE', 'HAM_BAND_FREQS6_MODE',
            'HAM_BAND_FREQS7_MODE', 'HAM_BAND_FREQS8_MODE', 'HAM_BAND_FREQS9_MODE', 'HAM_BAND_FREQS10_MODE'
            ]

