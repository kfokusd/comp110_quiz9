##
## Function: match_parthesis()
## - Recursive function to return True if all parthesis, "()" or square bracket, "[]", are matching
## - Takes 1 parameter with String type
## 
def match_parthesis(szStr):
    ## TODO: Implement your function here
    return True     # TODO: You need to modify this line

##
## Please DO NOT change the following
##
print(match_parthesis("()"))            # True 
print(match_parthesis("(()"))           # False 
print(match_parthesis("(((())))"))      # True 
print(match_parthesis("(((())))))"))    # False 
print(match_parthesis(""))              # True 
print(match_parthesis("[((([])))]"))    # True
print(match_parthesis("[(x[])))]"))     # False
print(match_parthesis("[(((x)))]"))     # True
print(match_parthesis("(((x)))"))       # True
print(match_parthesis("((x)))"))        # False