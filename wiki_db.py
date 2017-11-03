import sqlite3
import os

"""
wikipediaのデータをテキストファイルとして保存する
"""


os.chdir("作業ディレクトリの指定")

#用いたデータ
dbname = "jawiki-20170801-pages-articles.db.sqlite"

conn = sqlite3.connect(dbname)

#sql文を実行するためのオブジェクト実行
c = conn.cursor()

#記事情報を表示
select_sql = 'select * from articles'
f = open("wiki_db.txt","w")
for row in c.execute(select_sql):
    f.write(str(row))
    
f.close()
conn.close()



"""
データ収集元： http://koiroha.blogspot.jp/2017/04/how-to-get-wikipedia-dump-as-plaintext.html (11/2/2017閲覧)
"""





