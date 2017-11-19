import urllib
from bs4 import BeautifulSoup
import time

"""
料理データを収集するプログラムです

- 料理名
- 材料名

をリストにして格納


* 注意事項
- ページがない場合は飛ばす
"""

"""データ収集部"""
num = 1000000

while num < 1000100:

	time.sleep(1)
	
	user_knowledge_list = []
	
	
	try:
		# HTML を取得
		html = urllib.request.urlopen("http://cookpad.com/recipe/"+str(num)).read()

		# 解析用の BeautifulSoup オブジェクトを作成
		soup = BeautifulSoup(html, "lxml")
		
		# レシピのメイン部を取得
		recipe_main = soup.find("div", attrs={"id": "recipe-main"})

		# レシピのタイトルを取得
		recipe_title = recipe_main.find("h1", attrs={"class": "recipe-title fn clearfix"})
		user_knowledge_list.append(recipe_title.string)

		# 材料を取得
		for ingredient in recipe_main.findAll("div", attrs={"class": "ingredient_name"}):
			if ingredient.string == None:
				ingredient_a = ingredient.find("a", attrs={"class": "cookdict_ingredient_link"})
				user_knowledge_list.append(ingredient_a.string)
		
			else:
				user_knowledge_list.append(ingredient.string)
			
			
		print(user_knowledge_list)
		num += 1

	#ページが見つからないとき	
	except:
		num += 1
		
		
		
"""データ格納部"""
#以下にデータ格納処理

