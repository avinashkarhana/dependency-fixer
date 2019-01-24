# Dependencyhandler function START        
def dependencyhandler(depend):
            depin=input("Dependency missing ! named "+str(depend)+" !\nIf you want,I can install it by myself automatically.\nTo do so make sure you have a working internet connection because I will Need it to install dependency.\n Y for yes and N for no?")
            if(depin=="y" or depin=="Y"):
                from pip._internal import main
                leftdep=[]
                for go in depend:
                    package=str(go)
                    x=main(['install', package])
                    if not x:
                        print("Successfuly fixed dependecy "+package+" !")
                    else:
                        leftdep.append(go)
                        print("Sorry I was unable to install that dependency "+package+"! Please try running 'pip install "+package+"' in your command line(terminal or cmd)")
                    if len(leftdep)==0:
                        print("############################################\n\n\nAll dependencies Fixed !")
                        result=1
                    elif len(leftdep)<len(depend) and not len(leftdep):
                        result=-1
                        print("############################################\n\n\n"+str(len(leftdep))+" Dependencies can not be fixed !\nLeft dependecies are ")
                        for w in leftdep:
                            print(str(w)+", ")
                        print("Try Fixing these by yourself.")
                    elif len(leftdep)==len(depend):
                        print("############################################\n\n\nNo Dependencies Fixed !\nLeft dependecies are ")
                        for w in leftdep:
                            print("#"+str(w))
                        result=0
            else:
                result=0
            return(result,leftdep) # returns three type of values 0(no success),1(all success),-1(partial success) and a list with left dependencies that can not be fixed by function
# Dependencyhandler function END

if __name__ == "__main__":
    depend=[]
    x=input("Enter Dependency to be fixed:")
    depend.append(x)
    ww=input("Want to add more dependency ? Y for yes and N for no. : ")
    if ww=="Y" or ww=="y":
        xx=1
        while(xx>0):
            x=input("Enter Dependency to be fixed:")
            depend.append(x)
            we=input("Want to add more dependency ? Y for yes and N for no. : ")
            if we!="Y" and we!="y":xx=-1
    print("Dependencies to be fixed : "+str(depend))
    q=input("Fix ? Y for yes N for no. : ")
    if q=="y" or q=="Y":dependencyhandler(depend)