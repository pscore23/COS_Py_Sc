import scratchconnect # 諸々インポート
import time
import datetime
import sys

session = scratchconnect.ScratchConnect('_____', '_____') # サインイン
status = session.status() # ユーザーのステータスを取得
if status == 'New Scratcher': # New Scratcher なら強制終了
    sys.exit()
wait = lambda second: time.sleep(second) # PEP8 は無視していくスタイル
setwork = lambda text: session.set_work(content=text)

while True: # メインループ
    while True: # do while 文の再現
        session.update_data() # 情報を更新
        msg = session.messages_count() # 未読メッセージ数を取得
        if (msg > 0):
            break
        wait(1)
    while True: # かなり無理矢理なコードですがお許しを
        session.update_data()
        msg = session.messages_count()
        if (msg == 0):
            break
        wait(1)
    dt = datetime.datetime.now() # 現在日時を取得
    dt = str(dt.replace(microsecond = 0)) # ミリ秒以下を切り捨て
    setwork(f'生存確認 ({dt})\r\nこの表示は [COS_Py_Sc.py] によって自動更新されています。\r\nインスピレーションをくれた @yukku さんと\r\nこのシステムの開発者の @Rubik_13 さんに感謝!')
    wait(3)
