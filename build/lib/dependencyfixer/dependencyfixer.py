def fix(depend,instantkill=False,auto=True,verbose=False):
    def trace(s):
        if verbose:
            print(s)
    result=0
    leftdep=[]
    if not auto:
        depin=input("Module missing ! >"+str(depend)+"!\nIf you want,I can install it by myself automatically.\nTo do so I need active internet connection, so make sure you have a working internet connection!\n Enter Y for yes and N for no?")
    else:
        depin='y'
    if(depin=="y" or depin=="Y"):
        import pip._internal.cli.main
        for go in depend:
            package=str(go)
            x=pip._internal.cli.main.main(['install', '--quiet',package,'--user'])
            if not x:
                trace("\033[92m ( # )Successfuly installed Module '"+package+"' !\033[0m")
            else:
                leftdep.append(go)
                trace("\033[91m ( # ) Sorry I was unable to install that module "+package+"! Please try running '\033[0m \033[94m pip install "+package+" \033[0m \033[91m' in your command line(terminal or cmd)\033[0m")  
        if len(leftdep)==0:
            trace("############################################\n\n\n\033[92mAll given Modules Installed!\033[0m")
            result=1
        elif len(leftdep)<len(depend) and len(leftdep)!=0:
            result=-1
            trace("############################################\n\n\n\033[93m"+str(len(leftdep))+" Modules can not be installed !\033[0m\n\033[4mLeft Modules are :\033[0m")
            for w in leftdep:
                trace("\033[93m *"+str(w)+" \033[0m")
            trace("Try Fixing these by yourself.")
        elif len(leftdep)==len(depend):
            trace("############################################\n\n\n\033[91mSomething Went wrong!\033[0m \n\033[4mNo Dependencies Fixed !\nLeft Modules are :\033[0m")
            for w in leftdep:
                trace("\033[93m *"+str(w)+" \033[0m")
            result=0
    else:
        trace("############################################\n\n\n\033[91mUser denied installation of packages!\033[0m \n\033[4mNo Dependencies Fixed !\nLeft Modules are :\033[0m")   
        result=0
    if result!=1 and instantkill:
        exit()
    return result,leftdep # returns three type of values 0(no success),1(all success),-1(partial success) and a list with left dependencies that can not be fixed by function
# Dependencyfixer function END

if __name__ == "__main__":
    depend=[]
    x=input("Enter Module to be installed:")
    depend.append(x)
    ww=input("Want to add more module ? Y for yes and N for no. : ")
    if ww=="Y" or ww=="y":
        xx=1
        while(xx>0):
            x=input("Enter module to be fixed:")
            depend.append(x)
            we=input("Want to add more module ? Y for yes and N for no. : ")
            if we!="Y" and we!="y":xx=-1
    print("Modules to be instlled : "+str(depend))
    q=input("Fix ? Y for yes N for no. : ")
    if q=="y" or q=="Y":fix(depend)