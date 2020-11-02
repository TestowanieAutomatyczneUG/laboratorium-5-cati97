class Hamming:
    def distance(self, first, second):
        if len(first) == len(second):
            count_diff = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    count_diff += 1
                else:
                    continue
            return count_diff
        else:
            raise ValueError("Strands must have the same length")
