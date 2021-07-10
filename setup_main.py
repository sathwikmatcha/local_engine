import json
import os

paths=[]
files=[]
levels=[]

def addPath():  
    
    folder_selected=input("Select Folder")

    if not(os.path.isdir(folder_selected)):
        print("Path doesn't exist...")
        return
    
    if(folder_selected in paths):
        print("path already added")

    else:
        
        fileName=input("Input name of JSON file: ")

        while(True):
            if(fileName in files):
                print("file name cannot be accepted")
                inp1=input("Input name of JSON file: ")
            else:
                break
       
        level=input("Input Level of Engine(Max,1,2,3,0) (Default:Max) :  ")
        options=["Max","1","2","3","0"]
       
        if(level not in options):
            level=options[0]
        if(level==""):
            level=options[0]

        files.append(fileName+".json")
        paths.append(folder_selected)
        levels.append(level)
        
        return

def remtFile():

    fileName=input("Input name of JSON file: ")
    fileName+=".json"
    
    if(fileName in files):
        ind=files.index(fileName)
        
        paths.pop(ind)
        files.pop(ind)
        levels.pop(ind)

    else:
        print("no file in list")

    return

def remtPath():

    folder_selected=input()

    if not(os.path.isdir(folder_selected)):
        print("Path doesn't exist...")
        return    
    
    if(folder_selected in paths):
        ind=paths.index(folder_selected)
        
        paths.pop(ind)
        files.pop(ind)
        levels.pop(ind)
    else:
        print("folder not present in the list")

    return 

def createJSON(paths,files,levels):
    
    obj={
            "path":"",
            "level":"",
            "name":""
        }
    
    arr=[]
    
    for i in range(len(paths)):

        obj['path']=paths[i]
        obj['name']=files[i]
        obj['level']=levels[i]
    
        arr.append(obj)
    
    main_dict={"table":arr}
    json_object=json.dumps(main_dict,indent=4)

    with open("main.json","w") as outfile:
        outfile.write(json_object)

    return
    
def list_():
    
    if(len(paths)==0):
        print("path/file/level does not exist")
        return
    
    for i in range(len(paths)):
        print("")
        print("")

        print("path: "+ str(paths[i]))
        print("level: "+ str(levels[i]))
        print("name: "+ str(files[i]))
    
    return



a=input()

while(True):

    if(a=="a"):
        addPath()
        a=input()
        continue
    if(a=="rp"):
        remtPath()
        a=input()
        continue
    if(a=="rf"):
        remtFile()
        a=input()
        continue
    if(a=="s"):
        createJSON(paths,files,levels)
        a=input()
        continue
    if(a=="l"):
        list_()
        a=input()
        continue
    if(a=="q"):
        exit(0)
