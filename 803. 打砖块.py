def hitBricks(grid, hits):
    cnts = []


    row_num = len(grid)
    line_num = len(grid[0])

    for hit in hits:
        cnt = 0

        grid[hit[0]][hit[1]] = 0
        g = grid
        g.reverse()
        # g_r = zip(*g)
        print('------------------')

        for i, row in enumerate(g):
            print(row)

            for j, point in enumerate(row):
                if point:
                    up_flag = False if i == row_num else True
                    down_flag = False if i == 0 else True
                    left_flag = False if j == 0 else True
                    right_flag = False if j == line_num else True

                    up_point = True if up_flag or g[i + 1][j] else False
                    down_point = True if down_flag or g[i - 1][j] else False
                    left_point = True if not left_flag and g[i][j - 1] else False
                    right_point = True if not right_flag and g[i][j + 1] else False

                    move_down = not any((up_point, down_point, left_point, right_point))
                    print(up_point, down_point, left_point, right_point)

                    if move_down:
                        g[i][j] = 0
                        move_flag = False
                        for ii in range(i, 0, -1):
                            if g[ii][j]:
                                g[ii + 1][j] = 1
                                move_flag = True
                        if not move_flag:
                            g[0][j] = 1
                        cnt += 1
        grid = g
        cnts.append(cnt)
    return cnts


hitBricks(
[[1,0,0,0],
 [1,1,1,0]],
[[1,0]]
)

# hitBricks([
#     [1,0,0,0,1],
#     [1,1,1,0,1],
#     [1,1,1,0,1],
#     [1,1,1,0,1],
#     [1,1,1,0,1],
# ],
#
#
#           [[1,0]])