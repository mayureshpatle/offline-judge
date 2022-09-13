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

def run(cmd,tl):
    prc=subprocess.Popen(cmd,shell=True)
    pid=prc.pid
    
    T.sleep(5*tl+0.01)
    
    if kill_child_processes(pid):
        return 2

    return 1 if prc.returncode else 0


def submit(fname,cname,tl):
    all_files=os.listdir(fname+"\\input\\")    

    #generating execution command
    cmd=''

    #cpp
    if cname[-1]=='p':
        print("\n"+"-"*85+"\n")
        print("Compiling Solution Program")
        err=subprocess.getoutput("g++ -Wall -std=gnu++14 "+fname+"\\"+cname+" -o "+fname+"\\soln")
        if err=="":
            print("Compilation Successful")
        else:
            print("Compilation Error:")
            print(err)
            print("\nSOLUTION REJECTED")
            return
        cmd=fname+'\\soln <'

    #python
    else:
        cmd='python '+fname+"\\"+cname+' <'
            
    n=len(all_files)
    c=1
    for i in range(1,n+1):

        #file name
        name=str(c)+'.txt'
        print("\n"+"-"*85+"\n")
        print("RUNNING ON TESTCASE",c)
        
        command=cmd+fname+"\\input\\"+name+" >"+fname+"\\result\\"+name+" 2>"+fname+"\\stderr\\"+name
        res=run(command,tl)
        if res:
            print("SOLUTION REJECTED")
            if res==2 : print("TLE - Time Limit Exceed")
            else: print("RE - Runtime Error")
            return

        #compare result
        src=open(fname+"\\output\\"+name)
        dst=open(fname+"\\result\\"+name)
        exp=[line.strip() for line in src]
        res=[line.strip() for line in dst]
        src.close()
        dst.close()
        if exp==res:
            print("PASSED TESTCASE",i)
        else:
            print("WA - Wrong Answer on testcase",c)
            print("\nSOLUTION REJECTED")
            l=0
            while(l<len(res) and res[l]==exp[l]): l+=1
            print("Total lines printed:",len(res))
            print("Total lines expected:",len(exp))
            print("WA on line",l+1)
            return
            
        c+=1

    T.sleep(.3)
    print("\n"+"-"*85+"\n")
    T.sleep(.1)
    print("AC - Accepted\n  Congratulations!!!! SOLUTION PASSED ALL TESTCASES")
    return


        
