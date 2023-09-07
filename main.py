n, m = list(map(int, input().split()))
room = []
for _ in range(n):
    room.append(list(input()))
c, r = list(map(int, input().split()))
current_pos = [r, c]
input()
direction = 90
movements = list(input())
counter = 1
room[r - 1][c - 1] = '+'
for move in movements:
    if move == 'R':
        direction -= 90
        if direction < 0:
            direction += 360
    elif move == 'L':
        direction += 90
        direction %= 360
    elif move == 'M':
        pot_pos = current_pos.copy()
        if direction == 0:
            pot_pos[0] += 1
        elif direction == 90:
            pot_pos[1] += 1
        elif direction == 180:
            pot_pos[0] -= 1
        elif direction == 270:
            pot_pos[1] -= 1
        if not 0 < pot_pos[0] <= m or not 0 < pot_pos[1] <= n:
            continue
        if room[pot_pos[1] - 1][pot_pos[0] - 1] == '.':
            room[pot_pos[1] - 1][pot_pos[0] - 1] = '+'
            current_pos = pot_pos
            counter += 1
        elif room[pot_pos[1] - 1][pot_pos[0] - 1] == '+':
            current_pos = pot_pos
print(counter)

