
#Welcome to vastauine
#This is a sample code on Raspberry PI (Client End)
#Feel free to edit this code to meet your requirenment 
#READ THE LICENCE BEFORE YOU USE OR REPRODUCE THIS CONTENT
#this is a very basic program and not highly realible more realible versions to be roll out sooner 
#Vastauine holds no WARRENTY on use of this Product 
# This Program will check for updates if available will ask Shell to update
print('******************************************************')
print('---------------Welcome to Vastauine-------------------')
print('______________Download version 1.0____________________')
print('******************************************************')


import os,sys,time,urllib2
def version_check(MaxRetry):
    while(MaxRetry >= 0):
        try:
            version=urllib2.urlopen("http://vastauine.com/update/version").read()
            return version
        except Exception:
            print('Internet connectivity Error Retrying in 5 seconds :');print(MaxRetry)
            time.sleep(5)
            MaxRetry=MaxRetry - 1
    print('Connect to Internet and Retry Later ')
    print('######--- Closing Vastauine -- ######')
    exit()
    
def download_vastauine(MaxRetry):
    while(MaxRetry >= 0):
        try:
            os.system("sudo wget http://vastauine.com/vastauine.tar")
            return True
        except OSError:
            print('Error downloading file Check Internet connection. Retrying Download in 5 Seconds :')
            time.sleep(5)
            MaxRetry=MaxRetry - 1
    print('Connect to Internet and Retry Later ')
    print('######--- Closing Vastauine -- ######')
    exit()	
    

def checkStatus():
    # Function Returns False if no new updates
    # True if Update Available or existing file corrupt
    # 404 if Internet Connectivity Problem
    print("Checking for system updates . . .")    
    version=version_check(5)   
    if os.path.exists("vastauine/health.py")== True:
        try:        
            from vastauine.health import health
        except ImportError:
            print("Import Error")
            return (True)
        else:
            log=health()
            if log  == version:
                print('System is uptodate')
                return (False)
                #os.system('python vastauine/')
            else:
                # We may want to solve problem of Recheck First 
                print('Some Thing is not Good < Consider Update>')
                return (True)
    elif os.path.exists("vastauine/health.py")== False:
        print("No pakages currently Installed .. ")
        print("Updating  .. ")
        return (True)
    else:
	print("!!!!FATAL ERROR : Some components might have went missing")
        return(False)

    
def install():
    if os.path.exists("vastauine.tar")== True:
        try:
            os.system("sudo rm vastauine.tar")
        except OSError:
            print (OSError + "")
            return(False)
        else:
            print("Removed Dust")
    else:
        print("")

    if download_vastauine(5) == True:
        print("Sucessfully downloaded update")
    else:
        return(False)        
        
    try:
        os.system("sudo tar -xf vastauine.tar")
    except OSError:
        print (OSError + "Error occured while extracting files")
        return(False)
    else:
        print("Device sucessfully updated")

    try:
        os.system("sudo rm  vastauine.tar")
    except OSError:
        print (OSError + "Error removing addational packages")
        return(False)
    else:
        print("Device sucessfully updated")

    return (True)
    

        

def update():
    if os.path.exists("vastauine/")== True:
        try:
            os.system("sudo rm -r vastauine")
        except OSError:
            print (OSError + "Error occured while removing vastauine")
            exit()
        else:
            print("Sucessfully removed existing version")
            install_status=install()
            if install_status == True:
                return (True)
            elif (install_status) == False:
                return (False)
            else:
                print("Unknown Error")            
    else:
        install_status=install()
        
        if install_status == True:
            return (True)
        elif install_status == False:
            return (False)
        else:
            print("Unknown Error") 

def initilization():
    log_status=checkStatus()
    if log_status == True :
        log_update=update()
        if log_update == True:
            print('Sucessfull updated initilization')
        elif log_update == False:
            print('Update Failed')
        else:
            print('Unknown error Occured')
    elif log_status == False :
        print("No new update Available")
        from vastauine import communication 
        start()
        #communication()
    else:
        print('Unknown error occured') 

initilization()
