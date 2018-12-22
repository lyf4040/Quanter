def BeforeYearMonth(iYear,iMonth,iLast):
    iMonth = iMonth - iLast
    iYear = iYear + iMonth /12
    iMonth = iMonth%12
    if iMonth > 0:
        if iMonth <10:
            ansMonth = '0' + str(iMonth)
        else:
            ansMonth = str(iMonth)
    else:
        ansMonth = '12'
        iYear = iYear - 1

    strYearMonth = str(iYear) + '-' + ansMonth
    return strYearMonth