#coding=utf-8
import pyhk
import wx
import os
import sys
from PIL import ImageGrab

def capture_fullscreen():
    #抓取整個螢幕,用法可參考   http://pillow.readthedocs.org/en/3.1.x/reference/ImageGrab.html
    pic = ImageGrab.grab()    
    #保存圖片
    save_pic(pic)
    
def save_pic(pic, filename = '未命名圖片'):    
    # wx  用法可參考 http://www.wxpython.org/docs/api/wx.PySimpleApp-class.html
    app = wx.PySimpleApp()    
    wildcard = "pictures (*.png,*.jpeg,*.bmp)|*.png;*.jpeg;*.bmp"      
    #FileDialog用法	__init__(self, parent, message, defaultDir, defaultFile, wildcard, style, pos) 
    dialog = wx.FileDialog(None, "請選擇儲存路徑", os.getcwd(),
                           filename, wildcard, wx.FD_SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        format = dialog.GetPath().split(".")[-1]
        pic.save(dialog.GetPath().encode(sys.getfilesystemencoding()),format)
    else:
        pass    
    dialog.Destroy()    
    
def main():
    # pyhk 使用法方可參考   https://github.com/schurpf/pyhk
    hot = pyhk.pyhk()
    #註冊快捷鍵 CTRL+F1
    hot.addHotkey(['Ctrl', 'F1'], capture_fullscreen)  
    hot.start()
    
if __name__ == "__main__":
    main() 