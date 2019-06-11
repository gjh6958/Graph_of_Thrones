# Main python file for the GOT


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

# Makes the nodes that are given in the input file


def make_nodes(lines):
    character_names = []
    for line in lines:
	raw = ''
	if ' ++ ' in line:
	    raw = line.split(' ++ ')
	else:
	    raw = line.split(' -- ')
	for l in raw:
	    if l not in character_names:
		character_names.append(l)
        nodes = []
        for name in character_names:
            name = node(name)
            nodes.append(name)
    return nodes

# Takes in a name that matches a node name and finds the node


def str_to_node(name, nodes):
    for node in nodes:
        if node.get_name() == name:
            return node

# Creates the edges that connect the nodes that were made, forming the graph connections


def relate_nodes(lines, nodes):
    relationships = []
    for line in lines:
        rel = False
        if ' ++ ' in line:
            rel = True
            line = line.split(' ++ ')
        else:
            line = line.split(' -- ')
        node1 = str_to_node(line[0], nodes)
        node2 = str_to_node(line[1], nodes)
        relationships.append(edge(node1, node2, rel))

#  Finds the nodes that are uncommon between the two given edges


def find_nodes(edge1, edge2):
    raw_nodes = [edge1.get_node1(), edge1.get_node2(), edge2.get_node1(), edge2.get_node2()]
    nodes = []
    for i in raw_nodes:
        if i not in nodes:
            nodes.append(i)
        else:
            nodes.remove(i)
    return nodes

# Finds the connecting edge between two given nodes


def find_edge(edge1, edge2):
    nodes = find_nodes(edge1, edge2)
    rels1 = nodes[0].get_rel()
    rels2 = nodes[1].get_rel()
    for i in rels1:
        for j in rels2:
            if i is j:
                return i

# Algorithm to check if the graph made by the input file is balanced or not


def check_balance(nodes):
    marker1 = 0
    for character in nodes:
        marker1 = 0
        relationships = character.get_rel()
        while marker1 in range(0, len(relationships)-2):
            marker2 = marker1 + 1
            while marker2 in range(marker1+1, len(relationships)-1):
                edges = [relationships[marker1].get_rel(), relationships[marker2].get_rel(),
                         find_edge(relationships[marker1], relationships[marker2]).get_rel()]
                if edges.count(True) == 2:
                    return False
                marker2 += 1
            marker1 += 1
    return True


# Main function that runs the input parsing, graph building, and graph parsing


def main():
    fp = open("ex.in.txt", 'r')
    dims = fp.readline()
    dims = dims[:-1].split(' ')
    nodenum = int(dims[0])
    edgenum = int(dims[1])
    lines = fp.read().splitlines()
    characters = make_nodes(lines)
    relate_nodes(lines, characters)
    if check_balance(characters):
        print("Balanced")
        return
    print("Unbalanced")
    return

main()