def swapRow (givenList , answer , j , k):
    for i in range(len(givenList)):
        temp = givenList[j][i]
        givenList[j][i] = givenList[k][i]
        givenList[k][i] = temp

    temp = answer[j][i]
    answer[j][i] = answer[k][i]
    answer[k][i] = temp

    return

def correct(givenList , answer):
    for i in range(len(givenList)):
        if (givenList[i][i] == 0):
            temp_i = i
            toSwap = -1
            for j in range (i , len(givenList)):
                if (givenList[j][i] != 0):
                    toSwap = j
                    break

            if (toSwap != -1):
                swapRow(givenList ,answer , temp_i , toSwap)
                break

    return

def solve (givenList , answer):
    for i in range(len(givenList)):
        if (givenList[i][i] == 0):
            correct(givenList , answer)
        pivot = givenList[i][i]
        for j in range(len(givenList)):
            if (j == i):
                continue

            coef = (givenList[j][i] / givenList[i][i]) * (-1)
            for k in range(len(givenList)):
                givenList[j][k] += givenList[i][k] * coef

            answer[j] += answer[i] * coef

    for i in range (len(givenList)):
        div = givenList[i][i]
        answer[i] /= div
        givenList[i][i] /= div

    return answer
