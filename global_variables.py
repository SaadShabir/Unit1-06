# Created by: Saad Shabir
# Created on: Sep 2017
# Created for: ICS3U
# This program shows the difference between local and global variables

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_answer_label'].text = str(variableZ)
        
def global_button_touch_up_inside(sender):
    
    
    #global variableX
    #variableX = variableX + 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_answer_label'].text = str(variableZ)

view = ui.load_view()
view.present('full_screen')
