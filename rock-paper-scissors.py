import fileinput

if __name__ == '__main__':
    first_line = True
    cur_first_line = True

    for line in fileinput.input():

        if first_line:
            rounds = min(int(line), 1000)
            first_line = False

        elif rounds > 0:

            if cur_first_line:
                throws = min(int(line), 100)
                cur_first_line = False
                p1 = 0
                p2 = 0

            elif throws > 0:
                player1 = line[0]
                player2 = line[2]

                if player1 == 'R':
                    if player2 == 'S':
                        p1 += 1
                    elif player2 == 'P':
                        p2 += 1
                elif player1 == 'S':
                    if player2 == 'P':
                        p1 += 1
                    elif player2 == 'R':
                        p2 += 1
                elif player1 == 'P':
                    if player2 == 'R':
                        p1 += 1
                    elif player2 == 'S':
                        p2 += 1

                throws -= 1

                if throws == 0:
                    rounds -= 1
                    cur_first_line = True
                    if p1 == p2:
                        print('TIE')
                    elif p1 > p2:
                        print('Player 1')
                    else:
                        print('Player 2')
