# watermark
透過 Pillow , 將路徑底下全部的圖片檔加上浮水印
* [Demo Video](https://www.youtube.com/watch?v=pGatyVSFCvE) - Windows 

### 如何安裝 Pillow
```
pip install Pillow
```
可參考 [ Pillow官方文件 ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

## 特色
* 透過 Pillow ，將路徑底下全部的圖片檔加上浮水印

## 使用方法
```
python watermark.py [文字] [字型] [字型大小] [位置] [旋轉角度] [透明度] 
```

## 執行範例
```
python watermark.py 簽名 超世紀粗行書.TTF 50  CT 0 0.8 
```
說明:<br>
該範例為將路徑底下全部的圖片加上浮水印，<br>
浮水印的內容為<b> 簽名 </b>、字型為<b> 超世紀粗行書.TTF </b>，字型大小為<b> 50 </b>，<br>
浮水印位置為<b> CT </b>(中間 center)，旋轉角度為<b> 0 </b>度，透明度為<b> 0.8 </b>(數值越小越透明)<br>

浮水印位置說明:<br>
```
左上 upper left   (UL) 
左中 center left  (CL)
左下 lower left   (LL)
中上 center upper (CU)
中間 center       (CT)
中下 center lower (CL)
右上 upper right  (UR)
右中 center right (CR)
右下 lower right  (LR)
```
字型的部分:<br>
可自行上網下載，<br>
或是到本機的路徑 C:\Windows\Fonts 下取得字型

## 執行畫面
![alt tag](http://i.imgur.com/KgG0nuj.jpg)<br>
路徑底下的圖片會被加上浮水印，並放在 watermark_images 資料夾裡<br>
![alt tag](http://i.imgur.com/Ge91eem.jpg)
![alt tag](http://i.imgur.com/ltQnP1q.jpg)<br>
也可自行修改<br>
![alt tag](http://i.imgur.com/JUxl4xP.jpg)
![alt tag](http://i.imgur.com/tBIrWcv.jpg)


## Environment
* Python 2.7.3
* Pillow 3.1.1
* Windows 8.1

## License
MIT license
