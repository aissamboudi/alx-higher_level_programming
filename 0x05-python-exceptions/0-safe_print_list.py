def safe_print_list(my_list=[], x=0):
    cpt = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            cpt += 1
        except IndexError:
            break
    print("")
    return (cpt)