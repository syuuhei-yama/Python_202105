#練習問題 3 ジャンケン
def generater_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"

def is_win(my_hand, enemy_hand):
    if my_hand == "1" and enemy_hands == "2":
        return True
    elif my_hand == "2" and enemy_hands == "3":
        return True
    elif my_hand == "3" and enemy_hands == "1":
        return True
    return False

hands_dict = {
    "1" : "グー",
    "2" : "チョキ",
    "3" : "パー"
}
from random import randint
lose_count = 0
enemy_hands = generater_enemy_hand()

while True:
    my_hand = input("自分の手は何を出しますか？　1:グー, 2:チョキ, 3:パー")
    if my_hand not in ("1","2","3"):
        print("間違った入力です")
        continue
    enemy_hands =  str(randint(1, 3))
    print("あなたの出したては: {}, 相手の出した手は: {}".format(hands_dict.get(my_hand), hands_dict.get(enemy_hands)))
    if my_hand == enemy_hands:
        print("あいこ")
    elif is_win(my_hand, enemy_hands):
        print("あなたは勝ちまたした")
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print("負けました")
            break
        else:
            print("あなたは負けました。再チャレンジ")

