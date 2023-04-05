from class_module import PC  # Import Module

while 1>0:
    print("COMPUTER LAB MANAGEMENT SYSTEM \n")
    print("------------------------------ \n")
    print("Here is the main menu\n")
    print("1: Add a new PC")
    print("2: Search PC")
    print("3: Update PC")
    print("4: Remove PC")
    print("5: Show all PC info")
    print("6: Save all PC info")
    print("7: EXIT!\n")

    choice = input("Waiting for Input: \n")

    if choice == '1':
        PC.add_pc(PC)

    elif choice == '2':
        n = input("Enter PC number to search: ")
        PC.search_pc(n)

    elif choice == '3':
        PC.show_all_pc()
        n = input("Enter PC number to be updated: ")
        
        pc_exists = PC.search_pc(n)
        if pc_exists != 0:
            print(f"\nFor {n} selected PC")
            new_pc_num = input("\nEnter new PC number: ")
            new_pc_os = input("\Enter new PC'S operating system: ")
            new_pc_stat = input("\Enter new PC'S status: ")
            PC.update_pc(pc_exists, new_pc_num, new_pc_os, new_pc_stat)

    elif choice == '4':
        pc_num = input("\nEnter PC number to remove: ")
        pc_exists = PC.search_pc(pc_num)
        if pc_exists != 0:
            PC.remove_pc(pc_exists)

    elif choice == '5':
        PC.show_all_pc()

    elif choice == '6':
        PC.save_file()

    elif choice == '7':
        quit()