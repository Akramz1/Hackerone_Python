if __name__ == '__main__':
    name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name, score])
    newlist = sorted(set(score for name, score in name_score))
    lowest = newlist[1]
    res = [name for name, score in name_score if score == lowest]
    res.sort()
    for i in res:
        print(i)
