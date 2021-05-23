import csv
def write_into_csv_file(info_list):
    with open('StudentInfo.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
           
            writer.writerow(["First Name","Last Name","Gender","DoB","Contact Number","E-Mail ID"])

        writer.writerow(info_list)
                            
if __name__=='__main__':
    
    entry_check = 'yes'
    student_num = 0
    list1=["yes","Yes","YES"]
    list2=["yes","Yes","YES","no","No","NO"]
    list3=["no","No","NO"]

    while entry_check in list1:

        student_info = input ("\nEnter the student information in  the following format:\n[First Name, Last Name, Gender, DoB(DD/MM/YYYY), Contact Number, E-Mail ID]:\n")
        
        student_list=student_info.split(', ')

        print("\nEntered information is - \nFirst Name: {}\nLast Name: {}\nGender: {}\nDoB: {}\nContact Number: {}\nE-Mail ID: {}"
              .format(student_list[0],student_list[1],student_list[2],student_list[3],student_list[4],student_list[5]))

        info_verify= str (input ("\nIs the information entered correct?(yes/no): "))

        if info_verify in list1: 
            student_num += 1

            write_into_csv_file(student_list)

            entry_check = str (input ("\nDo you want to enter the details of another student?(yes/no): "))

            while entry_check not in list2:
                print ("Invalid entry, try again")
                entry_check = str (input ("\nDo you want to enter the details of another student? (yes/no): "))

        elif info_verify in list3:
            print("\nPlease re-enter the correct values!")


            
                                
                    

