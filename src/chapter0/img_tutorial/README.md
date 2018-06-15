# img_tutorial

## Install  
```bash
$ cd  
$ git clone  https://github.com/Choi-Laboratory/ros_tutorial.git  
$ cp -r ~/ros_tutorial/src/chapter0/img_tutorial ~/catkin_ws/src/  
$ cd ~/catkin_ws/src/img_tutorial  
$ chmod 755 *.sh  
$ ./install.sh  
$ ./opencv_3_4_install.sh  
```

## Lesson
ROSでUSBカメラを使う方法は以下のサイトを参考にしてください。  
[Raspberry Pi + ROSでUSB Cameraを使う](http://karaage.hatenadiary.jp/entry/2015/10/29/073000)  
　　　  

- ①　Imageトピックを表示するプログラムを書いてみよう。[解答例](https://github.com/Choi-Laboratory/ros_tutorial/blob/master/src/chapter0/img_tutorial/scripts/img_show.py)  
- ②　顔を検出するプログラムを書いてみよう。[解答例](https://github.com/Choi-Laboratory/ros_tutorial/blob/master/src/chapter0/img_tutorial/scripts/face.py)  
- ③　目を検出するプログラムを書いてみよう。[解答例](https://github.com/Choi-Laboratory/ros_tutorial/blob/master/src/chapter0/img_tutorial/scripts/eye.py)  
