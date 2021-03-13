
# Python script to help the Pacman to reach the goal
# not generic valid for given case

def find(inituple, finaltuple):
    path = []
    start_X = inituple.__getitem__(0)
    start_Y = inituple.__getitem__(1)
    goal_X = finaltuple.__getitem__(0)
    goal_Y = finaltuple.__getitem__(1)
    for x in range(start_X, goal_X + 1):
        for y in range(start_Y, goal_Y + 1):
            if not((x is 2 and y is 1) or (x is 1 and y is 3)):
                if not(x is 1 and y is 1):
                    path.append(tuple([x,y]))
    return path


if __name__ == '__main__':
    print(find((1, 1), (2,3)))
