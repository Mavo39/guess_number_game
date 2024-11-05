import random

def guess_number_game():
    # ユーザー入力項目
    n = int(input('開始値nを入力してください: '))
    m = int(input('終了値mを入力してください: '))

    # ランダムなナンバーを生成
    random_number = random.randint(n, m)

    # 試行回数を制限
    max_attempts = 5
    print(f'{max_attempts}回以内に数字を当ててください！')

    # ループ処理
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f'{attempt}回目の推測: '))

        if guess == random_number:
            print(f'おめでとうございます！{attempt}回目で正解しました！')
            break

        elif guess < random_number:
            print('（ヒント）数字が小さいです。')

        else:
            print('（ヒント）数字が大きいです。')

    # 試行回数が上限に達した場合
    else:
        print(f'残念でした。正解は{random_number}でした。')

guess_number_game()