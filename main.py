print("To do list program")
inp = int(input("Enter 1 for add a something to list, 2 for delete something and 3 for exit. "))

f = open("t.txt", "a+")

if inp == 1:
    append_som = input("Enter: ")
    f.seek(0)
    lines = f.readlines()
    next_num = len(lines) + 1
    f.write(f"{next_num}. {append_som}\n")
    print(f"Added: {next_num}. {append_som}")

elif inp == 2:
    f.seek(0)
    lines = f.readlines()
    z = int(input("enter the line number: "))
    if 1 <= z <= len(lines):
        del lines[z - 1]
        f.close()
        f = open("t.txt", "w")
        f.writelines(lines)
        print("Deleted successfully!")
    else:
        print("Invalid line number!")

else:
    exit()

f.close()