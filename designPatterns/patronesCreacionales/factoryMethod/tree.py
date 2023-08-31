import sys, time

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None  #in C/C++ in nullptr
        self.right = None #in C/C++ is nullptr


node = Node(5)
node.left = Node(20)
node.right = Node(35)
node.left.left = Node(45)
node.left.right = Node(60)



    #Recorrido en Anticipo
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)



    #Recorrido en Orden
def inorder(node):
    if node:
        preorder(node.left)
        print(node.data)
        preorder(node.right)
        print(node.data)



    #Recorrido Posterior al Pedido
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


def main():
    time.sleep(3)
    print("\n¿Como deseas recorrer el Arbol Binario?\n")
    tree_option = int(input("\t 1- Para recorrido en Anticipo. 2- Para recorrido en Orden. 3- Para recorrido Posterior al Pedido. 4- Para salir del Programa"))
    
    if tree_option == 1:
        print(preorder(node))
    
    if tree_option == 2:
        print(inorder(node))
    
    if tree_option == 3:
        print(postorder(node))

    if tree_option == 4:
        os.exit()

if __name__ == "__main__":
    main()

