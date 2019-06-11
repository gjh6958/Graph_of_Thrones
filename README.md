Graph_of_Thrones
Description
We'll focus in this challenge on what's called a complete graph, wherein every node is expressly connected to every other node. We'll also work assuming an undirected graph, that relationships are reciprocal.
In social network analysis, you can analyze for structural balance - a configuration wherein you'll find local stability. The easy one is when everyone enjoys a positive relationship with everyone else - they're all friends. Another structurally balanced scenario is when you have - in a graph of three nodes - two friends and each with a shared enemy, so one positive relationship and two negative ones.
With larger graphs, you can continue this analysis by analyzing every three node subgraph and ensuring it has those properties - all positive or one positive and two negative relationsgips.
A structurally balanced graph doesn't indicate complete future stability, just local stability - remember, factions can arise in these networks, akin to the Axis and Allies scenario of WW1 and WW2.
Today's challenge is to take a graph and identify if the graph is structurally balanced. This has great applicability to social network analysis, and can easily be applied to stuff like fictional universes like the Game of Thrones and the real world based on news events.
Example Input
You'll be given a graph in the following format: the first line contains two integers, N and M, telling you how many nodes and edges to load, respectively. The next M lines tell you relationships, positive (friendly, denoted by ++) or negative (foes, denoted by --). Example (from a subset of the Legion of Doom and Justice League):
6 15
Superman ++ Green Lantern
Superman ++ Wonder Woman
Superman -- Sinestro
Superman -- Cheetah
Superman -- Lex Luthor
Green Lantern ++ Wonder Woman
Green Lantern -- Sinestro
Green Lantern -- Cheetah
Green Lantern -- Lex Luthor
Wonder Woman -- Sinestro
Wonder Woman -- Cheetah
Wonder Woman -- Lex Luthor
Sinestro ++ Cheetah
Sinestro ++ Lex Luthor
Cheetah ++ Lex Luthor
Example Output
Your program should emit if the graph is structurally balanced or not. Example:
balanced
