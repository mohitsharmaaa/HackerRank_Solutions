import sys

sys.setrecursionlimit(2000)
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val
class Tree:
    def __init__(self):
        self.root=Node(1)
    def add(self):
        nodes=int(input().strip())
        a=[self.root]
        
        while(len(a)!=0 or nodes!=0):    
            l,r=[int(x) for x in input().strip().split(" ")]
            if a[0] is not None:
                if l==-1:
                    a[0].left=None
                else:
                    a[0].left=Node(l)
                    a.append(a[0].left)
                                       
                if r==-1:
                    a[0].right=None
                else:
                    a[0].right=Node(r)
                    a.append(a[0].right)
            del a[0]
            nodes-=1
    def swap_node(self,node,level):
        if node is None:
            return
        if level==1:
            #print(node.data)
            node.left,node.right=node.right,node.left
        else:

            self.swap_node(node.left,level-1)
            self.swap_node(node.right,level-1)

    def get_root(self):
        return self.root
    def get_height(self,node):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.left)+1,self.get_height(node.right)+1)
    
    def ques(self,height):
        q=int(input())
        for _ in range(q):
            level=int(input())
            t=height//level
            for i in range(1,t+1):
                self.swap_node(self.root,level*i)
            self.print_tree(self.root)
            print()
    def print_tree(self,node):
        if node is not None:
            self.print_tree(node.left)
            print(node.data,end=" ")
            self.print_tree(node.right)
tree=Tree()
tree.add()
tree.ques(tree.get_height(tree.get_root()))
