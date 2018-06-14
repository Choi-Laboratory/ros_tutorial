＜ROSの分散処理(master編)＞

●準備
①Wi-Fiに接続する。
②自分のIPアドレスを確認する。
端末を開いて、
hostname -I
→192.168.11.## と出る。

●手順
①通信相手と接続出来ているか確認(**の部分は相手に教えてもらう)
ping 192.168.11.**

②端末の環境設定ファイルを開く。
sudo gedit ~/.bashrc

③masterとして自分のIPアドレスを登録
export ROS_MASTER_URI=http://192.168.11.##:11311

④自分のIPアドレスを登録
export ROS_HOSTNAME=192.168.11.##

⑤.bashrcファイルを閉じる

⑥端末をすべて閉じる

⑦端末を2つ立ち上げ、
1つ目はroscore
2つ目はrosrun remote_sub listener.py



※分散処理を行わない時は.bashrcファイルのexport ~をコメントアウトしておいてください。
