import os

attivita = []

# Carica le attività salvate
if os.path.exists("attivita.txt"):
    with open("attivita.txt", "r", encoding="utf-8") as f:
        attivita = [line.strip() for line in f.readlines()]

while True:
    print("\n--- MENU ---")
    print("1. Aggiungi attività")
    print("2. Rimuovi attività")
    print("3. Visualizza elenco")
    print("4. Esci")

    scelta = input("Scegli un'opzione (1-4): ")

    if scelta == "1":
        nuova = input("Scrivi l'attività: ")
        attivita.append(nuova)
        print("Attività aggiunta!")

    elif scelta == "2":
        for i, item in enumerate(attivita):
            print(f"{i + 1}. {item}")
        numero = int(input("Numero dell'attività da rimuovere: ")) - 1
        if 0 <= numero < len(attivita):
            rimossa = attivita.pop(numero)
            print(f"Rimossa: {rimossa}")
        else:
            print("Numero non valido.")

    elif scelta == "3":
        if not attivita:
            print("Nessuna attività.")
        else:
            print("\n--- Elenco ---")
            for i, item in enumerate(attivita):
                print(f"{i + 1}. {item}")

    elif scelta == "4":
        with open("attivita.txt", "w", encoding="utf-8") as f:
            for item in attivita:
                f.write(item + "\n")
        print("Salvato. Arrivederci!")
        break

    else:
        print("Scelta non valida.")