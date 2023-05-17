from DSAgraph import *
def testFunc():
        g = DSAGraph()
        test1 = g.addVertex(3, "testing")
        test2 = g.addVertex(5, "value")
        test3 = g.addVertex(7, "another value")

        print("Printing current vertices ---")
        myiter = iter(g.vertices)
        for value in myiter:
            print(value)
        print("---")
        g.addEdge(3, 5)
        g.addEdge(5, 7)

        print("Printing test1's links ---")
        for value in iter(test1.linksList):
            print(value)
        print("---\nPrinting edge count of graph ---")
        print(g.getEdgeCount())
        print("---\nPrinting vertice count of graph ---")
        print(g.getVertexCount())
        print("---\nIs adjacent test ---")
        print(g.isAdjacent(test1, test3))
        print(g.isAdjacent(test1, test2))   
        print("---\nPrinting as adjacency list ---")
        g.displayAsList()
        print("---\nPrinting as adjacency matrix ---")
        g.displayAsMatrix()
        print("--- BFS --")
        for item in iter(g.BFS()):
            print(f"{item[0]} to {item[1]}")
        print("-----")
        print(g.getVertex(5))
        g.getAdjacent(100)
    testFunc()