symbols = ["=", "+", "-", "/", " "]


# ask for the equasion
print("please format as 'ax/b + c = d', make a, b, c and d as integers")
eqa = input("What is the equasion?\n")

def solve_eqa(eqa, symbols):

    multi_bool = False
    pm_bool = False
    div_bool = False
    multi_neg = False

    # making useful things

    def is_int(num):
        try:
            int(num)
            return True
        except:
            return False

    # finds the unknowns

    var = []

    for char in eqa:
        if is_int(char) or char in symbols:
            continue
        else:
            var.append(char)

    if len(var) > 1:
        # makes sure its not a simult eqa or some line or somethin
        print("Please only put ONE variable in your equasion")
    elif "." in var:
        # gets rid of floats
        print("No decimals or fractions please, i dont know how to do them!")    
    else:
        # finds location of the unknown
        var = var[0]
        place = eqa.find(var)

        # finds the adder
        if not eqa.find("+") < 1:
            pm_pos = eqa.find("+")
            pm_bool = True
        else:    
            if not eqa.find("-") < 1:
                pm_pos = eqa.find("-")
                pm_bool = True

        if pm_bool:
            adder = eqa[pm_pos:]
            adder = adder[:adder.find("=")]
            adder = adder.replace(" ", "")
            adder = int(adder)

        # finds the multiplier
        if place != 0:
                if eqa[0] == "-":
                    multi_neg = True

                if multi_neg:
                    multi = eqa[1:place]
                    multi = int(multi)
                    multi = -multi
                    
                else:
                    multi = eqa[:place]
                    multi = int(multi)

                multi_bool = True




        # finds the divisor
        # FIX THIS ASAP   

        if eqa[place + 1] != " ":
            if eqa[place + 2] == "-":
                if pm_bool:
                    div = eqa[place + 3:pm_pos - 1]
                else:
                    div = eqa[place + 3:eqa.find("=") - 1]

                div = int(div)
                div = -div
                
            else:
                if pm_bool:
                    div = eqa[place + 2:pm_pos - 1]
                else:
                    div = eqa[place + 2:eqa.find("=") - 1]

                div = int(div)

            div_bool = True
        
        # finds the post = number

        equal = eqa[eqa.find("=") + 1:]
        equal = equal.replace(" ", "")
        equal = int(equal)

        # finally soves the eqaaaaa, vibes!!!!

        if pm_bool:
            equal = equal - adder

        if div_bool:
            equal = equal * div

        if multi_bool:
            equal = equal / multi

        answer = equal

        if is_int(answer):
            answer = int(answer)

        return(answer)


print(solve_eqa(eqa, symbols))