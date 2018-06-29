class Gene:
    def __init__(self, position, sequence):
        self.position = position
        self.sequence = sequence

class Filter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class GeneFilter:
    def __init__(self, filters, genome):
        self.filters = filters
        self.genome = genome

    def position_filter(self):
        g = 1
        f = 1
        filtered = []
        while True:
            if (g - 1) >= len(self.genome) or (f - 1) >= len(self.filters):
                break

            filt = self.filters[f - 1]
            gene = self.genome[g - 1]

            # gene within current filter boundary
            if gene.position >= filt.start and gene.position < filt.end:
                filtered.append(gene)
                g = g+1

            # gene past current filter boundary
            if gene.position >= filt.end:
                f = f+1

            # gene before current filter boundary
            if g < len(self.genome) and gene.position < filt.start:
                g = g+1

        return filtered


def main():
    test_case_1()

def test_case_1():
    filters = [
        Filter(6, 7),
        Filter(15, 20)
    ]

    genome = [
        Gene(5,"G"),
        Gene(6,"A"),
        Gene(7,"T"),
        Gene(15,"G"),
        Gene(19,"T"),
        Gene(20,"C"),
        Gene(22,"T")
    ]

    genefiltered = GeneFilter(filters, genome)
    filtered = genefiltered.position_filter()

    expected = [
        Gene(6,"A"),
        Gene(15,"G"),
        Gene(19,"T"),
    ]

    assert filtered == expected

if __name__ == "__main__":
    main()
