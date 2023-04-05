class PC:
    all_pc = [] # stores all instances of the class 

    def __init__(self, pc_num, pc_os, pc_status):  
        self.number = pc_num
        self.os = pc_os
        self.status = pc_status

        PC.all_pc.append(self)
        print(f"\n New PC Registered\n")  #Adds to the list

    def add_pc(self):  #Adding  New Computer
        print("Enter new PC details:-\n")
        pc_num = input("PC number: ")
        pc_os = input("PC operating system: ")
        pc_status = input("PC status: ")

        pc_exists = PC.check_pc(pc_num)  # check for duplicates

        if pc_exists == 0:   
            new_pc = PC(pc_num, pc_os, pc_status)  #Adding PC object to the list object


        else:
            print("\n PC with same number already exists\n")
            print("To update pc number - press '1'")
            print("TO remove pc - press '2'")
            print("TO cancel - press '3'")

            i = input("\n Waiting for input: ")

            if i == '1':
                new_pc_num = input("\n New pc number: ")
                PC.update_pc(pc_exists, new_pc_num, pc_exists.os,
                                       pc_exists.status)
                new_pc = PC(pc_num, pc_os, pc_status)
            elif i == '2':
                PC.remove_pc(pc_exists)
                new_pc = PC(pc_num, pc_os, pc_stat)
            elif i == '3':
                PC.Main()
            else:
                PC.Main()

    def remove_pc(computer):  #Delete PC
        print(f"\n {computer.number} is deleted")
        PC.all_pc.remove(computer)

    def update_pc(computer, new_pc_num, new_pc_os, new_pc_status):  #Update Information
        if PC.check_pc(new_pc_num) == 0:
            old_pc_num = computer.number
            computer.number = new_pc_num
            computer.os = new_pc_os
            computer.status = new_pc_status
            print(f"PC {old_pc_num} has been updated\n")
        else:
            print(f"\n The number {computer.number} is already registered\n")

    def check_pc(pc_num):  #Checking whether Pc number is unique
        flag = 1
        for computer in PC.all_pc:
            if computer.number == pc_num:
                flag = 0
                break
        if flag == 0:
            return computer
        else:
            return 0

    def show_all_pc():  #Display all computer information
        if len(PC.all_pc) != 0:
            print("All PC details:-\n")
            for computer in PC.all_pc:
                print(f"PC number: {computer.number}")
                print(f"PC Operating System: {computer.os}")
                print(f"PC Status: {computer.status}\n")
        else:
            print("No PC available")

    def search_pc(pc_num):  # Search for PC number
        flag = 0
        for computer in PC.all_pc:
            if computer.number == pc_num:
                flag = 1
                print("Search results:-\n")
                print(f"PC number: {computer.number}")
                print(f"PC operating System: {computer.os}")
                print(f"PC status: {computer.status}")
                pc_exists = computer
                break
        if flag == 1:
            return pc_exists
        else:
            print(f"No PC found with PC number {pc_num}")
            return 0

    def save_file():  #Saves the Data in the Directory
        try:
            file = "ALL_PC.txt"
            with open(file, 'w') as file_obj:
                for computer in PC.all_pc:
                    file_obj.write(f"{computer.number},{computer.os},{computer.status}\n")
            print("\nAll PC information has been saved in the file")

        except Exception as e :
            print("\n File saving error!")

   