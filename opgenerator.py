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
    
    T.sleep(5.01)
    
    if kill_child_processes(pid):
        return 2

    return 1 if prc.returncode else 0


def generateop(fname,cname):
    all_files=os.listdir(fname+"\\input\\")    

    #generating execution command
    cmd=''

    #cpp
    if cname[-1]=='p':
        print("\n"+"-"*85+"\n")
        print("Compiling Output Generator Program")
        err=subprocess.getoutput("g++ -Wall -std=gnu++14 "+fname+"\\"+cname+" -o "+fname+"\\opgen")
        if err=="":
            print("Compilation Successful")
        else:
            print("Compilation Error:")
            print(err)
            print("\n Output Generation Aborted")
            return False
        cmd=fname+'\\opgen <'

    #python
    else:
        cmd='python '+fname+"\\"+cname+' <'
            
    n=len(all_files)
    c=1
    for i in range(1,n+1):

        #file name
        name=str(c)+'.txt'
        print("\n"+"-"*85+"\n")
        print("GENETATING OUTPUT FOR INPUT FILE NO.",i)
        
        command=cmd+fname+"\\input\\"+name+" >"+fname+"\\output\\"+name+" 2>"+fname+"\\stderr\\"+name
        res=run(command)
        if res:
            os.system("del "+fname+"\\output\\"+name)
            print("Output Generation Aborted")
            print("ERROR ")
            if res==2 : print("It took too long to generate this output file. <-_->")
            return False
        c+=1

    T.sleep(.3)
    print("\n"+"-"*85+"\n")
    T.sleep(.1)
    print("  Generated",n,"output files.")
    return True


        
