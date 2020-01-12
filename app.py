from flask import Flask, render_template
import csv
from disney_search import disney
from netflix_search import netflix
from crave_search import crave
import os
app = Flask(__name__)

searchResults = {

}
@app.route('/search')
def index():
    return searchResults


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    with open('output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # if line_count == 0:
            # print(row)

            searchResults[row[0]] = row
            searchResults[row[0]].pop(0)
            line_count += 1
            # else:
            #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            #     line_count += 1
        print(f'Processed {line_count} lines.')
    #return 1 #render_template('files/index.html')




def data_search(userinput):
    mydict = {}
    disney_list = disney()
    netflix_list = netflix()
    crave_list = crave()

    print(disney_list)
    print(netflix_list)
    print(crave_list)

    mydict["Disney"] = disney_list
    mydict["Netflix"] = netflix_list
    mydict["Crave"] = crave_list


    if userinput in mydict["Disney"]:
        answerDisney = "The program " + str(userinput) + " is on Disney+"
        print(answerDisney)

    elif userinput in mydict["Disney"] and userinput in mydict["Netflix"] :
        answerDisney = "The program " + str(userinput) + " is on Disney+ and Netflix"
        print(answerDisney)

    elif userinput in mydict["Disney"] and userinput in mydict["Crave"]:
        answerDisney = "The program " + str(userinput) + " is on Disney+ and Crave"
        print(answerDisney)

    elif userinput in mydict["Crave"] and userinput in mydict["Netflix"]:
        answerDisney = "The program " + str(userinput) + " is on Crave and Netflix"
        print(answerDisney)

    elif userinput in mydict["Netflix"]:
        answerNetflix = "The program " + str(userinput) + " is on Netflix"
        print(answerNetflix)

    elif userinput in mydict["Crave"]:
        answerCrave = "The program " + str(userinput) + " is on Crave"
        print(answerCrave)

    elif userinput in mydict["Disney"] and userinput in mydict["Netflix"] and userinput in mydict["Crave"] :
        answerDisney = "The program " + str(userinput) + " is on Disney+ and Netflix and Crave"
        print(answerDisney)

    return True


print(data_search("New Eden"))