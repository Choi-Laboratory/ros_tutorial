＜ROSの分散処理(sub編)＞

●準備
①Wi-Fiに接続する。(F710_5G または F710_2.4G)
②自分のIPアドレスを確認する。
端末を開いて、
hostname -I
→192.168.11.** と出る。

●手順
①通信相手と接続出来ているか確認(##の部分は相手に教えてもらう)
ping 192.168.11.##

②端末の環境設定ファイルを開く。
sudo gedit ~/.bashrc

③remote_masterの人のIPアドレスを登録(##の部分はremote_masterの人に教えてもらう)
export ROS_MASTER_URI=http://192.168.11.##:11311

④自分のIPアドレスを登録
export ROS_HOSTNAME=192.168.11.**

⑤.bashrcファイルを閉じる。

⑥端末をすべて閉じる。

⑦端末を1つ立ち上げ、
rosrun remote_sub talker.py



※分散処理を行わない時は.bashrcファイルのexport ~をコメントアウトしておいてください。
