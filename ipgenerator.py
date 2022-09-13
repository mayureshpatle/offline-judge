import os
import subprocess
import time as T
import multiprocessing as mp
import signal, psutil

def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for process in children:
        process.send_signal(sig)
    return len(children)

def run(cmd):
    noerr=False
    prc=subprocess.Popen(cmd,shell=True)
    pid=prc.pid
    
    tl = 15.01 if cmd[0]=='p' else 5.01
    T.sleep(tl)
    
    if kill_child_processes(pid):
        return 2

    return 1 if prc.returncode else 0


def generateip(fname,cname):
    all_files=os.listdir(fname+"\\input\\")

    n=int(input("  How many INPUT files you wish to generate? (Enter integer value)\n  "))

    if n<1:
        print("\n"+"-"*85+"\n")
        print("ERROR : INVALID NUMBER OF INPUT FILES")
        T.sleep(.5)
        print("\nInput Generation Aborted")
        T.sleep(.2)
        return
    

    #generating execution command
    cmd=''

    #cpp
    if cname[-1]=='p':
        print("\n"+"-"*85+"\n")
        print("Compiling Input Generator Program")
        err=subprocess.getoutput("g++ -Wall -std=gnu++14 "+fname+"\\"+cname+" -o "+fname+"\\ipgen")
        if err=="":
            print("Compilation Successful")
        else:
            print("Compilation Error:")
            print(err)
            print("\n Input Generation Aborted")
            return False
        cmd=fname+'\\ipgen >'

    #python
    else:
        cmd='python '+fname+"\\"+cname+' >'
            

    c=len(all_files)+1
    for i in range(1,n+1):

        #file name
        name=str(c)+'.txt'
        print("\n"+"-"*85+"\n")
        print("GENETATING NEW INPUT FILE NO.",i)
        
        command=cmd+fname+"\\input\\"+name+" 2>"+fname+"\\stderr\\"+name
        res=run(command)
        if res:
            os.system("del "+fname+"\\input\\"+name)
            os.system("del "+fname+"\\stderr\\"+name)
            print("Input Generation Aborted")
            print("ERROR ")
            if res==2 : print("It took too long to generate this input file. <-_->")
            return False
        c+=1

    T.sleep(.3)
    print("\n"+"-"*85+"\n")
    T.sleep(.1)
    print("  Generated",n,"input files.")
    return True


        
