import os

directory = "Trash"
if not os.path.exists(directory):
    os.makedirs(directory)
StillFiles = ['clean.py', '.git', 'clean.exe', 'Cisco Packet Tracer.lnk', 'StarCraft II.lnk', 'Trash', 'REAPER (x64).lnk', 'AnyDesk (4).exe','CleanDesktop.py', 'Guitar Pro 6.lnk', 'Guitar Rig 6.lnk', 'Hyper.lnk', 'Muzlo2', 'New ara', 'RX Pro Audio Editor.lnk', 'TabletDriverV0.2.3',
'График на ноябрь_n.xlsx', 'Планшет.txt', 'Текста мб', 'Учеба общая', 'Чечня', 'StarCraft II.lnk',
'']
AllFiles =  os.listdir()
print(AllFiles)
for x in AllFiles:
    if (not x in StillFiles):
        dist = directory + "/" + x
        if(not os.path.exists(dist)):
            os.rename(x, dist)
        else:

            count = 1
            defdist = dist.split('.')
            dist = defdist[0] + '(' + str(count) + ').txt' 
            
            while(True):
                if(os.path.exists(dist)):
                    count += 1
                    dist = defdist[0] + '(' + str(count) + ').txt'
                    continue
                else:
                    os.rename(x, dist)
                    break

print('Done!')
test = input()