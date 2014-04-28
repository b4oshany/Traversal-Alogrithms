import Tkinter

class Forest:
    roots = []            # list of nodes that have no tree parent
    children = {}         # node :--> list of tree children
    bounds = {}           # lower and upper leaf indexes for each node
    depths = {}           # depth of each node

    def __init__(self, roots, children):
        self.roots = roots
        self.children = children
        self.computeAllLeafIndexes()

    def getNodes(self):
        """Return a list of all nodes in the tree"""
        ls = self.roots[:]
        for x in self.children:
            if x not in ls:
                ls.append(x)
        return ls

    def getChildren(self, node):
        """Return the children of node as a list"""
        if node in self.children.keys():
            return self.children[node]
        return []            

    def isLeaf(self, node):
        """Return True if the node is a leaf."""
        return node not in self.children

    def getDepth(self, node):
        """Return the depth of the given node."""
        return self.depths[node]
        #if not self.isLeaf(node):
        #    return 0
        #else:
        #    return 1 + getDepth(self.children.index(node))

    def getMaxDepth(self):
        """Return the depth of the deepest tree"""
        return self.maxDepth
        #maxDepth = 0
        #for x in self.getNodes():
        #    curDepth = self.getDepth(x)
        #    if curDepth > maxDepth:
        #        maxDepth = curDepth
        #return maxDepth
            
        

    def computeAllLeafIndexes(self):
        """Determine the lower and upper leaf indexes for each subtree in
        each tree of this forest"""
        index = 0
        self.depths = {}
        self.bounds = {}
        self.maxDepth = 0
        for r in self.roots:
            index = self._computeTreeBounds(r, index, 0)
            index += 1
        self.width = index

    def _computeTreeBounds(self, root, start, depth):
        """Given the depth and lowest indexed leaf of a node,
        determine and store the maximum leaf index, and the maximum
        depth of the subtree rooted at it.  Return the index of its rightmost
        leaf.
        """
        self.maxDepth = depth
        if root not in self.depths.keys():
            self.depths[root] = depth         
        children = self.getChildren(root)  
        end = start 
        for i in children:
            end += 1
            self._computeTreeBounds(i, start, depth+1)        
        if root not in self.bounds.keys():
            self.bounds[root] = (start, end)
        return end        
             

    def getPositions(self, leafSpacing, levelSpacing, ox=0, oy=0):
        """Compute the coordinates of each node based on the bounds of
        each node, its level in the tree, and the given spacings.  All
        coordinates will be offset by (ox, oy) (added as a
        displacement).  Return the set of coordinates as a dictionary
        mapping nodes to coordinates.

        This will generate a tree that grows downwards (deeper levels in the
        tree have larger y coordinates).
        """
        positions = {}
        for i in self.getNodes():
            x = (self.bounds[i][1] - self.bounds[i][0]) * leafSpacing + ox
            y = (self.depths[i] * levelSpacing) + oy  
            positions[i] = (x, y)
        #print positions
        #print self.width
        #print levelSpacing
        #print leafSpacing
        #print ox
        #print oy
        return positions

    def draw(self, nodeSize, leafSpacing, levelSpacing):
        """Render an image of the tree with the given sizing dimensions
        """
        # make a window big enough to hold the tree + margins
        window = Tkinter.Tk()
        canvas = Tkinter.Canvas(window,
                                width=leafSpacing * (self.width + 2),
                                height = levelSpacing * (self.maxDepth + 2))
        canvas.pack()
        positions = self.getPositions(leafSpacing, levelSpacing,
                                      nodeSize+leafSpacing,
                                      levelSpacing)
        for node in self.roots:
            self.drawTree(node, positions, canvas, nodeSize)

    def _drawNode(self, node, positions, canvas, size):
        (x,y) = positions[node]
        r = size/2
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="green")
        text = canvas.create_text(x, y, text=str(node))

    def _drawEdge(self, src, dest, positions, canvas, size):
        (sx, sy) = positions[src]
        (dx, dy) = positions[dest]
        canvas.create_line(sx, sy, dx, dy, fill = "red")

    def drawTree(self, root, positions, canvas, nodeSize):
        """Draw the tree rooted at root on given canvas at given size.
        positions[node] ==> (x, y) # centre of node
        """
        for child in self.getChildren(root):
            self._drawEdge(root, child, positions, canvas, nodeSize)
            self.drawTree(child, positions, canvas, nodeSize)
        self._drawNode(root, positions, canvas, nodeSize)
