'''
1=A,2=B,3=C…という謎解きでよくある数字をアルファベットに直すやつです
大文字になります
'''
#標準入力から半角区切りで受け取った値をリストに格納
numList = input().rstrip().split(" ")
print(len(numList))

# 受け取った回数分回す
for i in range(len(numList)): 
#リストから1個とりだし
    num = int(numList[i])
    # 数字をアスキーコードに変換して解読
    num = 64 + num
    # アスキーコードから文字になおして改行せずに出力
    print(chr(num), end="")
