import os

file_path = input("Inserisci il percorso del file C++: ")

if file_path.endswith(".cpp"):
    # Ottieni il nome del file senza l'estensione .cpp
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Definisci il nome del file eseguibile e il percorso di output
    exe_name = file_name + ".exe"
    output_path = os.path.dirname(os.path.abspath(file_path))

    # Esegui il comando di compilazione
    compile_command = "g++ -o " + os.path.join(output_path, exe_name) + " " + file_path
    os.system(compile_command)

    # Mostra un messaggio di conferma
    print("Il file è stato compilato correttamente in:", os.path.join(output_path, exe_name))
else:
    print("Il file selezionato non è un file C++")
