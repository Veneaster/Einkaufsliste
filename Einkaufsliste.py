# Importiere wichtige Module für Dateien & System
from pathlib import Path
import sys

# Pfad zur Datei, wo die Liste gespeichert wird
FILE = Path(__file__).with_name('shopping_list.txt')


def load_items(path: Path = FILE) -> list:
    """Load items from a text file."""
    # Falls Datei nicht existiert — leere Liste zurückgeben
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as f:
        items = [line.rstrip('\n') for line in f]
    return [it for it in items if it.strip()]  # remove empty lines


def save_items(items: list, path: Path = FILE) -> None:
    """Save items into a text file."""
    # Öffnet die Dat und speichert jede Zeile
    with path.open('w', encoding='utf-8') as f:
        for it in items:
            f.write(f"{it}\n")


def print_items(items: list) -> None:
    """Print the shopping list."""
    if not items:
        print("\nYour shopping list is empty.\n")
        return

    print("\nCurrent Shopping List:")
    for i, it in enumerate(items, start=1):
        print(f"  {i}. {it}")
    print()


def add_item(items: list, name: str) -> None:
    """Add a new item to the list."""
    # Entfernt Leerzeichen links/rechts
    name = name.strip()
    if not name:
        print("Item name cannot be empty.")
        return

    items.append(name)
    print(f'Added: "{name}"')


def remove_item(items: list, key: str) -> None:
    """Remove an item by index or name."""
    key = key.strip()
    if not key:
        print("Enter a number or name to remove.")
        return

    # Versuche zuerst, ob es eine Nummer ist
    if key.isdigit():
        idx = int(key) - 1
        if 0 <= idx < len(items):
            removed = items.pop(idx)
            print(f'Removed: "{removed}"')
            return
        else:
            print("Invalid number.")
            return

    # Falls Name — entferne erste passende Zeile
    try:
        items.remove(key)
        print(f'Removed: "{key}"')
    except ValueError:
        print("Item not found.")


def clear_items(items: list) -> None:
    """Clear the whole list after confirmation."""
    # Sicherheitsfrage
    confirm = input("Are you sure you want to clear the whole list? (y/N): ").strip().lower()
    if confirm == 'y':
        items.clear()
        print("List cleared.")
    else:
        print("Cancelled.")


def menu():
    # Lade bestehende Items aus Datei
    items = load_items()
    print("Einkaufsliste — Simple Shopping List CLI Application")

    while True:
        print("\nMenu:\n 1) Show List\n 2) Add Item\n 3) Remove Item\n 4) Clear List\n 5) Save to File\n 6) Load from File\n 7) Exit")
        choice = input("\nChoose an option (1-7): ").strip()

        if choice == '1':
            print_items(items)
        elif choice == '2':
            name = input("Item name: ")
            add_item(items, name)
        elif choice == '3':
            key = input("Number or name to remove: ")
            remove_item(items, key)
        elif choice == '4':
            clear_items(items)
        elif choice == '5':
            save_items(items)
            print(f"Saved to {FILE.name}")
        elif choice == '6':
            items = load_items()
            print("Loaded from file.")
        elif choice == '7':
            ans = input("Save before exit? (Y/n): ").strip().lower()
            if ans in ('', 'y', 'yes'):
                save_items(items)
                print(f"Saved to {FILE.name}")
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Bye!")
        sys.exit(0)
