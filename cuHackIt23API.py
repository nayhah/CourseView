import urllib.request
import re

def getRMPInfo(FirstName, LastName):

    startingURL = "https://www.ratemyprofessors.com/search/teachers?query=" + FirstName + "%20" + LastName + "&sid=U2Nob29sLTI0Mg=="

    with urllib.request.urlopen(startingURL) as url:
        s = url.read().decode()
        RMPScore = re.search("\"avgRating\":(.*),\"numRatings",s).group(1)
        RMPDiff = re.search("\"avgDifficulty\":(.*),\"department",s).group(1)
        RMPTA = re.search("\"wouldTakeAgainPercent\":(.*),\"avgDiff",s).group(1)
        output = [RMPScore, RMPDiff, RMPTA]
    return output

def getCourseInfo(CourseTitle, CourseNum):
    StartingURL = "https://catalog.clemson.edu/search_advanced.php?cur_cat_oid=35&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=" + CourseTitle + "+" + str(CourseNum)
    with urllib.request.urlopen(StartingURL) as url:
        s = url.read().decode()
        urlAddon = re.search("href=\"(.*)\" aria-expanded=\"", s)
        newURL = "https://catalog.clemson.edu/" + urlAddon.group(1)
        with urllib.request.urlopen(newURL) as secondURL:
            s = secondURL.read().decode()
            CourseDesc = re.search("<hr>(.*)<br>",s)
            fullStr = CourseDesc.group(1)
            fullStr = re.sub(r'<.+?>', '', fullStr)
            fullStr = re.sub(r'&#.+?;', '', fullStr)
            fullStr = re.sub(' +', ' ', fullStr)
            return fullStr
''' testing
firstName = "Christopher"
lastName = "Plaue"
outList = getRMPInfo(firstName,lastName)
courseDesc = getCourseInfo("CPSC", 1010)
print("RMP Stats for Christopher Plaue:")
print("RMP Score: " + outList[0])
print("Difficulty Rating: " + outList[1])
print("% who would take again: " + outList[2] + "%\n")
print("CPSC 1010 Course Description:")
print(courseDesc)
'''
