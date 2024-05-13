class Node:

    def __init__(self,data) :

        self.data = data
        self.next = None

class LinkList :

    def __init__(self) :

        self.head = None

    def insertStart (self, new_data) :
        
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def printList(self) :

        temp = self.head

        while temp :

            print(temp.data)
            temp = temp.next

if __name__=="__main__" :

    ll = LinkList()

    ll.insertStart(1)
    ll.insertStart(2)


    ll.printList()
