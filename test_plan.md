'''
You are free to do this part of the question using any format as you like
but if you are planning to use a table, the template below might be helpful. 
You can create something similar on https://tableconvert.com/markdown-generator
'''

<add_course>

| Test ID | Test Category | Description                                                  | Input                                                     | Expected Output                                                          | Status |
|---------|---------------|--------------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | Valid course code, course name and credit hours              | "ABC123", "Introduction to the Alphabet", "3"             | Inputs added to course_info.txt                                          | Pass   |
| Test 02 | Positive Case | Invalid course code                                          | "ABC1", "ABC123", "Introduction to the Alphabet", "6"     | Prompts user to enter a new course code, inputs added to course_info.txt | Pass   |
| Test 03 | Negative Case | Course code already exists                                   | "CSC300"                                                  | Prompts user to enter a new code                                         | Pass   |
| Test 04 | Negative Case | Course code already exists, but is not corrected by the user | "CSC300", "CSC300", "CSC300"                              | Continues to prompt user to enter a new code after every input           | Pass   |
| Test 05 | Edge Case     | 40 character course name                                     | "ABC123", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "3" | Inputs added to course_info.txt                                          | Pass   |
| Test 06 | Edge Case     | 0 character course name                                      | "ABC123", ""                                              | Warning message and prompt user to enter a new name                      | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
N/A


<add_student>

| Test ID | Test Category | Description                                                           | Input                                                                                    | Expected Output                                                                  | Status |
|---------|---------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | Valid student ID, name, program code and course information           | "1234567890", "Jeslyn Bowman", "CS123", "2", "CSC300", "80", "ITS230", "80"              | Inputs added to student_info.txt                                                 | Pass   |
| Test 02 | Positive Case | Valid student ID that exists                                          | "2067564342", "1234567890", "Jeslyn Bowman", "CS123", "2", "CSC300", "80", "ITS230", "80 | Prompts user to enter a new student ID then inputs are added to student_info.txt | Pass   |
| Test 03 | Negative Case | Invalid student ID                                                    | "1"                                                                                      | Sends a warning and prompts user to enter a new student ID                       | Pass   |
| Test 04 | Negative Case | Invalid student name                                                  | "1234567890", ""                                                                         | Sends a warning and prompts for another name                                     | Pass   |
| Test 05 | Edge Case     | Everything is valid but a course code is not found in course_info.txt | "1234567890", "Jeslyn Bowman", "CS123", "2", "CSC301"                                    | Sends a warning and prompts for another course code that is in course_info.txt   | Pass   |
| Test 06 | Edge Case     | Everything valid but a grade                                          | "1234567890", "Jeslyn Bowman", "CS123", "2", "CSC300", "101"                             | Warning message and prompt user to enter another grade                           | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
N/A


<add_teacher>

| Test ID | Test Category | Description                                      | Input                                          | Expected Output                                                                                            | Status |
|---------|---------------|--------------------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | Everything is valid                              | "1234567", "John Smith", "1", "CSC300"         | Inputs are written into the teacher_info.txt                                                               | Pass   |
| Test 02 | Positive Case | Staff ID that already exists in teacher_info.txt | "1089786"                                      | Informs the user that the Staff ID already and exists and prompts for a new one                            | Pass   |
| Test 03 | Negative Case | Invalid Staff ID                                 | "123"                                          | Informs the user that the Staff ID is not the correct length and prompts the user to input a new one       | Pass   |
| Test 04 | Negative Case | Invalid teacher name                             | "1234567", ""                                  | Informs the user that the teacher name is not the correct length and prompts the user to input a new one   | Pass   |
| Test 05 | Edge Case     | Course code does not exist in course_info.txt    | "1234567", "Jane Doe", "1", "CSC100"           | Informs the user that the course code is not in the database and prompts the user to enter a different one | Pass   |
| Test 06 | Edge Case     | Duplicate course code                            | "1234567", "Jane Doe", "2", "CSC300", "CSC300" | Informs the user that the course code has already been entered and prompts for a different one             | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
N/A

<list_students>

| Test ID | Test Category | Description                                                           | Input | Expected Output                                      | Status |
|---------|---------------|-----------------------------------------------------------------------|-------|------------------------------------------------------|--------|
| Test 01 | Positive Case | The text files /home/course_info.txt and /home/student_info.txt exist | N/A   | Prints the data from the files in the correct format | Pass   |
| Test 02 | Positive Case | All file contain 1 or more student or course                          | N/A   | Prints the data from the files in the correct format | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
There are no Negative or Edge cases for this function since there is no
specification on how to handle the error if the files used are not found.
For the Positive cases, I assumed that the files would be found and that
through my testing, the output is consistent with the requirements.


<list_teachers>

| Test ID | Test Category | Description                                                           | Input | Expected Output                                      | Status |
|---------|---------------|-----------------------------------------------------------------------|-------|------------------------------------------------------|--------|
| Test 01 | Postive Case  | The text files /home/course_info.txt and /home/teacher_info.txt exist | N/A   | Prints the data from the files in the correct format | Pass   |
| Test 02 | Positive Case | All files contain 1 or more teacher or course                         | N/A   | Prints the data from the files in the correct format | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
This is the same as the <list_students> function.
There are no Negative or Edge cases for this function since there is no
specification on how to handle the error if the files used are not found.
For the Positive cases, I assumed that the files would be found and that
through my testing, the output is consistent with the requirements.


<search_student>

| Test ID | Test Category | Description                                                       | Input               | Expected Output                                                                    | Status |
|---------|---------------|-------------------------------------------------------------------|---------------------|------------------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | Correctly finding the information when searched by student ID     | "1", "2067564342"   | The information of the student is printed correctly                                | Pass   |
| Test 02 | Positive Case | Correctly finding the information when searched by student's name | "2", "Albert Smith" | The information of the student is printed correctly                                | Pass   |
| Test 03 | Negative Case | Invalid student ID is entered                                     | "1", "1234567890"   | The warning message is given and the user is prompted to give another student ID   | Pass   |
| Test 04 | Negative Case | Invalid student name is entered                                   | "1", "Jane Doe"     | The warning message is given and the user is prompted to give another student name | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
There are no Edge cases for this function since the student ID and the name
rely on the <add_student> function which has Edge cases.


<list_teachers_courses>

| Test ID | Test Category | Description                               | Input        | Expected Output                                                                     | Status |
|---------|---------------|-------------------------------------------|--------------|-------------------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | Valid student ID                          | "2067564342" | The information of the student and the teacher is printed in the correct format     | Pass   |
| Test 02 | Positive Case | Valid student ID but no specified teacher | "1234567890" | The information of the student and the teacher is printed in the correct format     | Pass   |
| Test 03 | Negative Case | Invalid student ID                        | "0987654321" | The warning message is printed and the user is prompted to enter another student ID | Pass   |
| Test 04 | Negative Case | Invalid student ID                        | "abc"        | The warning message is printed and the user is prompted to enter another student ID | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
There are no Edge cases for this function since the student ID and the name
rely on the <add_student> function which has Edge cases. Information on the 
teachers and courses are dependant on the <add_course>, <add_student> and
<add_teacher> functions. 

<course_gpa>

| Test ID | Test Category | Description                                                          | Input    | Expected Output                                                            | Status |
|---------|---------------|----------------------------------------------------------------------|----------|----------------------------------------------------------------------------|--------|
| Test 01 | Positive Case | A valid course code is given and all students have the same score    | "CSC300" | The gpa is calculated and printed                                          | Pass   |
| Test 02 | Positive Case | A valid course code is given and all students have a different score | "CSC300" | The gpa is calculated and printed                                          | Pass   |
| Test 03 | Negative Case | Invalid course code                                                  | "MAT998" | Warning message is given and user is prompted to enter another course code | Pass   |
| Test 04 | Negative Case | Invalid course code with incorrect formatting                        | "MA 998" | Warning message is given and user is prompted to enter another course code | Pass   |
| Test 05 | Edge Case     | All students have a score of 0                                       | "CSC300" | The gpa is calculated and printed                                          | Pass   |
| Test 06 | Edge Case     | A student has an non float value for the score                       | "CSC300" | The warning is given                                                       | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
N/A


<student_gpa>

| Test ID | Test Category | Description                                       | Input                                                                                 | Expected Output               | Status |
|---------|---------------|---------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------|--------|
| Test 01 | Positive Case | A student that has taken 2 courses                | "2067564342", "Albert Smith", "CS123", "2", "ITS230", "80", "CSC300", "65"            | The GPA calculated is 3.50    | Pass   |
| Test 02 | Positive Case | A student that has taken 3 courses                | "1234567890", "Jane Doe", "CS123", "3", "CSC300, "80", "ITS230", "65", "ABC123", "30" | The GPA is calculated as 2.33 | Pass   |
| Test 05 | Edge Case     | A student that scores the maximum possible points | "1234567890", "Jane Doe", "CS123", "3", "CSC300, "100", "ITS230", "100"               | The GPA is calculated as 4.00 | Pass   |
| Test 06 | Edge Case     | A student that scores the minimum possible points | "1234567890", "Jane Doe", "CS123", "3", "CSC300, "0", "ITS230", "0"                   | The GPA is calculated as 0.00 | Pass   |

Why a Positive/Negative/Edge case for this function can not be tested? (if applicable)
There are no Negative cases for this function since the scores rely on the
<add_student> function which handels the error for an invalid score.
