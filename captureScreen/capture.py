#coding=utf-8
import pyhk
import wx
import os
import sys
from PIL import ImageGrab

def capture_fullscreen():
    #�����ӿù�,�Ϊk�i�Ѧ�   http://pillow.readthedocs.org/en/3.1.x/reference/ImageGrab.html
    pic = ImageGrab.grab()    
    #�O�s�Ϥ�
    save_pic(pic)
    
def save_pic(pic, filename = '���R�W�Ϥ�'):    
    # wx  �Ϊk�i�Ѧ� http://www.wxpython.org/docs/api/wx.PySimpleApp-class.html
    app = wx.PySimpleApp()    
    wildcard = "pictures (*.png,*.jpeg,*.bmp)|*.png;*.jpeg;*.bmp"      
    #FileDialog�Ϊk	__init__(self, parent, message, defaultDir, defaultFile, wildcard, style, pos) 
    dialog = wx.FileDialog(None, "�п���x�s���|", os.getcwd(),
                           filename, wildcard, wx.FD_SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        format = dialog.GetPath().split(".")[-1]
        pic.save(dialog.GetPath().encode(sys.getfilesystemencoding()),format)
    else:
        pass    
    dialog.Destroy()    
    
def main():
    # pyhk �ϥΪk��i�Ѧ�   https://github.com/schurpf/pyhk
    hot = pyhk.pyhk()
    #���U�ֱ��� CTRL+F1
    hot.addHotkey(['Ctrl', 'F1'], capture_fullscreen)  
    hot.start()
    
if __name__ == "__main__":
    main() 