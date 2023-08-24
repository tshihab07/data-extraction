import re, csv
from collections import Counter

class FindDetails:
    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.names = re.compile(r"'([^']*)'")       # grab string that lies between single quotations
        self.phones = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
        
    

    def extract_names(self):
        names = Counter(self.names.findall(self.paragraph))     # avoid duplicate values and return counter objects
        return list(names)


    def extract_phones(self):
        phone_number = self.phones.findall(self.paragraph)
        return phone_number




# opening files to extract names and numbers
with open("dataSheet.txt", "r") as file:
    content = file.read()



fd = FindDetails(content)
name_list = fd.extract_names()
number_list = fd.extract_phones()


# saving contact into .txt file
with open('contactList.txt', 'a+') as file:
    file.write("--"*20 + "\n")
    file.write("XYZ pvt. ltd Employee Data".center(40) + "\n")
    file.write("--"*20 + "\n")
    file.write("Names\t\t\t Phones\n")
    file.write("--"*20 + "\n")

    for nm, ph in zip(name_list, number_list):
        file.write(nm.ljust(22) + ph + "\n")



# saving contact into .csv file
with open("contactList.csv", "a+") as file:
    file.write("--"*20 + "\n")
    file.write("XYZ pvt. ltd Employee Data".center(40) + "\n")
    file.write("--"*20 + "\n")

    col_header = ["Names", "Phones"]
    write_data = csv.DictWriter(file, col_header)
    write_data.writeheader()

    for nm, ph in zip(name_list, number_list):
        write_data.writerow({"Names": nm, "Phones": ph})



# print to the console
print("--"*20)
print("XYZ pvt. ltd Employee Data".center(40))
print("--"*20)
print("Names\t\t\tPhones")
print("--"*20)
for nm, ph in zip(name_list, number_list):
    print(nm.ljust(22)+ ph)


print()
