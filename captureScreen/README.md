# captureScreen
使用快捷鍵對電腦螢幕進行截圖
* [Demo Video等待新增]() - Windows 

### 如何安裝 Pillow
```
pip install Pillow
```
可參考 [ Pillow官方文件 ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

### 如何安裝 PYHK
先到  [PYHK](https://github.com/schurpf/pyhk)  下載(Download ZIP) <br>
或是 <br>
使用 cmd 輸入
```
git clone  https://github.com/schurpf/pyhk.git
```
使用方法
```
import pyhk.py
```
詳細使用方法可參考 [pyhk-end-user-documentation](http://schurpf.com/python/python-hotkey-module/pyhk-end-user-documentation/)

### 如何安裝 pyHook
先到  [pyHook](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook)  下載對應的版本 <br>
電腦為32bit，請下載  pyHook-1.5.1-cp27-none-win32.whl<br>
電腦為64bit，請下載  pyHook-1.5.1-cp27-none-win_amd64.whl<br>
安裝方法，在 cmd 輸入(在這裡用64bit做範例)
```
pip install pyHook-1.5.1-cp27-none-win_amd64.whl
```

### 如何安裝 wxPython
先到  [wxPython](http://www.wxpython.org/download.php)  下載對應的版本  <br>
電腦為32bit，請下載  wxPython3.0-win32-py27	32-bit Python 2.7 <br>
電腦為64bit，請下載  wxPython3.0-win64-py27	64-bit Python 2.7 <br>
載完後雙擊.EXE安裝

## 特色
* 透過 Pillow ，使用快捷鍵對電腦螢幕進行截圖

## 使用方法
```
pyhton capture.py
```
執行後，按鍵盤上的 'Ctrl' + 'F1' 就會對電腦螢幕進行截圖，<br>
並詢問你要儲存的路徑以及圖片格式

## 執行畫面
![alt tag]()
執行後程式會一直在背景執行<br>
如需強制終止，請按鍵盤上的 'Ctrl' + 'C'

## 輸出格式
圖片檔
![alt tag]()

## External 
* [PYHK](https://github.com/schurpf/pyhk) 
* [pyHook](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook)
* [wxPython](http://www.wxpython.org/download.php) 

## Environment
* Python 2.7.3
* Pillow 3.1.1
* Windows 8.1

## License
MIT license
