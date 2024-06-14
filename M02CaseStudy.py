#Ian Duncan
#M02CaseStudy
#Take in student's names and GPA and sort them into the Dean's list or Honor roll
last=input('Enter a last name: ')
while (last != 'ZZZ'):
    first=input('Enter a first name: ')
    gpa = input('Enter a gpa as a decimal: ')
    if (float(gpa)>=3.5):
        print(first,last, 'has made the Dean\'s list')
    elif (float(gpa)>=3.25):
        print(first,last, 'has made the Honor roll')
    else:
        print(first,last, 'has not made either list')
    last=input('Enter a last name: ')