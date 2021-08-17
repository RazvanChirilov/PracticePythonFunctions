# daca banda rulanta are mai multe item-uri decat cealalta, returneaza ultimul item al benzii
# daca numarul de itemuri de pe benzi este egal, returneaza ultimul item de la al primei benzi
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    return lst2[-1]




