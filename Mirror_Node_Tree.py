class Node():
    def __init__(self,val,s):
        self.data=val
        self.right=None
        self.left=None
        if s=="":
            self.string=""
        else:
            self.string=s
class Tree():
    def __init__(self):
        self.root=Node(1,"")

    def find_node(self,pn):
        a=[self.root]

        while(len(a)!=0):
            if a[0].data==pn:
                return a[0]
            if a[0].left is not None:
                a.append(a[0].left)
            if a[0].right is not None:
                a.append(a[0].right)
            del a[0]
    def add_node(self,node,val,side):
        s=node.string
        if side=='L':
           
            node.left=Node(val,s+'L')
        else:
            node.right=Node(val,s+'R')
    def bfs(self):
        a=[self.root]

        while(len(a)!=0):
            if a[0] is not None:
                
                print(str(a[0].data)+"  "+a[0].string)
            if a[0].left is not None:
                a.append(a[0].left)
            if a[0].right is not None:
                a.append(a[0].right)
            del a[0]
            
    def mirror(self,s):
        k=self.root
        if s=="":
            return self.root.data
        for i in s:
            if k is None:
                return -1
            if i=='R':
                k=k.left
            else:
                k=k.right
        if k is None:
            return -1
        else:
            return k.data
          

tree=Tree()

    
n,q=[int(x) for x in input().strip().split(" ")]
for _ in range(n-1):
    pn,val,side=[x for x in input().strip().split(" ")]
    pn=int(pn)
    val=int(val)
    node=tree.find_node(pn)
    #print(node.data)
    tree.add_node(node,val,side)
#tree.bfs()    
for _ in range(q):
    actual_node=int(input())
    node=tree.find_node(actual_node)
    print(tree.mirror(node.string))
    

        
    