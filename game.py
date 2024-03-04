import random
import math
import time

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def print_board(px, py, board_size, level, remaining_attempts):
    print(f"\nレベル {level + 1} - 残り試行回数: {remaining_attempts}")
    for y in range(board_size):
        for x in range(board_size):
            if x == px and y == py:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()

def provide_hint(distance, prev_distance, hint_level):
    if hint_level == 0:
        return  # ヒントなし
    elif hint_level == 1:
        if distance < 2:
            print("レーダー感知: ターゲットが非常に近い")
        elif distance < prev_distance:
            print("レーダー感知: ターゲットに近づいています")
        elif distance > prev_distance:
            print("レーダー感知")
    elif hint_level >= 2:
        print(f"レーダー感知: ターゲットまでおよそ {int(round(distance, 0))} の距離です。")

# ゲームのレベルごとの設定
levels = [
    {"board_size": 5, "max_attempts": 2, "hint_level": 2},  # レベル1
    {"board_size": 7, "max_attempts": 1.5, "hint_level": 2},  # レベル2
    {"board_size": 7, "max_attempts": 1.5, "hint_level": 1},  # レベル3
    {"board_size": 9, "max_attempts": 1.5, "hint_level": 1},  # レベル4
    {"board_size": 9, "max_attempts": 1.2, "hint_level": 1},  # レベル5
]

for level_index, level in enumerate(levels):
    board_size = level["board_size"]
    max_attempts = int(board_size * level["max_attempts"])
    hint_level = level["hint_level"]

    target_x = random.randrange(0, board_size)
    target_y = random.randrange(0, board_size)

    player_x = random.randrange(0, board_size)
    player_y = random.randrange(0, board_size)

    attempt_count = 0
    prev_distance = calc_distance(player_x, player_y, target_x, target_y)

    print(f"\n\n\nレベル {level_index + 1} 開始!")
    while attempt_count < max_attempts:
        remaining_attempts = max_attempts - attempt_count
        print_board(player_x, player_y, board_size, level_index, remaining_attempts)
        distance = calc_distance(player_x, player_y, target_x, target_y)

        provide_hint(distance, prev_distance, hint_level)

        if distance < 1:
            print("大成功! ターゲットにヒットしました!")
            time.sleep(1)
            if level_index == len(levels) - 1:  # 最終レベルの場合
                print("おめでとうございます! 全てのレベルをクリアしました!")
            break

        direction = input("H: ←、J: ↓、K: ↑、L: → >> ").lower()
        if direction == 'h' and player_x > 0:
            player_x -= 1
        elif direction == 'j' and player_y < board_size - 1:
            player_y += 1
        elif direction == 'k' and player_y > 0:
            player_y -= 1
        elif direction == 'l' and player_x < board_size - 1:
            player_x += 1
        else:
            print("不正な入力です。")
            continue

        attempt_count += 1
        prev_distance = distance

    if attempt_count >= max_attempts and level_index < len(levels) - 1:
        print("残念! 試行回数が最大に達しました。ゲームオーバーです。")
        break
