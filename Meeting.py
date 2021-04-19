def meeting(s):
    # sort ohne key funktioniert hier, weil die Einträge in string Form vorliegen, d.h. er geht Buchstabe für Buchstabe durch 

    # names = s.split(";")
    # upper = ["(" + entry.split(":")[1].upper() + ", " + entry.split(":")[0].upper() + ")" for entry in s.split(";")]
    # upper.sort()
    # return "".join(upper)
    return "".join(sorted(["(" + entry.split(":")[1].upper() + ", " + entry.split(":")[0].upper() + ")" for entry in s.split(";")]))


strng = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
strng = "John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell"
print(meeting(strng))
