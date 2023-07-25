import operator
import os

def main(args):

    file = open( "sales.csv", "r+" )
    lines = file.readlines()
    boolHadProblem = False
    max, sum, value = 0, 0, 0

    for line in lines:
        columns  = list(map(operator.methodcaller('strip'), line.split(",")))
    
        try:
            value = int( columns[2] )
            print()
        except:
            boolHadProblem = True
            print(f"parse error: {boolHadProblem}")
 
        if value > max:
            max = value
        
        sum += value

    print(f"top sale   : {max}")
    print(f"revenue    : {sum}")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
