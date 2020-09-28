import csv
def write_info_csv(info_csv):
    with open("student_info.csv",'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["name","Age","contact","E-mail ID"])
        writer.writerow(info_csv)
              
condition=True
while(condition):
    student_info=input("Enter information of student in following format:Name Age Contact E-mail: ")
    print("Entered information:"+student_info)
    student_info_list=student_info.split(" ")
    print(student_info_list)
    write_info_csv(student_info_list)
    a=input("enter (yes/No) if you want to enter information of more students : ")
    if(a=="yes"):
        condition=True
    elif(a=="No"):
        condition=False
        
