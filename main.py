#Importing required modules and files
#######################################################################################################

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import time as T
import os, sys

from uploader import *
from ipgenerator import *
from opgenerator import *
from checker import *


#Definitions
#######################################################################################################

st=PorterStemmer()
ll="\n  "
stop_words=set(stopwords.words('english'))
cwd=os.getcwd()+'\\'
syn={}

#print horzontal lines
def line():
    print("\n"+"-"*171+"\n")
def halfline():
    print("\n"+"-"*85+"\n")


#About
############################
def about():
    print("  OFFLINE JUDGE is an utility application for offline testing and testcase generation.")
    T.sleep(.5)
    print("\n  OFFLINE JUDGE can be used for single problem in one run.")
    T.sleep(.5)

#Functionalities
############################
def func():
    
    print("  List of provided functionalities:")
    T.sleep(.5)
    print("    -> Creating Input Files (with given program)")
    T.sleep(.5)
    print("    -> Creating Output Files based on Input Files (with given program)")
    T.sleep(.5)
    print("    -> Adding Testfiles")
    T.sleep(.5)
    print("    -> Testing Program/Code on saved Testfiles")
    T.sleep(.5)

#Languages
############################
def lang():
    print("  Supported Languages:")
    T.sleep(.5)
    print("    -> C++14")
    T.sleep(.5)
    print("    -> Python 3")
    T.sleep(.5)

#remove punctuations and stopwords
############################
def getclean(sentence):
    tokens=nltk.word_tokenize(sentence)
    words=[word for word in tokens if (word.isalpha()) and (word not in stop_words)]
    return words
    
#stemming all words in a sentence
############################
def getstem(sentence):
    words=getclean(sentence)
    words=[st.stem(word) for word in words]
    return words

#generate set of synonyms of given word
############################
def word_syn(word):
    syns=set()
    for synonym in wordnet.synsets(word):
        for l in synonym.lemmas():
            syns.add(st.stem(l.name()))
    return syns
    
#save synonyms of required words
############################
def generate_synonyms():
    syn['generate']=word_syn('generate')|word_syn('create')|word_syn('form')|word_syn('generator')
    syn['input']=word_syn('input')
    syn['output']=word_syn('output')
    syn['add']=word_syn('add')|word_syn('upload')
    syn['submit']=word_syn('test')|word_syn('submit')|word_syn('check')|word_syn('submission')|word_syn('solve')|word_syn('verify')
    syn['yes']=word_syn('yes')|word_syn('yeah')|{'yup','yep'}
    syn['no']=word_syn('no')|word_syn('not')|{'nope'}
    syn['testcase']={'testcase','testfile','case','file','data','testdata'}
    syn['exit']=word_syn('exit')|word_syn('close')|word_syn('stop')|word_syn('done')|word_syn('nothing')
    syn['exit']-=word_syn('make')|{'check'}
    syn['delete']=word_syn("delete")|word_syn("discard")|word_syn('overwrite')|word_syn('update')|word_syn('change')

#get problem folder
############################
def getfolder():
    name=input("  Enter problem name (or problem folder name): ")
    name=getstem(name)
    name=''.join(name)
    name=st.stem(name)
    if not os.path.isdir(cwd+name):
        os.system("mkdir "+name)
    if not os.path.isdir(cwd+name+'\\input'):
        os.system("mkdir "+name+"\\input")
    if not os.path.isdir(cwd+name+'\\output'):
        os.system("mkdir "+name+"\\output")
    if not os.path.isdir(cwd+name+'\\result'):
        os.system("mkdir "+name+"\\result")
    if not os.path.isdir(cwd+name+'\\stderr'):
        os.system("mkdir "+name+"\\stderr")
    print("  Operating on folder :",name,end=ll)
    return name


#help
############################
def need_help():
    print("\n  NEED HELP!  <*_*>")
    halfline()
    T.sleep(.5)
    func()
    T.sleep(.5)
    halfline()
    print("  Enter anything relevant to the functionality you want to use.")
    T.sleep(.5)
    print("  OR...... Tell to quit if you are done! <^_^>")
    T.sleep(.5)

#check old test files
############################
def old_data(fname):
    all_files=os.listdir(fname+"\\input\\")
    if len(all_files):
        print("  Some test files already exist.")
        print("  Do you want to DELETE them?",end=ll)
        ans=set(getstem(input()))
        if len(ans&syn['yes']) or len(ans&syn['delete']):
            os.system("del /S /Q "+fname+"\\input")
            os.system("del /S /Q "+fname+"\\output")
        halfline()

#check if input exists
############################
def inp_exists(fname):
    all_files=os.listdir(fname+"\\input\\")
    if len(all_files)==0:
        print("ERROR: NO INPUT FILES FOUND")
        T.sleep(.5)
        print("\nTask Aborted",end=ll)
        T.sleep(.5)
        halfline()
    return len(all_files)

#check if output id valid
############################
def op_exists(fname,ips):
    all_files=os.listdir(fname+"\\output\\")
    if len(all_files)==0:
        print("ERROR: NO OUTPUT FILES FOUND")
        T.sleep(.5)
        print("\nTask Aborted",end=ll)
        T.sleep(.5)
        halfline()
    if len(all_files)<ips:
        print("ERROR: OUTPUT IS MISSING/NOT GENERATED FOR SOME INPUTS")
        T.sleep(.5)
        print("\nTask Aborted",end=ll)
        T.sleep(.5)
        halfline()
    return len(all_files)

#ask for language
############################
def ask_lang():
    lang()
    s=input("  Select a language(Enter name or extension of language): ")
    if 'py' in s: return 1
    if 'c' in s: return 2
    print("ERROR: INVALID LANGUAGE")
    T.sleep(.5)
    print("\nTask Aborted")
    halfline()
    return 0

#upload code file
############################
def upload_code(cloc,desc):
    halfline()
    T.sleep(.5)
    print("UPLOADING",desc.upper(),"PROGRAM")
    os.system("python file_maker.py >"+cloc)
    print("\n  Notepad will pop-up for entering the program.")
    T.sleep(.8)
    print("  Enter or paste program in Notepad.")
    T.sleep(.8)
    print("  Save it, and then close the Notepad window to continue.\n")
    T.sleep(.8)
    os.system("notepad "+cloc)
    print(desc,"has been uploaded")
    halfline()
def create_file(fname,cname,desc):
    cloc=fname+"\\"+cname
    if os.path.exists(cwd+cloc):
        print(" ",desc,"already exists for selected language.")
        print("  Do you want to DELETE it?",end=ll)
        ans=set(getstem(input()))
        if len(ans&syn['yes']) or len(ans&syn['delete']):
            upload_code(cloc,desc)
    else:
        upload_code(cloc,desc)


#submission
def submission(task):
    if len(syn['submit']&task):
        line()
        print("TASK: SUBMIT SOLUTION\n")
        ips=inp_exists(fname)
        if ips:
            if op_exists(fname,ips):
                l=ask_lang()
                if l:
                    tl=float(input('\n  Time limit per test(in seconds): '))
                    cname="solution"
                    cname+='.py' if l==1 else '.cpp'
                    create_file(fname,cname,"Solution")
                    submit(fname,cname,tl*(4 if l==1 else 1))
                    return True
    return False
        


#Input and Perform Task
############################
def dotask(fname):
    print('\n  What do you wish to do?',end=ll)
    task=set(getstem(input()))

    #exit
    if len(syn['exit']&task):
        return False
    
    #generate input/output or both
    if len(syn['generate']&task):

        #input generation
        if len(syn['input']&task):
            line()
            print("TASK: INPUT GENERATION\n")
            old_data(fname)
            l=ask_lang()
            if l:
                cname='ipgen'
                cname+='.py' if l==1 else '.cpp'
                create_file(fname,cname,"Input Generator")
                l=generateip(fname,cname)
            if not l: return True

        #output generation
        if len(syn['output']&task):
            line()
            print("TASK: OUTPUT GENERATION\n")
            if inp_exists(fname):
                l=ask_lang()
                if l:
                    cname='opgen'
                    cname+='.py' if l==1 else '.cpp'
                    create_file(fname,cname,"Output Generator")
                    generateop(fname,cname)

        else: submission(task)

    #add testfile
    elif len(syn['add']&task):
        line()
        print("TASK: ADDING TESTFILES\n")
        old_data(fname)
        addtests(fname)

    #submit a solution
    elif submission(task):
        pass
                
    
    #need help?
    else:
        need_help()
    
    return True


#Interaction
#######################################################################################################
if __name__=="__main__":
    #clear screen
    os.system("cls")

    #Instrutucting User
    ############################
    print("\n  Welcome to the OFFLINE JUDGE!")
    T.sleep(.5)
    line()

    about()
    T.sleep(.5)
    halfline()

    func()
    T.sleep(.5)
    halfline()

    lang()

    generate_synonyms()

    line()
    fname=getfolder()
    T.sleep(.5)

    while dotask(fname):
        line()
        pass

    #exit section
    ############################
    T.sleep(.5)
    print("\n"+'-x'*85+'-')
    T.sleep(.5)
    print('\n  Thank You for using OFFLINE JUDGE! <^_^>')
    T.sleep(.5)
    print("\n  Press ENTER to exit.")
    input()














