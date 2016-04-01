# watermark
透過 Pillow , 將路徑底下全部的圖片檔加上浮水印
* [Demo Video等待新增]() - Windows 

### 如何安裝 Pillow
```
pip install Pillow
```
可參考 [ Pillow官方文件 ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

## 特色
* 透過 Pillow ，將路徑底下全部的圖片檔加上浮水印

## 使用方法
```
python example.py [文字] [字型] [字型大小] [位置] [旋轉] [透明度] 
```

## 執行範例
```
python example.py 簽名 超世紀粗行書.TTF 50  CT 0 0.8 
```
說明:<br>
該範例為將路徑底下全部的圖片加上浮水印，<br>
浮水印的內容為"簽名"、字型為"超世紀粗行書.TTF"，字型大小為"50"，<br>
浮水印位置為"CT"(中間 center)，旋轉角度為"0"，透明度為"0.8"(數值越小越透明)<br>

浮水印位置說明:<br>
左上 upper left (UL) <br>
左中 center left (CL)<br>   
左下 lower left (LL)<br>
中上 center upper (CU) <br>
中間 center (CT)<br>
中下 center lower (CL)  <br>
右上 upper right (UR) <br>
右中 center right (CR)<br>
右下 lower right (LR)<br>

字型的部分:<br>
可自行上網下載，<br>
或是到本機的路徑 C:\Windows\Fonts 下取得字型

## 執行畫面
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
