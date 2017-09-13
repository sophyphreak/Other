'''
This is a counter for reading a book to tell you how many pages you have left.
'''

def setPage(curOrEnd):
    #input string "current" or "end"
    message = "What is the " + curOrEnd + " page? "
    page = input(message)
    try:
        page = int(page)
    except:
        print('Please enter an integer')
        return page(curOrEnd)
    return page

def pagesTurned():
    print()
    turned = input("? ")
    if turned == "":
        return 1
    else:
        try:
            turned = int(turned)
        except:
            if turned == "restart":
                return turned
            else:
                print("Please enter an integer")
                return pagesTurned()
        return turned
def main():
    restart = False
    currentPage = setPage("current")
    endPage = setPage("end")
    print()
    print(endPage - currentPage, "pages left")
    while(endPage - currentPage > 0):
        pageTurn = pagesTurned()
        if pageTurn == "restart":
            restart = True
            break
        currentPage += pageTurn
        print()
        print("You are on page", str(currentPage) + ".")
        print("You have", endPage - currentPage, "pages left.")
    if restart == True:
        main()
    else:
        print("You're done!")

main()
