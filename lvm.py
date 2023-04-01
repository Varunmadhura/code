import subprocess
import os.path
will = True
while will:
    print('1. create physical volume.\n2. create volume group\n3. create logical volume\n4. show volumes attached\n5. display physical volumes\n6. Display volume group\n7. display logical volume\n8.making file system \n9.checking file system \n10.extend size of lvm \n11.reduce size of lvm\n12.mount storage\n13.unmount storage\n0.Exit')
    t = int(raw_input())
    if t==0:
        will = False
        break
    elif t==1:
        name =raw_input('Enter name/path for volume: ')
        os.system("pvcreate {}".format(name))
        print("physical volume is created")n
    elif t==2:
        vgname =raw_input("Enter name for volume group: ")n
        pvname = raw_input("Enter physical volume name: ")
        os.system("vgcreate {} {}".format(vgname,pvname))
        os.system("vgextend {} {}".format(vgname,pvname))
        print("volume group created")
    elif t==3:
        lvmname=raw_input("Enter name for logical volume group: ")
        lvmsize=int(raw_input("Enter  size in G: "))
        vgname=raw_input('Enter volume group name: ')
        os.system("lvcreate --size {}G --name {} {}".format(lvmsize,lvmname,vgname))
    elif t==4:
        os.system("df -hT")
    elif t==5:
        name=raw_input('Enter pv name: ')
        os.system("pvdisplay {}".format(name))
        print("PV LIST")
    elif t==6:
        name=raw_input("Enter name of volume group: ")
        os.system('vgdisplay {}'.format(name))
        print("VG LIST")
    elif t==7:
        lvname=raw_input("Enter name of logical volume group: ")
        os.system("lvdisplay {}".format(lvname))
        print("LV LIST")
    elif t==8:
        lvname=raw_input("Enter the logical volume name: ")
        filesysname=raw_input("Enter the file system name: ")
        os.system("mkfs -t {} {}".format(filesysname,lvname))
    elif t==9:
         lvname=raw_input("Enter the logical volume name: ")
         os.system("blkid {}".format(lvname))
    elif t==10:
        size=int(raw_input('Enter size to extennd: '))
        lvm=raw_input('Enter your lvm path: ')
        os.system('lvextend --size +{}G {}'.format(size,lvm))
        os.system('resize2fs {}'.format(lvm))
    elif t==11:
        size=int(raw_input('Enter size to reduce: '))
        lvm = raw_input('Enter  path of your lvm: ')
        lvsize=int(raw_input('Enter size to resize: '))
        folder = raw_input('Enter path where your lvm attached: ')
        dirpath = raw_input('Enter your directory path')
        os.system('umount {}'.format(lvm))
        os.system('e2fsck -f {}'.format(lvm))
        os.system('resize2fs {} {}'.format(lvm,lvsize))
        os.system('lvreduce --size -{}G {} -y'.format(size,lvm))
        os.system('mount {} {}'.format(lvm,dirpath))
    elif t==12:
        dirpath = raw_input('Enter your directory path: ')
        isExists=os.path.exists(dirpath)
        lvm = raw_input('Enter lvm name/path: ')
        os.system('mount {} {}'.format(lvm,dirpath))
        print('mounted successfully..')
    elif t==13:
        lvm = raw_input('Enter directory name/path: ')
        os.system('umount {}'.format(lvm))
        print('umount successfully...')
    else:
        print('Enter valid option...from above')


