class DoubleLinkedList:
    head = None
    tail = None
class DoubleNode:
    value = None
    nextNode = None
    previousNode = None
#Añade un elemento a la lista
def D_add(L, element):
    NodeA = DoubleNode()
    NodeA.value = element
    NodeA.nextNode = L.head
    if NodeA.nextNode != None:
        NodeA.nextNode.previousNode = NodeA
    else:
        L.tail = NodeA
    L.head = NodeA
#Devuelve la posicion de un elemento pasado por parametros
def D_search(L, element):
    currentnode = L.head
    posicion = 0    
    while currentnode != None:
        if currentnode.value == element:
            return posicion
        posicion = posicion + 1
        currentnode = currentnode.nextNode
    return None

def D_deleteNode(L,node):
    if L.head == node and L.tail == node:
        L.head = None
        L.tail = None
        return node
    if L.head == node:
        L.head = node.nextNode
        node.nextNode = None
        L.head.previousNode = None
        return node
    if L.tail == node:
        L.tail = node.previousNode
        node.previousNode.nextNode = None
        node.previousNode = None
        return node
    previous = node.previousNode
    nextnode = node.nextNode
    previous.nextNode = nextnode
    nextnode.previousNode = previous
    node.previousNode = None
    node.nextNode = None
    return node
