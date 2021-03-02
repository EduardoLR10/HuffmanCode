class Node:
    
    def __init__(self, position, code):

        self.left = None
        self.right = None
        self.position = position
        self.code = code
        self.children = 0

    def insert(self, position, counter):
        self.children = self.children + 1
        if self.left == None:
            if (counter + 1) == position:
                self.left = Node(position, self.code + "0")
                print("oi1 " + str(position) + " " + str(self.children))
            else:
                self.left = Node(-1, self.code + "0")
                print("oi2 " + str(position) + " " + str(self.children))
                self.left.insert(position, counter + 1)
        else:
            if (self.left.position == -1 and self.left.children < position):
                print("oi3 " + str(position) + " " + str(self.children))
                self.left.insert(position, counter + 1)
            else:
                if self.right == None:
                    if (counter + 1) == position:
                        self.right = Node(position, self.code + "1")
                        print("oi4 " + str(position) + " " + str(self.children))
                    else:
                        self.right = Node(-1, self.code + "1")
                        print("oi5 " + str(position) + " " + str(self.children))
                        self.right.insert(position, counter + 1) 
                else:
                    print("oi6 " + str(position) + " " + str(self.children))
                    self.right.insert(position, counter + 1)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.position, self.code),
        if self.right:
            self.right.PrintTree()

    def getLeafCodes(self, codes):
        if self.left:
            self.left.getLeafCodes(codes)
        if self.position != -1 and self.position != 0:
            codes.append(self.code)
        if self.right:
            self.right.getLeafCodes(codes)
        return codes
