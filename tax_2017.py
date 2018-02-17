
# coding: utf-8

# # settings

# In[ ]:


import os
import re
import pandas as pd


# In[ ]:


# pandas の最大表示列数を設定 (max_rows で表示行数の設定も可能)
pd.set_option('display.max_columns', 30)


# In[ ]:


os.getcwd()


# In[ ]:


# 請求書の場所を指定
bill_dir = r"D:\documents\tax\h29\Bill_2017"


# In[ ]:


def getEncode(filepath):
    '''
    テキストファイルの文字コードを確認する関数
    デコードエラーが出なくなるまで順番に試す
    試す順番で結果が変わる可能性がある
    getEncode(r'filepath')
    '''
    encs = "iso-2022-jp euc-jp sjis utf-8".split()
    for enc in encs:
        with open(filepath, encoding=enc) as fr:
            try:
                fr = fr.read()
            except UnicodeDecodeError:
                continue
        return enc


# In[ ]:


getEncode(r"D:\documents\tax\h29\Bill_2017\jcb\201802meisai.csv")


# # JCB

# In[ ]:


card = 'jcb'


# In[ ]:


bills = os.listdir('{0}\{1}'.format(bill_dir, card))
bills


# In[ ]:


jcb = pd.DataFrame()
for x in bills:
    jcb = jcb.append(pd.read_csv('{0}\{1}\{2}'.format(bill_dir, card, x)
                     , skiprows=5, encoding='Shift-JIS'))
display(jcb)


# In[ ]:


jcb.columns


# In[ ]:


jcb.groupby('カテゴリ').count()


# In[ ]:


jcb.groupby('支払区分').count()


# In[ ]:


jcb.groupby('摘要').count()


# In[ ]:


jcb['コード'] = ""
jcb['カード'] = 'JCB'


# In[ ]:


jcb = jcb[jcb['ご利用日'].str.contains('2017')]
display(jcb)


# In[ ]:


jcb = jcb[['ご利用日', 'コード', 'ご利用金額(￥)', 'ご利用先など', 'カード']]
display(jcb)


# In[ ]:


jcb.columns = ['日付', 'コード', '金額', '備考', 'カード']
display(jcb)


# In[ ]:


jcb = jcb.sort_values(['備考', '日付']).reset_index(drop=True)
display(jcb)


# In[ ]:


jcb['日付'] = jcb['日付'].str.replace(' ', "")
display(jcb)


# In[ ]:


jcb.to_csv('{0}\{1}.csv'.format(bill_dir, card), index=False, encoding=('Shift-JIS'))


# # rakuten

# In[ ]:


card = 'rakuten'


# In[ ]:


bills = os.listdir('{0}\{1}'.format(bill_dir, card))
bills


# In[ ]:


rakuten = pd.DataFrame()
for x in bills:
    rakuten = rakuten.append(pd.read_csv('{0}\{1}\{2}'.format(bill_dir, card, x)
                             , encoding='Shift-JIS'))
display(rakuten)


# In[ ]:


rakuten.columns


# In[ ]:


rakuten.groupby('利用者').count()


# In[ ]:


rakuten.groupby('支払方法').count()


# In[ ]:


rakuten['コード'] = ""
rakuten['カード'] = '楽天'


# In[ ]:


rakuten = rakuten[~rakuten['利用日'].isnull()]
display(rakuten)


# In[ ]:


rakuten = rakuten[rakuten['利用日'].str.contains('17.')]
display(rakuten)


# In[ ]:


rakuten = rakuten[['利用日', 'コード', '利用金額', '利用店名・商品名', 'カード']]
display(rakuten)


# In[ ]:


rakuten.columns = ['日付', 'コード', '金額', '備考', 'カード']
display(rakuten)


# In[ ]:


rakuten = rakuten.sort_values(['備考', '日付']).reset_index(drop=True)
display(rakuten)


# In[ ]:


rakuten['日付'] = rakuten['日付'].str.replace('.', '/')
display(rakuten)


# In[ ]:


rakuten['日付'] = rakuten['日付'].str.replace('17/', '2017/')
display(rakuten)


# In[ ]:


rakuten.to_csv('{0}\{1}.csv'.format(bill_dir, card), index=False, encoding=('Shift-JIS'))


# # view

# In[ ]:


card = 'view'


# In[ ]:


bills = os.listdir('{0}\{1}'.format(bill_dir, card))
bills


# In[ ]:


view = pd.DataFrame()
for x in bills:
    view = view.append(pd.read_csv('{0}\{1}\{2}'.format(bill_dir, card, x)
                       , skiprows=5, encoding='Shift-JIS'))
display(view)


# In[ ]:


view.columns


# In[ ]:


view.groupby('ご利用箇所').count()


# In[ ]:


view.groupby('払戻額').count()


# In[ ]:


view.groupby('支払区分（回数）').count()


# In[ ]:


view['コード'] = ""
view['カード'] = 'view'


# In[ ]:


view = view[~view['ご利用箇所'].isnull()]
display(view)


# In[ ]:


view = view[view['ご利用年月日'].str.contains('2017/')]
display(view)


# In[ ]:


view = view[['ご利用年月日', 'コード', 'ご利用額', 'ご利用箇所', 'カード']]
display(view)


# In[ ]:


view.columns = ['日付', 'コード', '金額', '備考', 'カード']
display(view)


# In[ ]:


view = view.sort_values(['日付']).reset_index(drop=True)
display(view)


# In[ ]:


view.to_csv('{0}\{1}.csv'.format(bill_dir, card), index=False, encoding=('Shift-JIS'))


# # nicos

# In[ ]:


card = 'nicos'


# In[ ]:


bills = os.listdir('{0}\{1}'.format(bill_dir, card))
bills


# In[ ]:


nicos = pd.DataFrame()
for x in bills:
    nicos = nicos.append(pd.read_csv('{0}\{1}\{2}'.format(bill_dir, card, x)
                         , encoding='Shift-JIS'))
display(nicos)


# In[ ]:


nicos.columns


# In[ ]:


nicos.groupby('支払回数').count()


# In[ ]:


nicos['コード'] = ""
nicos['カード'] = 'nicos'


# In[ ]:


nicos = nicos[~nicos['ご利用日'].isnull()]
display(nicos)


# In[ ]:


nicos = nicos[nicos['ご利用日'].str.match(r'\d+-\d+-\d+')]
display(nicos)


# In[ ]:


nicos = nicos[nicos['ご利用日'].str.contains('2017-')]
display(nicos)


# In[ ]:


nicos = nicos[['ご利用日', 'コード', 'ご利用金額（円）', 'ご利用先／商品内容など', 'カード']]
display(nicos)


# In[ ]:


nicos.columns = ['日付', 'コード', '金額', '備考', 'カード']
display(nicos)


# In[ ]:


nicos = nicos.sort_values(['備考', '日付']).reset_index(drop=True)
display(nicos)


# In[ ]:


nicos['日付'] = nicos['日付'].str.replace('-', '/')
display(nicos)


# In[ ]:


nicos.to_csv('{0}\{1}.csv'.format(bill_dir, card), index=False, encoding=('Shift-JIS'))


# # amazon

# 未完成。購入履歴の一覧を取得したかったが、サイトの構造的になかなか難しい。

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# In[ ]:


import sys
import time


# In[ ]:


AMAZON_EMAIL = input('email=')
AMAZON_PASSWORD = input('password=')


# In[ ]:


# ChromeのWebDriverオブジェクトを作成する
driver = webdriver.Chrome()


# In[ ]:


# Amazonの注文履歴画面(ログイン画面)を開く
driver.get('https://www.amazon.co.jp/gp/css/order-history')
print('Waiting for contents to be loaded...', file=sys.stderr)
time.sleep(2)  # 2秒間待つ


# In[ ]:


# タイトルに'Amazonサインイン'が含まれていることを確認する
assert 'Amazonサインイン' in driver.title


# In[ ]:


input_element = driver.find_element_by_name('email')
input_element.send_keys(AMAZON_EMAIL)
input_element.send_keys(Keys.RETURN)
print('Waiting for contents to be loaded...', file=sys.stderr)
time.sleep(2)  # 2秒間待つ


# In[ ]:


input_element = driver.find_element_by_name('password')
input_element.send_keys(AMAZON_PASSWORD)
input_element.send_keys(Keys.RETURN)
print('Waiting for contents to be loaded...', file=sys.stderr)
time.sleep(2)  # 2秒間待つ


# In[ ]:


# タイトルに'注文履歴'が含まれていることを確認する
assert '注文履歴' in driver.title


# In[ ]:


#要素をid番号から取得する(idが001のセレクトタグ)
element = driver.find_element_by_id("orderFilter")
#指定するテキストを設定する
text = "2017年"
#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
select = Select(element)
#セレクトタグのオプションをテキストを指定して選択する
select.select_by_visible_text(text)


# In[ ]:


# ソースコードを取得する
print(driver.page_source)


# In[ ]:


element = driver.find_element_by_id("ordersContainer")
print(element.text)


# In[ ]:


order = driver.find_elements_by_class_name("order")
for detail in order:
    print(detail.text)
    print('\n- - - - -\n')


# In[ ]:


order = driver.find_elements_by_class_name("order")


# In[ ]:


info = order[5].find_element_by_css_selector(".order-info")
info.text


# In[ ]:


detail = order[5].find_element_by_css_selector(".a-grid-top")
arow = detail.find_elements_by_css_selector(".a-row")
for x in arow:
    print(x.text)
    print('tag_name: {0}'.format(x.tag_name))
    print('\n')


# In[ ]:


# ページャーをたどる。
while True:
    assert '注文履歴' in browser.parsed.title.string # 注文履歴画面が表示されていることを確認する。

    print_order_history() # 注文履歴を表示する。

    link_to_next = browser.get_link('次へ') #「次へ」というテキストを持つリンクを取得する。
    if not link_to_next:
        break #「次へ」のリンクがない場合はループを抜けて終了する。

    print('Following link to next page...', file=sys.stderr)
    browser.follow_link(link_to_next) # 次へ」というリンクをたどる。

        


# In[ ]:


def print_order_history():
    """
    現在のページのすべての注文履歴を表示する
    """
    for line_item in driver.find_elements_by_class_name("order-info"):
        order = {} # 注文の情報を格納するためのdict
        # ページ内のすべての注文履歴について反復する。ブラウザーの開発者ツールでclass属性の値を確認できる
        # 注文の情報のすべての列について反復する
        for column in line_item.find_elements_by_class_name("a-column"):
            try:
                label_element = column.find_element_by_class_name('label')
                value_element = column.find_element_by_class_name('value')
            except:
                continue
            # ラベルと値がない列は無視する。
            if label_element and value_element:
                label = label_element.text
                value = value_element.text
                order[label] = value
        print(order['注文日'], order['合計']) # 注文の情報を表示する。
        print(order)


# In[ ]:


print_order_history()


# In[ ]:


# スクリーンショットを撮る
driver.save_screenshot('search_results.png')


# In[ ]:


driver.quit()


# In[ ]:


# ページャーをたどる。
while True:
    assert '注文履歴' in browser.parsed.title.string # 注文履歴画面が表示されていることを確認する。

    print_order_history() # 注文履歴を表示する。

    link_to_next = browser.get_link('次へ') #「次へ」というテキストを持つリンクを取得する。
    if not link_to_next:
        break #「次へ」のリンクがない場合はループを抜けて終了する。

    print('Following link to next page...', file=sys.stderr)
    browser.follow_link(link_to_next) # 次へ」というリンクをたどる。

        


# In[ ]:


def print_order_history():
    """
    現在のページのすべての注文履歴を表示する
    """
    for line_item in browser.select('.order-info'):
        order = {} # 注文の情報を格納するためのdict
        # ページ内のすべての注文履歴について反復する。ブラウザーの開発者ツールでclass属性の値を確認できる
        # 注文の情報のすべての列について反復する
        for column in line_item.select('.a-column'):
            label_element = column.select_one('.label')
            value_element = column.select_one('.value')
            # ラベルと値がない列は無視する。
            if label_element and value_element:
                label = label_element.get_text().strip()
                value = value_element.get_text().strip()
                order[label] = value
        print(order['注文日'], order['合計']) # 注文の情報を表示する。
        

