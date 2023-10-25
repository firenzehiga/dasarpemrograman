
cuaca = input ("apakah cuaca pad hari ini?")

match cuaca:
    case "panas":
        print("ke kampus memakai mobil")
    case "hujan":
        print("ke kampus memakai jas ujan")
    case "badai":
        print("tidak berangkat ke kampus")
    case _:
        print("tetap berangkat ke kampus")