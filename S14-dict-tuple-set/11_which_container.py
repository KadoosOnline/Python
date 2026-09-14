'''Which container should I use?

    list  [ ]   ordered, changeable, duplicates allowed
                -> a sequence of things you will add to and loop over
    tuple ( )   ordered, NOT changeable, duplicates allowed
                -> a fixed record, several return values, a dictionary key
    set   { }   NOT ordered, changeable, NO duplicates
                -> membership tests, removing duplicates
    dict  {k:v} keys -> values
                -> when every item has a name / an identifier
'''

def main() -> None:
    scores_list = [20, 18, 20, 15]                 # order matters
    student_record = ('Ali', 'Rezaei', 2005)       # fixed, never changes
    subjects = {'math', 'physics', 'math'}         # duplicates disappear
    student = {'name': 'Ali', 'score': 20}         # named fields

    print(scores_list, student_record, subjects, student)

    print(type(scores_list), type(student_record), type(subjects), type(student))

if __name__ == '__main__':
    main()
