# denchu_File_Searcher
 デンチュウさんのプログラムで変更されたところを見る（多分最初にあるPATHを変えればなんでも比較できるかも)

## 注意
著作権とかの都合上でんちゅー本体やRedmeは消しましたのでresult.txtと標準出力が異なる可能性があります。

## コードの評価について
見てわかる通り違うスコープで同じ名前の変数を使っていたりします。くそコードです。リストはさすがに分けてたかも。
動いたからいいやってくらいのクオリティです。

## 動機
デンちゅーのプログラミングの授業で毎回ファイルをダウンロードするのでなぜかと思った。ポストを毎回変えて課題を一定の期間でしか受け取らないようにするのかなと思ってた。

## 結果(雑に書いたから多分バグがなければ)
configのステージの部分しかほとんど変わらない！<br>
こういう拡張性があるプログラム好き<br>
configを変えたらどうゆう処理になるか解析できたら強そう。<br>


## 実行方法
一応サンプルとしてデンチューっぽいデータを入れているけど、実際に自分の作業ディレクトリに入れて相対パスを入力するといいかも

これを実行する
```
denchu_diff.py
```


ファイルに出力するのもあり
```
denchu_diff.py > result.txt
```
