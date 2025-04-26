from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/angou', methods=['GET', 'POST'])
def angou():
    if request.method == 'POST':
        text = request.form.get("tinko")
        key = request.form.get("manko")
        if len(key) == 0:
            return render_template("input_angou.html")
        mapping = [
        "あ", "い", "う", "え", "お",
        "か", "き", "く", "け", "こ",
        "さ", "し", "す", "せ", "そ",
        "た", "ち", "つ", "て", "と",
        "な", "に", "ぬ", "ね", "の",
        "は", "ひ", "ふ", "へ", "ほ",
        "ま", "み", "む", "め", "も",
        "や", "ゆ", "よ",
        "ら", "り", "る", "れ", "ろ",
        "わ", "を", "ん",
        "が", "ぎ", "ぐ", "げ", "ご",
        "ざ", "じ", "ず", "ぜ", "ぞ",
        "だ", "ぢ", "づ", "で", "ど",
        "ば", "び", "ぶ", "べ", "ぼ",
        "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
        "ぁ", "ぃ", "ぅ", "ぇ", "ぉ",
        "ゃ", "ゅ", "ょ", "っ"]

        kansei = ""
        for i in text:
            soeji = 0
            for r in mapping:
                if i == r:
                    kansei = kansei + str(soeji + int(key))
                    break
                else:
                    soeji += 1
        kansei = kansei + key
        return render_template("output_angou.html",kansei=kansei)

    else:
        return render_template("input_angou.html")


@app.route('/hukugou', methods=['GET', 'POST'])
def hukugou():
    if request.method == 'POST':
        text = request.form.get("tinge")
        mapping = [
        "あ", "い", "う", "え", "お",
        "か", "き", "く", "け", "こ",
        "さ", "し", "す", "せ", "そ",
        "た", "ち", "つ", "て", "と",
        "な", "に", "ぬ", "ね", "の",
        "は", "ひ", "ふ", "へ", "ほ",
        "ま", "み", "む", "め", "も",
        "や", "ゆ", "よ",
        "ら", "り", "る", "れ", "ろ",
        "わ", "を", "ん",
        "が", "ぎ", "ぐ", "げ", "ご",
        "ざ", "じ", "ず", "ぜ", "ぞ",
        "だ", "ぢ", "づ", "で", "ど",
        "ば", "び", "ぶ", "べ", "ぼ",
        "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
        "ぁ", "ぃ", "ぅ", "ぇ", "ぉ",
        "ゃ", "ゅ", "ょ", "っ"]

        kugiri = ""
        moji = ""
        youso = len(text)
        if youso == 0:
            return render_template("input_hukugou.html")

        key = text[youso-3] + text[youso-2] + text[youso-1]
        text = text[:-3]
        for i in text:
            kugiri = kugiri + i
            if len(kugiri) != 3:
                continue
            soeji = int(kugiri) - int(key)
            moji = moji + mapping[soeji]
            kugiri = ""
        return render_template("output_hukugou.html",moji=moji)

    else:
        return render_template("input_hukugou.html")




if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)  
