class edge:
    def __init__(self, node1, node2, rel):
        self.node1 = node1
        self.node2 = node2
        self.rel = rel
        node1.add_rel(self)
        node2.add_rel(self)

    def get_node1(self):
        return self.node1

    def get_node2(self):
        return self.node2

    def get_rel(self):
        return self.rel

    def __str__(self):
        rela = ''
        if self.rel == False:
            rela = 'Negative'
        else:
            rela = 'Positive'
        return (self.node1.get_name() + " has a " + rela + " relationship with " + self.node2.get_name())


class node:
    def __init__(self, name):
        self.name = name
        self.rels = []

    def add_rel(self, rel):
        self.rels.append(rel)

    def get_rel(self):
        return self.rels

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
