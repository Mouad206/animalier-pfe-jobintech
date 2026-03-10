def afficher_tableau(data):

    if not data:
        print("Aucune donnée")
        return

    headers = list(data[0].keys())

    print("-" * 80)
    print(" | ".join(headers))
    print("-" * 80)

    for row in data:
        print(" | ".join(str(row[h]) for h in headers))

    print("-" * 80)