# resizePicture
重新對圖片設定大小、旋轉

# 如何安裝 Pillow
```
pip install Pillow
```
可參考 [ Pillow官方文件 ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

## 特色
* 透過 Pillow , 重新對圖片設定大小、旋轉

## 使用方法
```
pyhton resize.py [模式] [大小or角度] 
```

## 執行範例 
###範例一  圖片大小比率縮放
``` 
python resize.py size 200
```
說明:<br>
該範例為將圖片大小放大為200%<br>
如修改為50，即對圖片縮小50%<br>
###範例二 指定圖片大小
``` 
python resize.py size 640 360
```
說明:<br>
該範例為將圖片大重新設定為<br>
640*360 [width]*[height] 大小<br>
可自行修改  [width]*[height] 的數值
###範例三 旋轉圖片
``` 
python resize.py rotate 90
```
說明:<br>
該範例為將圖片逆時針旋轉90度<br>
如需順時針旋轉圖片，可將角度修改為-90<br>

## 執行畫面
###範例一
![alt tag]()
###範例二
![alt tag]()
###範例三
![alt tag]()


## 輸出格式
圖片檔
![alt tag]()

## Environment
* Python 2.7.3
* Pillow 3.1.1
* Windows 8.1

## License
MIT license
