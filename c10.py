from tkinter import *

conduitType = ["Heavy duty rigid UPVC conduit", "Corflo conduit", 
"Medium duty corrugated", "Medium duty rigid UPVC conduit"]
CableType = ["-", "1", "1.5", "2.5", "4" , "6" ,"10" ,"16", "25", "35", "50", "70" , "95" ,"120" ,"150","185","240","300",
"400","500","630"]


class Application(Frame):

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.UserIn = IntVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self): 

        self.conduitLbl = Label (self, text = "Type of Conduit", height=2, width=20)#Label
        self.conduitLbl.grid(row=0, column = 0)

        self.conduit = StringVar(master) ### OPTION MENU FOR CONIOT TYPE
        self.conduit.set("Heavy duty rigid UPVC conduit") # default value
        self.conduitOptions = OptionMenu(master, self.conduit, *conduitType)
        self.conduitOptions.config(width=28)
        self.conduitOptions.grid(row=0, column=1)
        
        self.PVCLabel = Label (master, text = "Cable Type", height=2, width=20)#Label
        self.PVCLabel.grid(row=1, column = 0)
        
        self.cable = StringVar(master)
        self.cable.set("-") # default value
        self.PVCom = OptionMenu(master, self.cable, *CableType, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=1, column=1)

        self.circuitLbl = Label (master, text = "Number of Circuits:", height=1, width=20) #Label
        self.circuitLbl.grid(row=2, column = 0)

        self.getCircuit = StringVar()  
        self.getCircuit = Entry (master) ######## ENTRY BOX

        self.getCircuit.grid(row=2, column=1)        
            
        self.btn = Button(master, text="Calculate", bg="light grey", command=self.onButtonClick)
        self.btn.grid(row = 3,column=1)           

        self.conduitTypeResult = Label (master, text = "Conduit Type: ", height=1, width=40) #Label
        self.conduitTypeResult.grid(row=0, column =2) 

        self.PVCResult = Label (master, text = "Cable Type: ", height=2, width=25) #Label
        self.PVCResult.grid(row=1, column =2)    

        self.circuitNo = Label (master, text = "Number of Circuits: ", height=2, width=25) #Label
        self.circuitNo.grid(row=2, column =2)   

        self.conduitResult = Label (master, text = "-", height=2, width=40, font='Helvetica 9 bold') #Label
        self.conduitResult.grid(row=3, column =2)    

        self.disclaimerText = Label (master, text = """DISCLAIMER\n Please refer to Table C10 (can be viewed by clicking Open Table button)
         to confirm the results before practically applying the Number Of Conduits. Each output has not been tested thus 
         caution should be taken when using this program.\n
         REFERENCE: AS/NZ 3000:2018 Electrical Installations (known as the Australian/New Zealand Wiring Rules)"""
        ,font='Helvetica 9 bold') #Label
        self.disclaimerText.grid(row=6, rowspan=2, column=0, columnspan=3, sticky=W)    
        
        self.close = Button(master, text="Close", bg="light grey", command=master.destroy)
        self.close.grid(row = 4,column=0) 

        self.canvas = Canvas(master, width=99, height=29)
        self.canvas.grid(row=4, column=2)
        self.logo = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c10---max-single-core-sheathed-cables\\Lucid Logo.PNG')
        self.canvas.create_image(0, 0, image = self.logo, anchor = NW)
        self.canvas.logo = self.logo   

        def openImage(): ### opens table
            control = Toplevel()
            canvas = Canvas(control, width=1172, height=704)
            canvas.pack(expand = YES, fill = BOTH)
            png1 = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c10---max-single-core-sheathed-cables\\Capture.PNG')
            canvas.create_image(0, 0, image = png1, anchor = NW)
            canvas.png1 = png1

        self.openImage = Button(master, text="Open Table", bg="light grey", command=openImage)#image open button
        self.openImage.grid(row=4, column = 1)

        def reset():
             self.PVCResult.configure(text="" )
             self.conduitTypeResult.configure(text="-" )
             self.PVCResult.configure(text="-" )
             self.conduit.set("Heavy duty rigid UPVC conduit")
             self.cable.set("-")
             self.circuitNo.configure(text="-")
             self.conduitResult.configure(text="-", bg='gray85', borderwidth=2, relief='flat')

        self.tableview = Button(master, text="Reset", bg="light grey", command=reset)
        self.tableview.grid(row = 3,column=0) 

        if (self.cable.get()=='-'):
            self.btn.config(state=DISABLED)
        
        if (self.cable.get()=="1", "1.5", "2.5", "4" , "6" ,"10" ,"16", "25", "35", "50", "70" , "95" ,"120" ,"150","185","240","300",
        "400","500","630"):
            self.btn.config(state=NORMAL)
        
    
    def onButtonClick(self):
        
        #get values
        def getConduitType(self): #type of conduit
            self.x = self.conduit.get()
            return self.x
        def getCable(self):
            self.x = self.cable.get()
            return self.x             
        def getCircuitState(self):
            self.x = self.getCircuit.get()          
            return int(self.x)
        

        if not self.getCircuit.get():
            self.conduitResult.configure(text="Error: Missing Values", bg='orange' )      

        self.conduitTypeResult.configure(text="Conduit Type:  " + self.conduit.get(), font='Helvetica 9 bold')
       
        self.PVCResult.configure(text="CableType:  " + self.cable.get(),font='Helvetica 9 bold' )
        
        self.circuitNo.configure(text="Number of Circuits:  "+ self.getCircuit.get(), font='Helvetica 9 bold')

        def circuitNo(self):

            if (getConduitType(self)=="Heavy duty rigid UPVC conduit"):


                if(getCable(self)=="1" and getCircuitState(self) <= int("5")):
                    return "20"
                
                if(getCable(self)=="1" and getCircuitState(self)<= int("9")):
                    return "25"
                
                if(getCable(self)=="1" and getCircuitState(self)<= int("16")):
                    return "32"
            
                if(getCable(self)=="1" and getCircuitState(self)<= int("26")):
                    return "40"
                
                if(getCable(self)=="1" and getCircuitState(self)<= int("43")):
                    return "50"
                
                if(getCable(self)=="1" and getCircuitState(self)<= int("71")):
                    return "63"
                
                if(getCable(self)=="1" and getCircuitState(self) >= int("100")):
                    return "80(NZ), 80(AUS), 100(NZ), 100(AUS), 125 or 150"
        
                if ((getCable(self)=="25" or getCable(self)=="35" or getCable(self)=="50" )
                    and getCircuitState(self)<= int("0")):
                    return '20'
                
                if ((getCable(self)=="70" or getCable(self)=="95") and getCircuitState(self)<= int("0")):
                    return "20 or 25"
                if ((getCable(self)=="120" or getCable(self)=="150") and getCircuitState(self)<= int("0")):
                    return "20, 25 or 32"
                if ((getCable(self)=="185" or 
                getCable(self)=="240" or getCable(self)=="300") and getCircuitState(self)<= int("0")):
                    return "20, 25, 32 or 40" 
                if ((getCable(self)=="400" or getCable(self)=="500") and getCircuitState(self)<= int("0")):
                    return "20, 25, 32, 40 or 50"    
                if ((getCable(self)=="630") and getCircuitState(self)<= int("0")):
                    return "20, 25, 32, 40, 50 or 63"

                if ((getCable(self)=="25" or getCable(self)== "35")
                    and getCircuitState(self)<= int("1")):
                    return '25 or 32'
                if ((getCable(self)=="50") and getCircuitState(self)<= int("1")):
                    return "25,	32 or 40"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("1")):
                    return "25,	32,	40 or 50"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("1")):
                    return "32 or 40" 
                if ((getCable(self)=="120" or getCable(self)=="150") and getCircuitState(self)<= int("1")):
                    return "40 or 50"    
                if ((getCable(self)=="185" or 
                getCable(self)=="240") and getCircuitState(self)<= int("1")):
                    return "50 or 63"
                if ((getCable(self)=="300") and getCircuitState(self)<= int("1")):
                    return "50, 63 or 80(NZ)"
                if ((getCable(self)=="400" or getCable(self)=="500") and getCircuitState(self)<= int("1")):
                    return "63 or 80(NZ) or 80(AUS)"
                if ((getCable(self)=="630") and getCircuitState(self)<= int("1")):
                    return "80(NZ), 80(AUS) or 100(NZ)"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int(int("2"))):
                    return "40"
                if ((getCable(self)=="70") and getCircuitState(self)<= int(int("2"))):
                    return "50"
                if ((getCable(self)=="120") and getCircuitState(self)<= int("2")):
                    return "63"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("2")):
                    return "150"
                if ((getCable(self)=="240") and getCircuitState(self)<= int("2")):
                    return "80(NZ)"
                if ((getCable(self)=="300") and getCircuitState(self)<= int("2")):
                    return "80(AUS)"
                if ((getCable(self)=="630") and getCircuitState(self)<= int("2")):
                    return "100(AUS)"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("3")):
                    return "40"
                if ((getCable(self)=="50") and getCircuitState(self)<= int("3")):
                    return "50"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("3")):
                    return "63"
                if ((getCable(self)=="185") and getCircuitState(self)<= int("3")):
                    return "80(NZ)"
                if ((getCable(self)=="240") and getCircuitState(self)<= int("3")):
                    return "80(AUS)"
                if ((getCable(self)=="400" or getCable(self)=="500") and getCircuitState(self)<= int("3")):
                    return "100(NZ) or 100(AUS)"
                if ((getCable(self)=="630") and getCircuitState(self)<= int("3")):
                    return "125"

                if ((getCable(self)=="25") and getCircuitState(self)<= int("4")):
                    return "50"
                if ((getCable(self)=="50") and getCircuitState(self)<= int("4")):
                    return "63"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("4")):
                    return "80(NZ)"
                if ((getCable(self)=="185") and getCircuitState(self)<= int("4")):
                    return "80(AUS)"
                if ((getCable(self)=="300") and getCircuitState(self)<= int("4")):
                    return "100(NZ) or 100(AUS)"
                if ((getCable(self)=="500") and getCircuitState(self)<= int("4")):
                    return "125"
                if ((getCable(self)=="630") and getCircuitState(self)<= int("4")):
                    return "150"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("5")):
                    return "50"
                
                if ((getCable(self)=="120") and getCircuitState(self)<= int("5")):
                    return "80(NZ)"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("5")):
                    return "80(AUS)"
                if ((getCable(self)=="240") and getCircuitState(self)<= int("5")):
                    return "100(NZ) or 100(AUS)"
                if ((getCable(self)=="400") and getCircuitState(self)<= int("5")):
                    return "125"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("6")):
                    return "63"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("6")):
                    return "80(NZ)"
                if ((getCable(self)=="120") and getCircuitState(self)<= int("6")):
                    return "80(AUS)"
                if ((getCable(self)=="185") and getCircuitState(self)<= int("6")):
                    return "100(NZ) or 100(AUS)"
                if ((getCable(self)=="300") and getCircuitState(self)<= int("6")):
                    return "125"
                if ((getCable(self)=="500") and getCircuitState(self)<= int("6")):
                    return "150"
                #7
                if ((getCable(self)=="35") and getCircuitState(self)<= int("7")):
                    return "63"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("7")):
                    return "80(AUS)"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("7")):
                    return "100(NZ)"
                if ((getCable(self)=="400") and getCircuitState(self)<= int("7")):
                    return "150"
                #8                       
                if ((getCable(self)=="70") and getCircuitState(self)<= int("8")):
                    return "80(NZ)"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("8")):
                    return "100(AUS)"
                if ((getCable(self)=="240") and getCircuitState(self)<= int("8")):
                    return "125"
                if ((getCable(self)=="300") and getCircuitState(self)<= int("8")):
                    return "150"
                #9
                if ((getCable(self)=="25") and getCircuitState(self)<= int("9")):
                    return "63"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("9")):
                    return "80(AUS)"
                if ((getCable(self)=="120") and getCircuitState(self)<= int("9")):
                    return "100(NZ)"

                if ((getCable(self)=="50") and getCircuitState(self)<= int("10")):
                    return "80(NZ)"
                if ((getCable(self)=="120") and getCircuitState(self)<= int("10")):
                    return "100(AUS)"
                if ((getCable(self)=="185") and getCircuitState(self)<= int("10")):
                    return "125"
                if ((getCable(self)=="240") and getCircuitState(self)<= int("10")):
                    return "150"

                if ((getCable(self)=="95") and getCircuitState(self)<= int("11")):
                    return "100(NZ)"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("12")):
                    return "80(AUS)"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("12")):
                    return "100(AUS)"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("12")):
                    return "125"

                if ((getCable(self)=="35") and getCircuitState(self)<= int("15")):
                    return "80(AUS)"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("15")):
                    return "100(NZ)"              
                if ((getCable(self)=="120") and getCircuitState(self)<= int("15")):
                    return "125"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("16")):
                    return "80(NZ)"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("16")):
                    return "100(AUS)"
                if ((getCable(self)=="150") and getCircuitState(self)<= int("16")):
                    return "150"
                
                if ((getCable(self)=="95") and getCircuitState(self)<= int("18")):
                    return "125"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("19")):
                    return "80(AUS"
                if ((getCable(self)=="50") and getCircuitState(self)<= int("19")):
                    return "100(NZ)"
                
                if ((getCable(self)=="120") and getCircuitState(self)<= int("20")):
                    return "150"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("21")):
                    return "100(AUS)"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("24")):
                    return "100(NZ)"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("24")):
                    return "125"
                if ((getCable(self)=="95") and getCircuitState(self)<= int("24")):
                    return "150"

                if ((getCable(self)=="35") and getCircuitState(self)<= int("26")):
                    return "100(AUS)"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("29")):
                    return "100(NZ)"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("31")):
                    return "125"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("31")):
                    return "150"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("39")):
                    return "125"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("41")):
                    return "150"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("48")):
                    return "125"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("52")):
                    return "150"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("62")):
                    return "150"
                #CableType AND HEAVY    
                
                #1
                if ((getCable(self)=="4") and getCircuitState(self)<= int("1")):
                    return "20"
                if ((getCable(self)=="6") and getCircuitState(self)<= int("1")):
                    return "20"
                if ((getCable(self)=="10" or getCable(self)=="16") and getCircuitState(self)<= int("1")):
                    return "20 or 25"
                #3
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("3")):
                    return "20"
                if ((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self)<= int("3")):
                    return "25"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("3")):
                    return "32"

                #4
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("4")):
                    return "20"
                if ((getCable(self)=="10") and getCircuitState(self)<= int("4")):
                    return "32"
                #5

                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("5")):
                    return "25"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("5")):
                    return "40"
                #6
                if ((getCable(self)=="6") and getCircuitState(self)<= int("6")):
                    return "32"
                if ((getCable(self)=="10") and getCircuitState(self)<= int("6")):
                    return "40"
                #7
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("7")):
                    return "25"
                if ((getCable(self)=="4") and getCircuitState(self)<= int("7")):
                    return "32"
                #8

                if ((getCable(self)=="16") and getCircuitState(self)<= int("8")):
                    return "50"


                if ((getCable(self)=="6") and getCircuitState(self)<= int("9")):
                    return "40"
                #10
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("10")):
                    return "32"
                #11
                if ((getCable(self)=="4") and getCircuitState(self)<= int("11")):
                    return "40"
                if ((getCable(self)=="10") and getCircuitState(self)<= int("11")):
                    return "50"
                #13
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("13")):
                    return "32"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("13")):
                    return "63"
                #16
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("16")):
                    return "40"
                if ((getCable(self)=="6") and getCircuitState(self)<= int("16")):
                    return "50"
                #18
                if ((getCable(self)=="10") and getCircuitState(self)<= int("18")):
                    return "63"
                #19
                if ((getCable(self)=="4") and getCircuitState(self)<= int("19")):
                    return "50"
                #19
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("21")):
                    return "40"
                #24
                if ((getCable(self)=="16") and getCircuitState(self)<= int("24")):
                    return "80(NZ)"
                #24
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("26")):
                    return "63"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("27")):
                    return "50"
                
                if ((getCable(self)=="16") and getCircuitState(self)<= int("28")):
                    return "82(AUS)"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("31")):
                    return "63"

                if ((getCable(self)=="10") and getCircuitState(self)<= int("32")):
                    return "80(NZ)"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("32")):
                    return "80(NZ)"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("36")):
                    return "50"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("36")):
                    return "50"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("38")):
                    return "80(AUS)"

                
                if ((getCable(self)=="16") and getCircuitState(self)<= int("43")):
                    return "100(NZ)"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("44")):
                    return "63"
                    
                if ((getCable(self)=="16") and getCircuitState(self) <= int("46")):
                    return "100(AUS)"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("48")):
                    return "80(NZ)"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("55")):
                    return "80(AUS)"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("56")):
                    return "80(NZ)"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("58")):
                    return "100(NZ)"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("59")):
                    return "63"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("63")):
                    return "100(AUS)"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("64")):
                    return "80(AUS)"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("64")):
                    return "80(AUS)"
                
                if ((getCable(self)=="16") and getCircuitState(self) <= int("70")):
                    return "125"
                
                
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("79")):
                    return "80(NZ)"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("85")):
                    return "100(NZ)"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("92")):
                    return "80(AUS)"

                if ((getCable(self)=="6") and getCircuitState(self)<= int("92")):
                    return "100(AUS)"

                if ((getCable(self)=="16") and getCircuitState(self) <= int("92")):
                    return "150"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("95")):
                    return "125"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("99")):
                    return "100(NZ)"             

                if ((getCable(self)=="1.5") and getCircuitState(self) >= int("100")):
                    return "80(NZ), 80(AUS), 100(NZ), 100(AUS), 125 or 150"
                
                if ((getCable(self)=="2.5") and getCircuitState(self) >= int("100")):
                    return "100(NZ), 100(AUS), 125 or 150"                       

                if ((getCable(self)=="4") and getCircuitState(self) >= int("100")):
                    return "100(AUS), 125 or 150"
    
                if ((getCable(self)=="6") and getCircuitState(self) >= int("100")):
                    return "125 or 150"
                
                if ((getCable(self)=="10") and getCircuitState(self) >= int("100")):
                    return "150"
                    
            if (getConduitType(self)=="Corflo conduit"):
                if ((getCable(self)=="16") and getCircuitState(self)<= int("43")):
                    return "100(NZ)"
                
                if ((getCable(self)=="16") and getCircuitState(self)<= int("45")):
                    return "100(AUS)"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("60")):
                    return "100(AUS)"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("89")):
                    return "100(AUS)"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("58")):
                    return "100(NZ)"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("85")):
                    return "100(NZ)"
                
                if ((getCable(self)=="4") and getCircuitState(self)>= int("100")):
                    return "100(NZ)"
                
                if ((getCable(self)=="4") and getCircuitState(self)>= int("100")):
                    return "100(NZ)"
                
                if ((getCable(self)=="16") and getCircuitState(self)<= int("67")):
                    return "125"
                
                if ((getCable(self)=="10") and getCircuitState(self)<= int("97")):
                    return "125"
                
                if ((getCable(self)=="16") and getCircuitState(self)<= int("88")):
                    return "150"

                if (((getCable(self)=="1.5" or (getCable(self)=="2.5"))) and getCircuitState(self) >= int("100")):
                    return "100(NZ), 100(AUS), 125 or 150"
                    
                if ((getCable(self)=="4") and getCircuitState(self) >= int("100")):
                    return "100(AUS), 125 or 150"
                    
                if ((getCable(self)=="6") and getCircuitState(self) >= int("100")):
                    return "125 or 150"
                    
                if ((getCable(self)=="10") and getCircuitState(self) >= int("100")):
                    return "150"
                
                if ((getCable(self)=="630") and getCircuitState(self)<= int("1")):
                    return "100(NZ) or 100(AUS)"
                
                if ((getCable(self)=="400" or getCable(self)=='500') and getCircuitState(self)<= int("3")):
                    return "100(NZ) or 100(AUS)"               
                if ((getCable(self)=="630") and getCircuitState(self)<= int("3")):
                    return "125"
                
                if ((getCable(self)=="300") and getCircuitState(self)<= int("4")):
                    return "100(NZ) or 100(AUS)"               
                if ((getCable(self)=="500") and getCircuitState(self)<= int("4")):
                    return "125"
                if ((getCable(self)=="630") and getCircuitState(self)<= int("4")):
                    return "150"
                
                if ((getCable(self)=="240") and getCircuitState(self)<= int("5")):
                    return "100(NZ) or 100(AUS)"               
                if ((getCable(self)=="400") and getCircuitState(self)<= int("5")):
                    return "125"
                
                if ((getCable(self)=="185") and getCircuitState(self)<= int("6")):
                    return "100(NZ) or 100(AUS)"               
                if ((getCable(self)=="300") and getCircuitState(self)<= int("6")):
                    return "125"
                if ((getCable(self)=="400" or getCable(self)=="500") and getCircuitState(self)<= int("6")):
                    return "150"
                
                if ((getCable(self)=="150") and getCircuitState(self)<= int("7")):
                    return "100(NZ)"               
                if ((getCable(self)=="240") and getCircuitState(self)<= int("7")):
                    return "125"
                
                if ((getCable(self)=="150") and getCircuitState(self)<= int("8")):
                    return "100(AUS)"  
                if ((getCable(self)=="300") and getCircuitState(self)<= int("8")):
                    return "150"  
                
                if ((getCable(self)=="95") and getCircuitState(self)<= int("11")):
                    return "100(NZ)"
                
                if ((getCable(self)=="120") and getCircuitState(self)<= int("10")):
                    return "100(AUS)" 
                if ((getCable(self)=="240") and getCircuitState(self)<= int("10")):
                    return "125" 
                if ((getCable(self)=="300") and getCircuitState(self)<= int("10")):
                    return "150" 
                
                if ((getCable(self)=="95") and getCircuitState(self)<= int("12")):
                    return "100(AUS)" 
                if ((getCable(self)=="150") and getCircuitState(self)<= int("12")):
                    return "125" 
                
                if ((getCable(self)=="185") and getCircuitState(self)<= int("13")):
                    return "150" 
                
                if ((getCable(self)=="120") and getCircuitState(self)<= int("14")):
                    return "125" 
                
                if ((getCable(self)=="150") and getCircuitState(self)<= int("16")):
                    return "150" 
                
                if ((getCable(self)=="95") and getCircuitState(self)<= int("17")):
                    return "125" 
                
                if ((getCable(self)=="70") and getCircuitState(self)<= int("15")):
                    return "100(NZ) or 100(AUS)" 
                
                if ((getCable(self)=="120") and getCircuitState(self)<= int("19")):
                    return "150" 
                if ((getCable(self)=="50") and getCircuitState(self)<= int("19")):
                    return "100(NZ)" 
                
                if ((getCable(self)=="70") and getCircuitState(self)<= int("20")):
                    return "125" 

                if ((getCable(self)=="70") and getCircuitState(self)<= int("23")):
                    return "125" 
                if ((getCable(self)=="95") and getCircuitState(self)<= int("23")):
                    return "150" 

                if ((getCable(self)=="35") and getCircuitState(self)<= int("24")):
                    return "100(NZ)" 
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("29")):
                    return "100(NZ)" 
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("30")):
                    return "100(AUS)"
                if ((getCable(self)=="70") and getCircuitState(self)<= int("30")):
                    return "150"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("25")):
                    return "100(AUS)"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("30")):
                    return "125"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("38")):
                    return "125"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("45")):
                    return "125"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("45")):
                    return "125"
                
                if ((getCable(self)=="50") and getCircuitState(self)<= int("40")):
                    return "150"
                
                if ((getCable(self)=="25") and getCircuitState(self)<= int("60")):
                    return "150"
                
                if ((getCable(self)=="35") and getCircuitState(self)<= int("50")):
                    return "150"
        
            if (getConduitType(self)=="Medium duty corrugated"):
        
                if ((getCable(self)=="4" or getCable(self)=="6" or getCable(self)=="10" or getCable(self)=="16") and getCircuitState(self)<= int("1")):
                    return "20"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("2")):
                    return "20"
                if ((getCable(self)=="6") and getCircuitState(self)<= int("2")):
                    return "25"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("2")):
                    return "32"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("3")):
                    return "20"
                if ((getCable(self)=="4") and getCircuitState(self)<= int("3")):
                    return "25"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("3")):
                    return "32"
            
                if ((getCable(self)=="1") and getCircuitState(self)<= int("4")):
                    return "20"
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("4")):
                    return "25"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("4")):
                    return "40"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("5")):
                    return "32"
                if ((getCable(self)=="10") and getCircuitState(self)<= int("5")):
                    return "40"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("6")):
                    return "25"
                if ((getCable(self)=="6") and getCircuitState(self)<= int("6")):
                    return "32"
                
                if ((getCable(self)=="1") and getCircuitState(self)<= int("7")):
                    return "25"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("8")):
                    return "32"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("11")):
                    return "32"
                
                if ((getCable(self)=="1") and getCircuitState(self)<= int("14")):
                    return "32"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("8")):
                    return "40"
                
                if ((getCable(self)=="1") and getCircuitState(self)<= int("23")):
                    return "40"
                
                if ((getCable(self)=="1.5") and getCircuitState(self)<= int("19")):
                    return "40"
                
                if ((getCable(self)=="2.5") and getCircuitState(self)<= int("14")):
                    return "40"
                
                if ((getCable(self)=="6") and getCircuitState(self)<= int("10")):
                    return "40"
                    
            if (getConduitType(self)=="Medium duty rigid UPVC conduit"):
    
                if ((getCable(self)=="16") and getCircuitState(self)<= int("0")):
                    return "16"

                if ((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6" or getCable(self)=="10") and getCircuitState(self)<= int("1")):
                    return "16"
                if ((getCable(self)=="6" or getCable(self)=="10" or getCable(self)=="16") and getCircuitState(self)<= int("1")):
                    return "20"
                if ((getCable(self)=="16") and getCircuitState(self)<= int("1")):
                    return "35"
                
                if ((getCable(self)=="4") and getCircuitState(self)<= int("2")):
                    return "20"
                if ((getCable(self)=="10") and getCircuitState(self)<= int("2")):
                    return "25"
                
                if ((getCable(self)=="1" or getCable(self)=="1.5") and getCircuitState(self)<= int("3")):
                    return "16"
                if ((getCable(self)=="2.5" ) and getCircuitState(self)<= int("3")):
                    return "20"
                if ((getCable(self)=="6" ) and getCircuitState(self)<= int("3")):
                    return "25"
                if ((getCable(self)=="16" ) and getCircuitState(self)<= int("3")):
                    return "32"
                
                if ((getCable(self)=="1.5" ) and getCircuitState(self)<= int("5")):
                    return "20"
                
                if ((getCable(self)=="1" ) and getCircuitState(self)<= int("6")):
                    return "20"
                
                if ((getCable(self)=="4" ) and getCircuitState(self)<= int("4")):
                    return "25"
                
                if ((getCable(self)=="2.5" ) and getCircuitState(self)<= int("6")):
                    return "25"
                
                if ((getCable(self)=="1.5" ) and getCircuitState(self)<= int("8")):
                    return "25"
                
                if ((getCable(self)=="1" ) and getCircuitState(self)<= int("10")):
                    return "25"
                
                if ((getCable(self)=="10" ) and getCircuitState(self)<= int("4")):
                    return "32"
                
                if ((getCable(self)=="6" ) and getCircuitState(self)<= int("6")):
                    return "32"
                
                if ((getCable(self)=="4" ) and getCircuitState(self)<= int("7")):
                    return "32"
                
                if ((getCable(self)=="2.5" ) and getCircuitState(self)<= int("11")):
                    return "32"
                
                if ((getCable(self)=="1.5" ) and getCircuitState(self)<= int("14")):
                    return "32"
                
                if ((getCable(self)=="1" ) and getCircuitState(self)<= int("17")):
                    return "32"

                if ((getCable(self)=="16" ) and getCircuitState(self)<= int("5")):
                    return "40"
                
                if ((getCable(self)=="10" ) and getCircuitState(self)<= int("7")):
                    return "40"
                
                if ((getCable(self)=="6" ) and getCircuitState(self)<= int("10")):
                    return "40"
                
                if ((getCable(self)=="4" ) and getCircuitState(self)<= int("12")):
                    return "40"
                
                if ((getCable(self)=="2.5" ) and getCircuitState(self)<= int("17")):
                    return "40"
                
                if ((getCable(self)=="1.5" ) and getCircuitState(self)<= int("23")):
                    return "40"
                
                if ((getCable(self)=="1" ) and getCircuitState(self)<= int("28")):
                    return "40"
                
                if ((getCable(self)=="1" ) and getCircuitState(self)<= int("45")):
                    return "50"
                
                if ((getCable(self)=="1.5" ) and getCircuitState(self)<= int("38")):
                    return "50"
                
                if ((getCable(self)=="2.5" ) and getCircuitState(self)<= int("28")):
                    return "50"
                
                if ((getCable(self)=="4" ) and getCircuitState(self)<= int("20")):
                    return "50"
                
                if ((getCable(self)=="6" ) and getCircuitState(self)<= int("17")):
                    return "50"
                
                if ((getCable(self)=="10" ) and getCircuitState(self)<= int("11")):
                    return "50"
                
                if ((getCable(self)=="16" ) and getCircuitState(self)<= int("8")):
                    return "50"
                    
            else:
                return "Invalid input, please check again"
        
        self.conduitResult.configure(text="Number of Conduits: \n" + circuitNo(self), bg='green2', borderwidth="1", relief="raised")
        
        if (circuitNo(self)=="Invalid input, please check again"):
            self.conduitResult.configure(bg='firebrick1', borderwidth="2", relief="sunken")
            self.circuitNo.configure(text="Number of Circuits: - "+ self.getCircuit.get(), font='Helvetica 9 bold')
            
master = Tk()
master.title("Guide to Max No. of Single-Core Sheather Calbes Installed in Conduit. Table C10")
master.geometry("700x275")
app = Application(master)

master.mainloop()



