# ROSにおける分散処理講座

## 分散処理とは

分散処理とは複数のコンピュータを用いてノード通信を行う処理のことです。
これを用いることによって、コンピュータの処理性能に合わせてノードを適切に割り振ることで効率的な処理が可能となります。
プログラムを並列に処理するには一般では手間と技術が必要とされていますが、ROSを用いることで簡単に行うことができます。

通信を行うためにはまず通信先がどこにいるのか確認しなければなりません。
それを確認する場所となるのが「Master」と呼ばれるサーバです。Masterには通信に各ノードの情報が登録されています。MasterはROSでは「roscore」コマンドで起動します。

今回はtalkerとlistenerのトピック通信を2台のPCで行います。

1台はMasterとlistener、もう1台はtalkerを立ててコンピュータ間の通信を行います。


