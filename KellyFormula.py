def KellyFormula(listW):
    #listMoney回测资金量的list
    def funG(f):
        answerG = -1
        for iTerListW in range(0,len(listW)):
            answerG = answerG * (1+f*listW[iTerListW])
        return answerG
    res = minimize(funG, 0.5)
    answer = res['x']
    return answer