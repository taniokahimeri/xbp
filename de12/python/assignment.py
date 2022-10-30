
for i in range(1,4):
    print(i,"人目")


    maru= 0
    
    print("これから電車クイズを始めます!3人の中で一番横浜の電車について知っている人は誰なのか⁉")

    k = input("横浜駅に入っている鉄道会社数は？　選択肢:10,6,5")
    if k == "6":
        print("正解")
        maru = maru + 1
    else:
        print("不正解　正解は6でした。")

    n = input("みなとみらい線の駅数は？　選択肢:5,6,2")    
    if n == "6" :
        print("正解")
        maru = maru + 3
    else:
        print("不正解　正解は6でした。")

    g = input("神奈川県の全駅数は？　選択肢:251,97,371")
    if g == "371":
        print("正解")
        maru = maru + 9
    else:
        print("不正解　正解は371でした。")

    w = input("神奈川県の駅がない場所は？ 選択肢:綾瀬市,中井町,座間市")    
    if w == "綾瀬市" :
        print("正解")
        maru = maru + 7
    else:
        print("不正解　正解は綾瀬市でした。")
        
    print("終了！　あなたの点数は20点満点中ー", maru , "点です")