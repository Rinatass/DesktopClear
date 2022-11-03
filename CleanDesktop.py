import os

directory = "Trash"
if not os.path.exists(directory):
    os.makedirs(directory)
StillFiles = ['Cisco Packet Tracer.lnk', 'StarCraft II.lnk', 'Trash', 'REAPER (x64).lnk', 'CleanDesktop.py', 'AnyDesk (4).exe','CleanDesktop.py', 'Guitar Pro 6.lnk', 'Guitar Rig 6.lnk', 'Hyper.lnk', 'Muzlo2', 'New ara', 'RX Pro Audio Editor.lnk', 'TabletDriverV0.2.3',
'График на ноябрь_n.xlsx', 'Планшет.txt', 'Текста мб', 'Учеба общая', 'Чечня', 'StarCraft II.lnk',
'']
AllFiles =  os.listdir()
for x in AllFiles:
    if (not x in StillFiles):
        dist = directory + "/" + x
        os.rename(x, dist)
