def afficher_tableau(data):

    if not data:
        print("Aucune donnée.")
        return

    headers = list(data[0].keys())

    # largeur des colonnes
    col_widths = {
        h: max(len(str(h)), max(len(str(row[h])) for row in data))
        for h in headers
    }

    # ligne séparation
    line = "+".join("-" * (col_widths[h] + 2) for h in headers)

    print("\n" + line)

    # entêtes
    header_row = " | ".join(f"{h:{col_widths[h]}}" for h in headers)
    print(header_row)

    print(line)

    # lignes
    for row in data:
        row_str = " | ".join(f"{str(row[h]):{col_widths[h]}}" for h in headers)
        print(row_str)

    print(line + "\n")
    
    
    
def choisir_element(data, message="Choisir un élément : "):

        if not data:
            print("Aucune donnée disponible.")
            return None

        choix = int(input(message))

        if choix < 1 or choix > len(data):
            print("❌ Choix invalide")
            return None

        return data[choix-1]