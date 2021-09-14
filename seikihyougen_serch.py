import re

s = 'id: deep, mail: deep@foo.com, tel: 03-0123-4567'

# re.search関数は文字列にパターンとマッチする部分があるかを調べる
m = re.search('tel: [-\d]+' or 'mail:[-\d]', s)
print(m)  # <re.Match object; span=(30, 47), match='tel: 03-0123-4567'>
r = m.group()  # re.Matchオブジェクトのgroupメソッドでマッチ全体を抽出
print(r)  # tel: 03-0123-4567

# re.match関数は文字列の先頭とパターンがマッチするかを調べる
m = re.match('tel: [-\d]+', s)  # 「tel: 03-……」は先頭にはないので
print(m)  # これはNoneとなる

m = re.match('\w+: [-\w@.]+', s)  # 文字列先頭が「\w+: [-\w@.]+」にマッチするか
print(m)  # <re.Match object; span=(0, 8), match='id: deep'>
r = m.group()
print(r)  # id: deep

# re.search関数が返すのは最初にマッチした部分を表すre.Matchオブジェクト
m = re.search('\w+: [-\w@.]+', s)
print(m)  # <re.Match object; span=(0, 8), match='id: deep'>
print(m.group())  # id: deep

# 全てのre.Matchオブジェクトを取得するにはre.finditer関数を使う
m_iter = re.finditer('\w+: [-\w@.]+', s)
for m in m_iter:
    print(m.group())
# 出力結果：
# id: deep
# mail: deep@foo.com
# tel: 03-0123-4567

# re.Matchオブジェクトのメソッドを使って抽出する文字列をカスタマイズする
m = re.match('id: \w+', s)

start = m.start()  # マッチ全体の開始位置を取得
end = m.end()  # マッチ全体の終了位置を取得
print(f'start: {start}, end: {end}')  # start: 0, end: 8
print(f'span of match: {s[start:end]}')  # span of match: id: deep

start, end = m.span()  # マッチ全体の開始位置と終了位置を取得
print(f'span of match: {s[start:end]}')  # span of match: id: deep

m = re.match('id: (\w+)', s)  # グループを指定
r = m.group()  # マッチ全体を取得
print(r)  # id: deep
r = m.group(1)  # 最初のグループを取得
print(r)  # deep