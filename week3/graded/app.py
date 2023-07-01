from jinja2 import Template
import sys 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('data.csv')

studentLayoutFile = open('studentLayout.html', 'r')
studentLayout = studentLayoutFile.read()
studentLayoutFile.close()

courseLayoutFile = open('courseLayout.html', 'r')
courseLayout = courseLayoutFile.read()
courseLayoutFile.close()

wrongFile = open('wrong.html', 'r')
wrongLayout = wrongFile.read()
wrongFile.close()

studentId, courseId = None, None 

flag = True 
if len(sys.argv) < 3 :
    flag = False  
else :
    if sys.argv[1] == '-s' : 
        studentId = sys.argv[2]
    elif sys.argv[1] == '-c' : 
        courseId = sys.argv[2]
    else : 
        flag = False 


def createTemplate(studentId = None, courseId = None, flag = True) :
    if studentId : 
        courses = list(data[data[data.columns[1]]])
        if studentId not in courses :
            studentDetails = data[data[data.columns[0]] == int(studentId)]
            studentDetails.reset_index(inplace = True)
            total = sum(studentDetails[data.columns[2]])
            
            if len(studentDetails) > 0 :

                html_template = Template(studentLayout)
                content = html_template.render(data = studentDetails, total_marks = total)

                html_doc = open('index.html', 'w')
                html_doc.write(content)
                html_doc.close()

            else : 
                flag = False 
        else : 
            flag = False 
        
    elif courseId : 
        courseDetails = data[data[data.columns[1]] == int(courseId)]
        courseDetails.reset_index(inplace = True)
        
        plt.hist(courseDetails[data.columns[2]])
        plt.savefig('plot.png')

        avgMark = courseDetails[data.columns[2]].mean()
        maxMark = courseDetails[data.columns[2]].max()
        
        if len(courseDetails) > 0 :

            html_template = Template(courseLayout)
            content = html_template.render(avgMarks = avgMark, maxMarks = maxMark)

            html_doc = open('index.html', 'w')
            html_doc.write(content)
            html_doc.close()
            
        else : 
            flag = False 

    if (courseId == None and studentId == None) or flag == False : 
        html_template = Template(wrongLayout)
        content = html_template.render()

        html_doc = open('index.html', 'w')
        html_doc.write(content)
        html_doc.close()
        
    # print(content)
    # return content

def main() :
    createTemplate(studentId, courseId, flag)