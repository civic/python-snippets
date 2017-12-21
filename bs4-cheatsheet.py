import requests
from bs4 import BeautifulSoup


def main():
    #making_soup()

    navigation()

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
                <li><a href="http://www.google.com/">google.com</a></li>
            </ul>
        </body>
    </html>''', 'html.parser')

    # 子要素をたぐる
    print(soup.head)
    print(soup.head.title)  # headの下のtitle

    # find_allは全検索してリストで返す
    li_elements = soup.find_all("li")
    print(li_elements)
    # findは検索して最初に見つかった1つ目
    first_li_element = soup.find('li')
    print(first_li_element)

    #属性も検索条件につける
    anchors_to_google = soup.find_all("a", href="http://www.google.com/")
    print(anchors_to_google)

    # classは予約後なのでアンダースコア付加
    first_link_element = soup.find("a", class_="first")
    print(first_link_element)

    print(first_link_element['href'])   # 属性取得
    print(first_link_element.string)    # テキスト要素

    # stringとcontentsの違い
    print(soup.body.string) #直下のテキスト要素
    print(soup.body.contents)   #配下のすべてのsoupオブジェクト

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
