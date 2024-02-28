def main():
    names_set = set()
    while True:
        name = input("Enter  name (or press Enter to finish): ")
        if not name:
            break
        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    print("\nList of names entered:")
    for name in names_set:
        print(name)

if __name__ == "__main__":
    main()
