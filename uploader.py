import os
import time as T

def addtests(fname):
    all_files=os.listdir(fname+"\\input\\")

    n=int(input("  How many Testfiles you wish to add? (Enter integer value)\n  "))

    if n<1:
        print("\n"+"-"*85+"\n")
        print("ERROR : INVALID NUMBER OF TESTFILES")
        T.sleep(.5)
        print("\nAborted Adding Testfiles")
        T.sleep(.2)
        return
    
    c=len(all_files)+1

    print("\n  Notepad will pop-up for entering test data of each file.")
    T.sleep(.8)
    print("  Enter or paste appropriate data as per instruction in the Notepad.")
    T.sleep(.8)
    print("  Save it, and then close the Notepad.\n")
    T.sleep(.8)

    for i in range(1,n+1):

        #file name
        name=str(c)+'.txt'

        print("-"*85+"\n")
        print("UPLOADING NEW TESTFILE NO.",i)

        #get input data
        print("\n  Copy the input data for testfile no.",i)
        T.sleep(1)
        print("  Press ENTER if copied (or if you want to enter data manually)")
        input()
        print("  Notepad will pop-up, paste the input data there and save it.")
        T.sleep(1)

        os.system("python file_maker.py >"+fname+"\\input\\"+name)
        print("  If you have saved the data then close Notepad to continue.")
        os.system("notepad "+fname+"\\input\\"+name)

        #get output data
        print("\n  Copy the output data for testfile no.",i)
        T.sleep(1)
        print("  Press ENTER if copied (or if you want to enter data manually)")
        input()
        print("  Notepad will pop-up, paste the output data there and save it.")
        T.sleep(1)

        os.system("python file_maker.py >"+fname+"\\output\\"+name)
        print("  If you have saved the data then close Notepad to continue.")
        os.system("notepad "+fname+"\\output\\"+name)
        
        c+=1

    T.sleep(.3)
    print("\n"+"-"*85+"\n")
    T.sleep(.1)
    print("  Added",n,"testfiles")


        
