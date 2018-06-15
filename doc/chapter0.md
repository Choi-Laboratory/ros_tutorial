# ROSとOpenCVを使った顔認識  

 ROSにはImage型のトピックが用意されており、ROSで画像処理をすることが可能です。  
USBカメラから取得したImage型のトピックをsubscribeし、OpenCVを用いた画像処理を行います。  
cascadeファイルを用いて、USBカメラで取得した映像から人の顔の認識ができるようになるのが目標です。  
