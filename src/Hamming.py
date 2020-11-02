class Hamming:
    def distance(self, first, second):
        if first == "" and second == "":
            return 0
        elif first == second:
            return 0
        else:
            return 1
