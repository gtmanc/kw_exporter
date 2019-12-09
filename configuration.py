
server = "brookmanwang.altek.c.t"
host = 'BrookmanWang'
port = 8080

user = 'jensonchin' #user = getpass.getuser()


projects = {"WAVE3_CommsFW",
            "WAVE3_JNI_ContinuaAgent_1",
            "WAVE3_JNI_RCFrameworkLibrary_1",
            "WAVE3_RCApp_ContinuaService",
            "WAVE3_RCApp_EMWRService",
            "WAVE3_RCApp_FirmwareUpdateChecker",
            "WAVE3_RCApp_RCFrameworkLibrary",
            "WAVE3_RCApp_RCLauncher",
            "WAVE3_RCApp_RCSystemService",
            "WAVE3_RCApp_ReminderService",
            "WAVE3_RCApp_SoloMPumpService"
}

name_report = "KW_Report.xlsx"

# Determine the query
# To retrieve all the fixed issue, 'build:any state:Fixed' can be used. 
# However, there is something needs to be done for the JSon parser.  
query = 'build:any'