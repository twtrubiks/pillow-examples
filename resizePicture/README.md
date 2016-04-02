# resizePicture
透過 Pillow , 將路徑底下全部的圖片檔，重新設定大小、旋轉
* [Demo Video](https://youtu.be/7MbGPZjNwmE) - Windows 

### 如何安裝 Pillow
```
pip install Pillow
```
可參考 [ Pillow官方文件 ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

## 特色
* 透過 Pillow , 將路徑底下全部的圖片檔，重新設定大小、旋轉

## 使用方法
```
python resize.py [模式] [大小or角度] 
```

## 執行範例 
###範例一  圖片大小比率縮放
``` 
python resize.py size 50
```
說明:<br>
該範例為將路徑底下全部的圖片大小縮小為50%<br>
如修改為150，即對圖片放大150%<br>
###範例二 指定圖片大小
``` 
python resize.py size 640 360
```
說明:<br>
該範例為將路徑底下全部的圖片大重新設定為<br>
640 * 360 <br>
[width] * [height] 大小<br>
可自行修改  [width] * [height] 的數值
###範例三 旋轉圖片
``` 
python resize.py rotate 90
```
說明:<br>
該範例為將路徑底下全部的圖片逆時針旋轉90度<br>
如需順時針旋轉圖片，可將角度修改為-90<br>

## 執行畫面
###範例一
執行後路徑底下會多一個名稱為 resized_images 的資料夾<br>
資料夾裡會有 p1.jpg 和 p2.png 的縮小50%的圖片
![alt tag](http://i.imgur.com/aJ3a76S.jpg)
###範例二
執行後路徑底下會多一個名稱為 resized_images 的資料夾<br>
資料夾裡會有 p1.jpg 和 p2.png 的 640 * 360 大小的圖片
![alt tag](http://i.imgur.com/zHhi3Gx.jpg)
###範例三
執行後路徑底下會多一個名稱為 resized_images 的資料夾<br>
資料夾裡會有 p1.jpg 和 p2.png 的 逆時針旋轉90度的圖片<br>
![alt tag](http://i.imgur.com/Xr4kqfx.jpg)

## Environment
* Python 2.7.3
* Pillow 3.1.1
* Windows 8.1

## License
MIT license
