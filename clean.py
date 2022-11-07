import os
def GetUsername():
    return os.getenv("username")

def GetConfigPath(username):
    
    return f"C:/Users/{username}/Documents/DesktopCleaner"

def CreateConfig(configPath):
    if (os.path.exists(configPath) == False):
        os.makedirs(configPath)
        print("Created")


def GetPathes(configPath):
    count = 0
    whiteListPath = configPath + "/whitelist.cfg"
    if (os.path.exists(whiteListPath) == False):
        cfg = open(whiteListPath, "w")
        cfg.write("clean.exe\nTrash\nReadme.txt\nYouCanAddMore\n")
        cfg.close()
        print("Created")
        count += 1
    trashDirPath = configPath + "/trashdir.cfg"
    if (os.path.exists(trashDirPath) == False):
        cfg = open(trashDirPath, "w")
        cfg.write(f"C:/Users/{username}/Desktop/Trash")
        cfg.close()
        print("Created")
        count +=1
    cleanDirPath = configPath + "/сleandir.cfg"
    if (os.path.exists(cleanDirPath) == False):
        cfg = open(cleanDirPath, "w")
        cfg.write(f"C:/Users/{username}/Desktop")
        cfg.close()
        print("Created")
        count +=1
    if(count != 0):
        quit()
    return whiteListPath, trashDirPath, cleanDirPath

def GetDirectories(whiteListPath, trashDirPath, cleanDirPath):
    file = open(trashDirPath)
    trashDirectory = file.readline()
    file.close()

    file = open(cleanDirPath)
    cleanDirectory = file.readline()
    file.close()


    file = open(whiteListPath, encoding='utf-8')
    StillFiles = file.readlines()
    file.close()
    trashDirectoryFolder = trashDirectory.split('/')
    lenth = len(trashDirectoryFolder)
    StillFiles.append(trashDirectoryFolder[lenth-1])
    return trashDirectory, cleanDirectory, StillFiles


username = GetUsername()
configPath = GetConfigPath(username)
CreateConfig(configPath)
whiteListPath, trashDirPath, cleanDirPath = GetPathes(configPath)
trashDirectory, cleanDirectory, StillFiles = GetDirectories(whiteListPath, trashDirPath, cleanDirPath)




count = 0
for x in StillFiles:
    StillFiles[count] = x.strip()
    count+=1

print(StillFiles)


if not os.path.exists(trashDirectory):
    os.makedirs(trashDirectory)

if(cleanDirectory == ""):
    AllFiles =  os.listdir()
else:
    AllFiles =  os.listdir(cleanDirectory)


for x in AllFiles:
    if (not x in StillFiles):
        dist = trashDirectory + "/" + x
        startingpoint = cleanDirectory + "/" + x
        if(not os.path.exists(dist)):
            os.rename(startingpoint, dist)
        else:

            count = 1
            defdist = dist.split('.')
            if(len(defdist) > 1):
                dist = defdist[0] + '(' + str(count) + ')' + '.' + defdist[1]
            else:
                dist = defdist[0] + '(' + str(count) + ')'
            
            while(True):
                if(os.path.exists(dist)):
                    count += 1
                    if(len(defdist) > 1):
                        dist = defdist[0] + '(' + str(count) + ')' + '.' + defdist[1]
                    else:
                        dist = defdist[0] + '(' + str(count) + ')'
                    continue
                else:
                    os.rename(startingpoint, dist)
                    break

print('Done!')
