import pdfplumber as pr

class student():

    def __init__(self,name,sorce):
        self.name=name
        self.sorce=sorce

if __name__=="__main__":
    st_list=[]
    pdf = pr.open('D:\\林\\2022年专升本选拔考试成绩++公示.pdf')
    ps = pdf.pages
    for i in range(len(ps)):
        page=ps[i]
        tables=page.extract_tables()
        table=tables[0];
        for j in range(len(table)):
             if table[j][3]=="大学英语" and table[j][5]=="西方经济学" and table[j][7]=="管理学原理":
                 if table[j][4] == "缺考": table[j][4] = "0"
                 if table[j][6] == "缺考": table[j][6] = "0"
                 if table[j][8] == "缺考": table[j][8] = "0"
                 sorce=float(table[j][4])+float(table[j][6])+float(table[j][8])
                 st_list.append(student(table[j][1],sorce))

st_list.sort(key=lambda student:student.sorce,reverse=True)

for i in range(len(st_list)):
    num=i+1
    print(str(num)+" "+st_list[i].name+" "+str(st_list[i].sorce))