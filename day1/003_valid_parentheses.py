class solution:
    def isValid(self, s:str)->bool:
        hashmap={')':'(','}':'{',']':'['}
        stk=[]
        loop_value=1
        for ch in s:
            print("Loop no ", loop_value)
            print("Current Value of ch ", ch)
            if ch not in hashmap:
                stk.append(ch)

            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[ch]:
                        return False
            print("Value of stack", stk)
        return not stk
        
def main():
    check_value ="[()]"
    t_obj = solution()
    print("Checking Valid Parenthisis for [()]")
    print("The String provided above is ",t_obj.isValid(check_value))


if __name__ == "__main__":
    main()
        