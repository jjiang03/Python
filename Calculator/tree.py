# author: Justin Jiang
# date: March 2, 2023
# file: tree.py a Python program that sets up a expression tree class
from stack import Stack
class BinaryTree:

    def __init__(self,treeObj):
        self.key = treeObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            
            
            self.leftChild = t
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            
            self.rightChild = t
    def getRightChild(self):
   
       return self.rightChild
    
    def getLeftChild(self):
  
        return self.leftChild
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key
    def __str__(self):
        
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree (BinaryTree):
    
    def make_tree(postfix):
        s = Stack()
        
        for i in postfix:
            if i in "()^*/+-":
                #create a new tree
                t = ExpTree(i)
                t.rightChild = s.pop()
                t.leftChild = s.pop()
                s.push(t)
            else:
                s.push(ExpTree(i))
        return s.peek()
    
    def __str__(self):
        return (ExpTree.inorder(self))
    
    def preorder(tree):
        hold = ""
        
        if tree:
            hold += tree.getRootVal()
            hold += ExpTree.preorder(tree.leftChild)
            hold += ExpTree.preorder(tree.rightChild)
        return hold
    
    def postorder(tree):
        hold = ""
        if tree:
            hold += ExpTree.postorder(tree.leftChild)
            hold += ExpTree.postorder(tree.rightChild)
            hold += tree.getRootVal()
        return hold

    def inorder(tree):
        res = ''
        if tree != None:
            if tree.leftChild:
                res += '('
            res += ExpTree.inorder(tree.leftChild)
            res+=(tree.getRootVal())
            res+=ExpTree.inorder(tree.rightChild)
            if tree.rightChild:
                res += ')'
        return res
            
        

    def evaluate(tree):
        #check if tree is a number or not
        if tree.getLeftChild() != None and tree.getRightChild() != None:
            
        #evaluate left and right child
       
            left = (ExpTree.evaluate(tree.getLeftChild()))
            right = (ExpTree.evaluate(tree.getRightChild()))
            #check if tree is an operator
            if tree.getRootVal() in "^*/+-":
                if tree.getRootVal() == "+":
                    return float(left) + float(right)
                elif tree.getRootVal() == "-":
                    return float(left) - float(right)
                elif tree.getRootVal() == "*":
                    return float(left) * float(right)
                elif tree.getRootVal() == "/":
                    return float(left) / float(right)
                elif tree.getRootVal() == "^":
                    return float(left) ** float(right)
        else:
            return tree.getRootVal()
      
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0

    test1 = "2 3 4 + *".split()
    tree1 = ExpTree.make_tree(test1)
    print(ExpTree.inorder(tree1))
    print(ExpTree.preorder(tree1))
    

    