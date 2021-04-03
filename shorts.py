
def squares_to_rect(list):
    squares = sorted(list, reverse=True)
    rectangles = []

    i = 0
    for _ in range(len(squares)):
        #print("next i")
        j = len(squares)
        while i != j:#
            area = 0
            #print("next j")
            for cur_sqr in range(i, j):
                area += squares[cur_sqr] ** 2
                #print(area)
            if area % squares[i] == 0:
                long_side = area // squares[i]
                if not long_side == squares[i]:
                    rectangles.append("({} * {})".format(long_side, squares[i]))
                #print(rectangles)
            j -= 1
        i += 1

    # quadrate aller kombinationen mindestens zweier zahlen aus der lsite miteinander addieren und durch den größten wert der seite der addierten
    # quadrate teilen. das ergebnis X und die längste Seite Y sollen dann in folgender Form in der Liste squares ausgegeben werden:
    # "(Y * X)"

    return rectangles

# if __name__ == "__main__":
#     squares_to_rect(list)

liste = [5,5,3,2,1,1]
print(squares_to_rect(liste))

