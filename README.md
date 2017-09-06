# atsumori-slack-bot
巷で流行っている熱盛をSLACK内で表示させるSLACK BOTです。<br>
誰かの会話に10%の確率で熱盛のリアクションをして「失礼しました。」とBotが謝ります。

## 環境
Python (version 3.X)<br>
### Python モジュール
slackbot (version 0.4.1)<br>
slacker (version 0.9.42)<br>

## 使い方
1. SLACK Botを作成<br>
私はこちらを参考にしました。<br>
[PythonのslackbotライブラリでSlackボットを作る](http://qiita.com/sukesuke/items/1ac92251def87357fdf6)<br>
Botの名前と画像はTさんに設定するとよりリアルになります。<br>
Botを作成した時には表示されるAPI_TOKENは4で使うのでメモしておいてください。

2. 熱盛の絵文字を登録<br>
SLACKの絵文字として熱盛の画像を登録しましょう。<br>
絵文字の名前はatsumoriとしてください。
熱盛ジェネレーターを作っている有志の方もいます。<br>
[熱盛ジェネレーター](https://totoraj930.github.io/atumori/)<br>
*Tさんや熱盛の画像は自己責任でお願いします。

3. API_TOKENを設定<br>
slackbot_settings.pyをエディタなどで開きます。<br>
`API_TOKEN = 'xxxxxxxxxxxxxxxxx'`<br>
となっている箇所を1でメモしたAPI_TOKENで書き換えます。<br>
例えば、メモしたAPI_TOKENがatsumoriiiiiiiiiiでしたら<br>
`API_TOKEN = 'atsumoriiiiiiiiii'`<br>
と記入します。シングルクォーテーションも必ず書いてください。<br>

4. Botを起動<br>
ターミナルなどからrun.pyをPythonで実行します。<br>
`python run.py`<br>
正常に起動できていたらSLACKからみた時Botがアクティブになっていると思います。<br>

5. Botをどこかのチャンネルに招待<br>
Botを例えば#randomなどのチャンネルに追加してください。<br>
追加したチャンネルで、誰かの会話に10%の確率で熱盛のリアクションをして「失礼しました。」とBotが謝ります。<br>

## おまけ
設定を変えたい時はplugins/parameters.pyをエディタなどで開きます。<br>
各行は以下の設定を表しています。お好みにカスタマイズしてください。
```
EMOJI_NAME: リアクションさせる絵文字の名前
ATSUMORI_PROBABILITY: 熱盛する確率
NORMAL_PROBABILITY: 熱盛してさらにそれがノーマル熱盛の確率
```
例：<br>
ATSUMORI_PROBABILITY = 0.5<br>
NORMAL_PROBABILITY = 0.9<br>
だった場合、<br>
50% × 90% = 45%の確率で「失礼しました。熱盛と出てしまいました。」<br>
50% × 10% = 5%の確率で「あっ…熱盛が出てしまい…ました失礼しました。」<br>
と表示されます。<br>
<br>
##### ご紹介させていただいたQiitaやGithubのURLは不都合がありましたら削除いたしますので御連絡ください。
