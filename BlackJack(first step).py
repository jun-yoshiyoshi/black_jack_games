#入門編
# #ディーラーとプレイヤー２人に２枚ずつカードを配る
#ディーラーのカードは１枚伏せる
#カードの合計値が２１に近づくように
#カードの追加（ヒット）をしたり、追加をしない（スタンド）を選択します。
# カードの合計値が２１を越えた時点で、負けが決定します。
#プレイヤーは合計値が２１を越えない限り、何度でもカードを追加できます。
#ディーラーは合計値が１７を越えるまで必ずカードを追加します。

#２から９のカードの値はそのまま２～９となる。
#１０と絵札（Ｊ，Ｑ、Ｋ）のカードは全て１０とする。
#Ａのカードは１と１１のうち、有利な方で数える。

#プログラミング的思考
#(deck)　トランプを作る：　数字を数えられるようにする。
# (deal)　トランプを２マイ配る：絵札(J,Q,K)で表示させる。
# (hand)  プレイヤーに配られたカードを記録する
#(hit)  ヒットの場合handを追加する
#(game) 　実際にプレーする
#(total)　合計値を求める
#ＴＯＤＯ　(result) 勝ち負けを表記する
#(play_again) リプレイ

import random

deck =[1,2,3,4,5,6,7,8,9,10,11,12,13]*4


def deal():
    hand =[]
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if  card == 11:
            card ="J"
        if  card == 12:
            card ="Q"
        if  card == 13:
            card ="K"
        if  card == 1:
            card ="A"
        hand.append(card)
    return hand
            

def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if  card == 11:
        card ="J"
    if  card == 12:
        card ="Q"
    if  card == 13:
        card ="K"
    if  card == 1:
        card ="A"
    hand.append(card)
    return hand
            
def total(hand):
    score = 0
    for card in hand:
        if card =="J" or card =="Q" or card =="K":
            score +=10
        elif card == "A":
            if score >=11:
                score += 1
            else:
                score += 11
        else:
            score +=card
    return score

def play_again():
    again =input("もう一度プレイしますか？（Ｙ/Ｎ）:")
    if again =="Y" or again =="y":
        #game()
        return
    else:
        print("お疲れ様でした！")
        exit()

def result(dealer_hand,player_hand):
    if total(player_hand)>total(dealer_hand):
        print(f"ディーラーの合計は{total(dealer_hand)},あなたの合計は{total(player_hand)}です。YOU　WIN")
        choice = quit
    if total(player_hand)<total(dealer_hand):
        print(f"ディーラーの合計は{total(dealer_hand)},あなたの合計は{total(player_hand)}です。YOU　LOSE")
        choice = quit
    if total(player_hand)==total(dealer_hand):
        print(f"ディーラーの合計は{total(dealer_hand)},あなたの合計は{total(player_hand)}です。PUSH")
        choice = quit

def game():
    dealer_hand =deal()
    player_hand =deal()
    print(f"ディーラーの見せ札は{dealer_hand[0]}です。")
    print(f"プレイヤーは{player_hand}です。")

    choice = 0

    while choice !=quit:
        choice = input("ヒットしますか？スタンドしますか？(Hit/Stand):").lower()
        if choice == "hit":
            hit(player_hand)
            print(f"あなたのカードは{player_hand[-1]}が配られ、カードは{player_hand}で合計は{total(player_hand)}となります。")
            if total(player_hand)>21:
                print("あなたはバーストしました。YOU LOSE...")
                choice =quit
        elif choice =="stand":
            print(f"あなたの合計は{total(player_hand)}です。")
            print(f"ディーラーの２枚目のカードは{dealer_hand[1]}合計は{total(dealer_hand)}です。")
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(f"ディーラーの新しいカードは{dealer_hand[-1]}です。")
            
                if total(dealer_hand)>21:
                    print("ディーラーはバーストしました。YOU WIN")
                    choice =quit
            if total(dealer_hand)<=21:
                result(dealer_hand,player_hand)
                choice =quit
    
    

game()