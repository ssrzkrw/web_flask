# HAISETU方式WEBページ作成の構想
## 使用技術
### Flask
WEBページとPythonとのやり取りをすることができる技術  
[(紹介動画リンク)](https://www.youtube.com/watch?v=bzbrpkbjWe8&t=1130s)　[(参考実装)](https://www.youtube.com/watch?v=bzbrpkbjWe8&t=1130s)　[(公式)](https://flask.palletsprojects.com/en/stable/)  

## 作成流れ
①　A.htmlで暗号化、復号化を選択するボタンを用意  
②　暗号化であればB.htmlへ、復号化であればC.htmlへ遷移  
③　B.htmlに遷移した場合、暗号化したい文字列と暗号キーを受け取る用にテキストボックスを2つと実行ボタンを用意
④　Python側にテキストボックス内の値が送られ、暗号化を行う  
⑤　暗号化の結果をD.htmlに送り、値を表示する  

![永野芽郁](https://www.sponichi.co.jp/entertainment/news/2023/08/22/jpeg/20230822s00041000556000p_view.webp)