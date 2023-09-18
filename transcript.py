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
        new_node = Transcript.CourseNode(course_name, year, prereqs, None)

        if self.head is None:
            self.head = new_node
            return

        if year < self.head.year:
            new_node.next = self.head
            self.head = new_node

        prev = self.head
        trav = self.head.next
        while trav is not None:
            if year < trav.year:
                prev.next = new_node
                new_node.next = trav
                return

            prev = trav
            trav = trav.next

        # year goes at end of list
        prev.next = new_node

    def __num_courses_in_year(self, node, year):
        if node is None:
            return 0
        if node.year > year:
            return 0
        if node.year == year:
            return 1 + self.__num_courses_in_year(node.next, year)
        return self.__num_courses_in_year(node.next, year)

    def num_courses_in_year(self, year):
        return self.__num_courses_in_year(self.head, year)

    def check_prereqs(self):
        trav1 = self.head
        while trav1 is not None:
            trav2 = self.head
            prereqs_found = 0
            while trav2 is not None:
                if trav1.course_name == trav2.course_name:
                    break
                if trav2.course_name in trav1.prereqs:
                    prereqs_found += 1
                trav2 = trav2.next

            if prereqs_found < len(trav1.prereqs):
                return False

            trav1 = trav1.next

        return True

    def get_transcript(self):
        if self.head is None:
            return ''

        stack = []
        trav = self.head
        s = ''

        while trav is not None:
            stack.append(trav)
            trav = trav.next

        top_year = stack[-1].year
        s += str(top_year) + '\n'
        while len(stack) > 0:
            node = stack.pop()
            if node.year != top_year:
                top_year = node.year
                s += '\n'
                s += str(node.year) + '\n'
            s += node.course_name + '\n'

        return s

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
