class Node:
    def __init__(self ,data = None):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def _insert_recursive(self , value  , node):
        if value["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(value)
                
            else:
                self._insert_recursive(value, node.right) 
        else:
            return   

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value ,self.root)
        
    
    
    def _search_recursive(self, blog_id, node):
        if node.left == Node and node.right == None: 
            return False
        if blog_id == node.data["id"]:
            return node.data
        
        if blog_id < node.data["id"]:
            if blog_id == node.left.data["id"]: 
                return node.left.data
            return self._search_recursive(blog_id, node.left)

        
        if blog_id > node.data["id"]:
            if blog_id == node.right.data["id"]:
                return node.left.data
            return self._search_recursive(blog_id, node.right)
    
    def search(self , blog_id):
        blog_id = int(blog_id)
        if self.root is None:
            return False
        
        return self._search_recursive(blog_id  ,self.root)  