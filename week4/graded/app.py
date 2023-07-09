from flask import Flask, render_template, request 
import matplotlib.pyplot as plt
import numpy as np 

def read_data() : 
    f = open('data.csv', 'r')
    data = f.readlines()
    
    cleanData = []
    for row in data : 
        cleanData.append(row[:-1])

    studentDict, courseDict = {}, {}

    for i in range(1, len(cleanData)) : 
        sid, cid, marks = cleanData[i].split(',')
        if int(sid) not in studentDict.keys() : 
            studentDict[int(sid)] = {'courseID' : [int(cid)], 'marks' : [int(marks)]}
        else : 
            studentDict[int(sid)]['courseID'].append(int(cid))
            studentDict[int(sid)]['marks'].append(int(marks))

    for i in range(1, len(cleanData)) : 
        sid, cid, marks = cleanData[i].split(',')
        if int(cid) not in courseDict.keys() : 
            courseDict[int(cid)] = {'studentID' : [int(sid)], 'marks' : [int(marks)]}
        else : 
            courseDict[int(cid)]['studentID'].append(int(sid))
            courseDict[int(cid)]['marks'].append(int(marks))
            
    f.close()
    print(studentDict)
    print(courseDict)

    return studentDict, courseDict 


app = Flask(__name__, template_folder='templates')

@app.route("/", methods = ['POST', 'GET'])
def hello_world() : 
    studentData, courseData = read_data()
    if request.method == 'GET' :
        return render_template('index.html')
    elif request.method == 'POST' : 
        if request.form['ID'] == 'student_id' : 
            try : 
                studentID = int(request.form['id_value'])
                filterData = studentData[studentID]
                print(filterData)

                totalMarks = sum(filterData['marks'])
                return render_template('student.html', data = filterData, studentID = studentID, totalMarks = totalMarks)
            except : 
                return render_template('wrong.html')
        
        elif request.form['ID'] == 'course_id' : 
            try : 
                courseID = int(request.form['id_value'])
                filterData = courseData[courseID]
                print(filterData)

                maxMarks, avgMarks = np.max(filterData['marks']), np.mean(filterData['marks'])
                
                plt.hist(np.array(filterData['marks']))
                plt.xlabel('Marks')
                plt.ylabel('Frequency')
                plt.savefig(f"static/{courseID}.png")
                print('done')
                return render_template('course.html', highestMarks = maxMarks, avgMarks = avgMarks, url = courseID)
            except : 
                return render_template('wrong.html')

        else : 
            return render_template('index.html')
    
    else : 
        return render_template('wrong.html')

if __name__ == '__main__' : 
    app.run()