from random import randint
import time

hands = ['グー','チョキ','パー']
rules = ['あいこ','負け','勝ち']
win = 0
lose = 0
draw = 0

print('只今より、じゃんけんを開始いたします。')

while True:
    #player
    print('0:グー 1:チョキ 2:パー')
    p = int(input('出す手を数字で入力してください：'))
    print('あなたは、'+hands[p]+'を出しました。')
    time.sleep(1)

    #相手側（PC）
    m = randint(0,2)
    print('PCは、'+hands[m]+'を出しました。')

    #判定
    i = ( p - m )%3
    print(rules[i])
    if i ==0:
        draw += 1
    elif i == 1:
        lose += 1
    else:
        win += 1
    time.sleep(1)

    #結果出力
    print('{}勝/{}負/{}引き分け'.format(win,lose,draw))
    if win == 3:
        print('結果は……')
        time.sleep(1)
        print('You win!　あなたは計3勝しました!')
        break
    if lose == 3:
        print('結果は……')
        time.sleep(1)
        print('You lose。あなたは3敗しました。またのお越しをお待ちしております。')
        break
    time.sleep(1)


