import pyvda
import sys



def switch_to_desktop(desktop_number):
    desktops = pyvda.get_virtual_desktops()

    if desktop_number>len(desktops):
        while desktop_number>len(desktops):
            pyvda.VirtualDesktop.create()
            desktops = pyvda.get_virtual_desktops()

    pyvda.VirtualDesktop(desktop_number).go()

switch_to_desktop(int(sys.argv[1]))

print(len(pyvda.get_virtual_desktops()))
