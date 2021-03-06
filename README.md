# project_tanaka

## ゼミ内容
4/30説明内容  
機械学習 ⊃ ディープラーニング  

![kikaigakushuu](https://user-images.githubusercontent.com/48379176/117101642-a4c32080-adb1-11eb-9e95-333daa8a28d9.jpg)

上記隠し層が,複雑化かつ多層化されたものを一般的にディープラーニングと呼ぶ.  
上記の隠し層には様々な処理を行う層をいくつも組み合わせており,その中で,画像解析の分野で多く用いられるのがCNNモデルと呼ばれる層の組み合わせパターンだ. 

CNNモデル：隠し層 ⊃ 畳み込み層,プーリング層,結合層  

![tatamikomi](https://user-images.githubusercontent.com/48379176/117101687-bc9aa480-adb1-11eb-9247-83a9ab6e67a7.jpg)
![puringu](https://user-images.githubusercontent.com/48379176/117101716-ccb28400-adb1-11eb-8825-58d16eb22502.jpg)

以下がCNNモデルの基本設計図となる.

![CNN](https://user-images.githubusercontent.com/48379176/117101749-ddfb9080-adb1-11eb-8997-96abae36db7c.jpg)

ここで,結合層から出力層に送られるデータは多次元データとなっており,これがモデルがサンプルから学習した特徴をパラメータとして表したものとなる.  
この各パラメータに,重要度によって重みづけをすることにより,検証時の精度が上下する.  
その重みづけアルゴリズムにはいくつか種類があり,それらのアルゴリズムを最適化アルゴリズムとよぶ.  
このアルゴリズムを変更することにより,モデルの精度改め,損失率が変わってくる. 

損失率:学習時の重みづけパラメータ - 検証時の重みづけパラメータ  

ここで,その重みづけパラメータを出力値としてそのまま出力すると,出力値の合計が1にならず,確率としてあらわせないため,不便である.  
そこで,出力する前に,以下のsoftmax関数を与えることにより,出力の合計が1となり,確率として表現できる.  

## chainer
chainer 環境を windowsOS でうまく整えられずやむなく基礎編のみで中断
応用は windowsOS 適性の keras で続行する

## keras
### commit 1:
keras 環境構築したのち、ベースとなる写真データを Google Image Download を用いて一括ロード.
以上データベースをセットアップし、基本モデルを構築し、学習させた.
初期モデルの予測度計算値は３割前後でまだまだ粗削りといった感じ.
### commit 2:
#### モデル構成変更...
  Dense層の活性化関数softmax
  コンパイルのlossをbinary型からcategory型へ
  epochsとbatch_sizeをいじってみてscoreの高いものを選ぶ
#### 画像水増し...
  ベース画像を上下左右反転させ、4倍のデータ量に
  次は、ベースの画像量を増やしてみることにしようかな
### commit 3:
画像をダウンロードしている最中に気づくがそもそものジャンル分けが曖昧だったと気づく.
画像データ数が少なかったことも踏まえて改めて集めてくることに.
ChromeDriverを用いて、肉料理、海鮮、スイーツ、麺類の各ジャンルの画像を1000枚近く集め、４倍に水増ししたのち、以前のモデル構成でコンパイル.
scoreは6,7割とだいぶ伸びたがまだまだ微調整が必要.

![accuacy](https://user-images.githubusercontent.com/48379176/103351020-2eea3800-4ae5-11eb-877a-337b73134e0a.jpg)
![loss](https://user-images.githubusercontent.com/48379176/103351074-593bf580-4ae5-11eb-8e5a-e2d1a13e6e1c.jpg)

### commit 4:
epochsを50 batch_sizeを32で設定し、正答率と損失率のグラフをきれいに可視化してみる.
試行回数10前後でどうやら過学習を起こしているように見てとれる.次は過学習対策を施してみる.
目指すは正答率８割

![accuacy](https://user-images.githubusercontent.com/48379176/103398299-71605300-4b7f-11eb-81c8-cb79f2dbb975.jpg)
![loss](https://user-images.githubusercontent.com/48379176/103398305-77563400-4b7f-11eb-877f-504b184f60cf.jpg)

### commit 5:
試行錯誤の末、なんとか正答率8割越えのモデルを作成した.
モデルを複雑にしたり、画像サイズをより大きくしたりと色々試みたものの、計算処理容量が限界なのか精度が逆におちたりした.一応テストモデルとして、このモデルを採用していくことにするが、今後できれば精度を上げたい.

![accuracy](https://user-images.githubusercontent.com/48379176/104145468-738da180-540a-11eb-8b02-2ab68e32f42a.jpg)
![loss](https://user-images.githubusercontent.com/48379176/104145616-10503f00-540b-11eb-9960-3e6e435fd29c.jpg)

### commit 6:
前回のコミットから少し機械学習のモデル精度上げから離れ、せっかくなのでwebappとして形に残そうと思い、webアプリケーションに手を出した。  
使うのはpythonとdjangoで、主な機能は以下の通り。  
写真をapp上にアップロード→写真からジャンルを自動で検出→写真と情報を連結させながらDBに保存→保存したデータをもとにマップ上に表示する  
一言で表すと、お気に入りのグルメマップ、といった感じだ。  
今は基礎のモデル構成が完成し、あとは画像のデータとリンクさせ、今まで制作してきた機械学習のプロジェクトと組み合わせれば形になる。  

### commit 7:
写真とDBの情報をリンクさせて、保存することができたので、必要最低限の機能を持った webapp が完成した.  
以下プレビュー.  
![sta1](https://user-images.githubusercontent.com/48379176/105624664-ed8c4480-5e66-11eb-972c-a31d6bbd32af.jpg)  
![sta2](https://user-images.githubusercontent.com/48379176/105624684-04cb3200-5e67-11eb-974d-2106dfda4379.jpg)  
![sta3](https://user-images.githubusercontent.com/48379176/105624688-11e82100-5e67-11eb-8f25-24afd055ff09.jpg)  
![sta4](https://user-images.githubusercontent.com/48379176/105624695-190f2f00-5e67-11eb-938d-d55a0f11f9d1.jpg)  
![sta5](https://user-images.githubusercontent.com/48379176/105624712-33e1a380-5e67-11eb-962a-35bba0ef88a6.jpg)  
![sta6](https://user-images.githubusercontent.com/48379176/105624747-6db2aa00-5e67-11eb-8ba1-cbdcf46416dd.jpg)
