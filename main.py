import pandas
import os


# Global Variables

data = pandas.read_excel("./bin/data.xlsx")


# Functions

def item_index(column, cell):
    for i in range(0, len(column)):
        if column[i] != cell: i+=1
        else: break
    return i

def inbreeding_check(cow, cow_num):
    return [i for i in data['Cattle'] if i != data['Relations'][cow_num] and i != cow]

def sex_checker(lst, cow, cow_num):
    print(f"{len(lst)} {lst}")
    cow_sex = data['Sex'][cow_num]
    [lst.remove(i) for i in lst if data['Sex'][item_index(data['Cattle'], i)] == cow_sex]
    print(f"{len(lst)} {lst}")
    return lst
    

def breeding_check(cow):
    cow_num = item_index(data['Cattle'], cow)
    can_breed_with = sex_checker(inbreeding_check(cow, cow_num), cow, cow_num)
    print(f"{cow.title()} may not breed with {data['Relations'][cow_num].title()}, but may", end=" ")
    return sorted(can_breed_with)


if __name__ == "__main__":
    os.system("clear")  # Unix/*nix systems only
    print("Breeding Checker: Version 0.0.1a\n" + "-"*31)
    cow_to_check = input("Please enter a cow to check: ").lower()
    if [i == cow_to_check for i in data['Cattle'] if cow_to_check == i]:
        cow_list = breeding_check(cow_to_check)
        for_index = len(cow_list[-1])*-1
        breed_with = ", ".join(cow_list).title()
        print(f"breed with {breed_with[:for_index]}and {breed_with[for_index:]}.")
    else:
        print(f"You do not own the cow '{cow_to_check}'")
    