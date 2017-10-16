from scrapy.http import HtmlResponse

res = HtmlResponse(url="http://example.com", body=b"""
    <html>
    <body>
        <div id="main">
            <ul>
                <li data="1">list1</li>
                <li data="2" class="even">list2</li>
                <li data="3">list3</li>
            </ul>
            <div>aaa<div>bbb</div></div>
        </div>
        <div id="sub">
            <ul>
                <li data="1">list4</li>
                <li data="2" class="even">list5</li>
                <li data="3">list6</li>
            </ul>
            <div>ccc<div>ddd</div></div></div>
    </body>
    </html>
""")

# text要素をextract
print("#liのtext要素取得")
print(res.xpath('//li/text()').extract())
print(res.css('li::text').extract())

# 最初の要素をextract
print("#最初の要素取得")
print(res.xpath('//li/text()').extract_first())     # extract_first
print(res.xpath('//li/text()')[0].extract())     # selectorの1要素目からextract

print(res.css('li::text').extract_first())
print(res.css('li::text')[0].extract())

# id指定でフィルタ
print("#id指定")
print(res.xpath('//div[@id="main"]//li/text()').extract())  # [@id="main"]
print(res.css('div#main li::text').extract())               # #main

# class指定でフィルタ
print("#class指定")
print(res.xpath('//div[@id="main"]//li[@class="even"]/text()').extract())  # [@class="even"]
print(res.css('div#main li.even::text').extract())               # .even

# 属性指定でフィルタ
print("#属性指定")
print(res.xpath('//div[@id="main"]//li[@data="3"]/text()').extract())  # [@data="3"]
print(res.css('div#main li[data="3"]::text').extract())               # [data="3"]

# 直下の子要素指定でフィルタ
print("#直下の子要素指定")
print(res.xpath('//div[@id="main"]/div/text()').extract())  #  //divなら["aa", "bb"]になる
print(res.css('div#main>div::text').extract())  # div#main divなら["aa", "bb"]になる 

# 属性取得
print("#属性の取得")
print(res.xpath('//li/@data').extract())
print(res.css('li::attr(data)').extract())

# Elementを取得してループ
print("#Elementを取得してループ")
for elm in res.xpath("//li"):
    #liの要素まで取得してからさらにそこからxpathで取得 
    data = elm.xpath('@data').get()
    text = elm.xpath('text()').get()
    print("{}\t{}".format(data, text))
print()
for elm in res.css("li"):
    #liの要素まで取得してからさらにそこからcssで取得 
    data = elm.css('::attr(data)').get()
    text = elm.css('::text').get()
    print("{}\t{}".format(data, text))


