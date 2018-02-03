def find3Triplets(trp, n):
    foundnumnum = True
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (trp[i] + trp[j] + trp[k] == 0):
                    print("triplets whose sum is zero is %s" % trp[i], trp[j], trp[k])
                    foundnum = True
    if (foundnum == False):
        print(" not exist ")
trp = [int(x) for x in input("Enter in a list: ").split()]
n = len(trp)
find3Triplets(trp, n)
