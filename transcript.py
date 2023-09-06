class Transcript:
    class CourseNode:
        def __init__(self, course_name, year, prereqs, next):
            self.course_name = course_name
            self.year = year
            self.prereqs = prereqs
            self.next = next

    def __init__(self):
        self.head = None

    def add(self, course_name, year, prereqs):
        # Implement this
        return

    def __num_courses_in_year(self, node, year):
        # Implement this
        return

    def num_courses_in_year(self, year):
        return self.__num_courses_in_year(self.head, year)

    def check_prereqs(self):
        # Implement this
        return

    def get_transcript(self):
        # Implement this
        return

    def to_string(self):
        trav = self.head
        s = ''

        if trav is not None:
            s += '(' + trav.course_name + ')'
            trav = trav.next

        while trav is not None:
            s += '-->(' + trav.course_name + ')'
            trav = trav.next

        return s
