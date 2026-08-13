def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Basit Not Yöneticisi ---")
    print("1. Not Ekle")
    print("2. Notları Listele")
    print("3. Not Sil")
    print("4. Çıkış")
    print("---------------------------")

def add_note(notes):
    """Prompts the user for a note and adds it to the list."""
    note = input("Eklemek istediğiniz notu girin: ")
    notes.append(note) # Demonstrates adding an item to a list, a basic data structure.
    print(f"'{note}' notu eklendi.")

def list_notes(notes):
    """Displays all notes with their indices."""
    if not notes:
        print("Henüz hiç notunuz yok.")
        return
    print("\n--- Notlarınız ---")
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}") # Iterating through a list and displaying elements.
    print("------------------")

def delete_note(notes):
    """Prompts the user for a note index and deletes it."""
    list_notes(notes) # Show notes first
    if not notes:
        return

    try:
        index_to_delete = int(input("Silmek istediğiniz notun numarasını girin: ")) - 1
        # Conditional logic (if/else) to check for valid input and list bounds.
        if 0 <= index_to_delete < len(notes):
            deleted_note = notes.pop(index_to_delete) # Demonstrates removing an item from a list.
            print(f"'{deleted_note}' notu silindi.")
        else:
            print("Geçersiz not numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def main():
    """Main function to run the note manager application."""
    notes = [] # This list is a fundamental data structure, often taught early in CS.

    while True: # A 'while' loop is a common control flow structure for interactive programs.
        display_menu()
        choice = input("Seçiminizi yapın (1-4): ")

        # 'if/elif/else' statements demonstrate conditional logic, directing program flow.
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            list_notes(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            print("Not yöneticisinden çıkılıyor. Hoşça kalın!")
            break # Exits the loop, ending the program.
        else:
            print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
