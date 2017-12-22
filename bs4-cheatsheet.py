import requests
from bs4 import BeautifulSoup


def main():
    #making_soup()

    #navigation()

    select()

def select():
    """
    css セレクタを使った検索。jqueryっぽい
    """
    soup = BeautifulSoup('''
    <html>
        <head><title>example</title></head>
        <body>
            <ul>
                <li><a href="http://example.com/" class="first">example.com</a></li>
                <li><a href="http://www.google.com/" data="123">google.com</a></li>
            </ul>
        </body>
    </html>''', 'html.parser')

    # タグ全検索してリストで返す
    li_elements = soup.select("li")
    print(li_elements)  # [<li><a class="first" href="http://example.com/">example.com</a></li>,
                        #  <li><a href="http://www.google.com/">google.com</a></li>]

    # select_oneは検索して最初に見つかった1つ目
    first_li_element = soup.select_one('li')
    print(first_li_element) # <li><a class="first" href="http://example.com/">example.com</a></li>
    # 見つからない場合はNone
    nothing_image_element = soup.select_one('img')
    print(nothing_image_element)    # None

    #属性検索
    anchors_to_google = soup.select('a[href="http://www.google.com/"]')
    print(anchors_to_google)    # [<a href="http://www.google.com/">google.com</a>]
    #data属性存在
    print(soup.select('a[data]'))  # [<a data="123" href="http://www.google.com/">google.com</a>]

    # class指定
    first_link_element = soup.select_one("a.first")
    print(first_link_element)   # <a class="first" href="http://example.com/">example.com</a>

def navigation():
    """
    soupオブジェクトからのタグナビゲーション。
    find_allで目的のタグを見つけ、そこからツリー構造をたどる
    """
    soup = BeautifulSoup('''
    <html>
        <head><title>example</title></head>
        <body>
            <ul>
                <li><a href="http://example.com/" class="first">example.com</a></li>
                <li><a href="http://www.google.com/" data="123">google.com</a></li>
            </ul>
        </body>
    </html>''', 'html.parser')

    # 子要素をたぐる
    print(soup.head)        # <head><title>example</title></head>
    # headの下のtitle
    print(soup.head.title)  # <title>example</title>

    # find_allは全検索してリストで返す
    li_elements = soup.find_all("li")
    print(li_elements)  # [<li><a class="first" href="http://example.com/">example.com</a></li>,
                        #  <li><a href="http://www.google.com/">google.com</a></li>]
    # 見つからない場合は空のリスト
    nothing_images = soup.find_all('img')
    print(nothing_images)   # []

    # findは検索して最初に見つかった1つ目
    first_li_element = soup.find('li')
    print(first_li_element) # <li><a class="first" href="http://example.com/">example.com</a></li>
    # 見つからない場合はNone
    nothing_image_element = soup.find('img')
    print(nothing_image_element)    # None

    #属性も検索条件につける
    anchors_to_google = soup.find_all("a", href="http://www.google.com/")
    print(anchors_to_google)    # [<a href="http://www.google.com/">google.com</a>]

    # classは予約後なのでアンダースコア付加
    first_link_element = soup.find("a", class_="first")
    print(first_link_element)   # <a class="first" href="http://example.com/">example.com</a>

    # 属性取得
    print(first_link_element['href'])   # http://example.com/
    # テキスト要素
    print(first_link_element.string)    # example.com

    # 親要素
    parent = first_link_element.parent
    print(parent)   # <li><a class="first" href="http://example.com/">example.com</a></li>

def making_soup():
    """
    soupオブジェクトの生成
    第1引数は、HTML文字列 or ファイルハンドル
    第2引数で、htmlをparseするためのparserライブラリを指定する
    よく使用されるのは2つ。それぞれ特徴がある。
    - 'html.parser' Python標準ライブラリなのですぐに使える。速度は遅い
    - 'lxml' 高速なlxmlライブラリ。C依存するので環境に実行環境ごとのビルドが必要。
    """

    # HTML文字列コンテンツ引数に生成する。
    soup = BeautifulSoup('<html><body>hoge</body></html>', 'html.parser')
    print(soup)

    # ファイルハンドルを引数に生成
    with open('index.html') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    print(soup)

    # URLからHTTPリクエストを投げて取得するようなAPIは無い
    # requestsなどの別モジュールを使って取得する

    res = requests.get('http://b.hatena.ne.jp/hotentry')
    soup = BeautifulSoup(res.content, 'html.parser')

    print(soup)

if __name__ == '__main__':
    main()
