class Node :

    def __init__(self,data) :

        self.data = data
        self.next = None

def ReversingSecondHalf(head) :

        prev = None
        current = head

        while current :
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
class LinkList :

    def __init__(self) :
        self.head = None

    def insertAtStart(self,new_data) :
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self,new_data) :
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_data
            return
        last = self.head
        while last.next :
            last = last.next
        last.next = new_node

    def deleteFromStart (self) :
        if self.head is None :
            return f"The list is empty"
        self.head = self.head.next
    
    def deleteFromEnd (self) :
        if self.head is None:
            return f"The list is Empty"
        if self.head.next is None :
            self.head = None
            return
        last = self.head.next
        while last.next :
            last = last.next
        last = None

    def deleteInPosition (self, n) :

        if self.head is None:

            return f"the list is empty"
        
        if self.head and n==1:
            
            current = self.head
            self.head = self.head.next
            
            return current.data

        

        current = self.head

        prev = None
        position = 1

        while current and position < n:

            if position < n:
                prev = current
                current = current.next
                position += 1
        
        prev.next = current.next

        return current.data
    

    def reverse (self) :
        current = self.head
        prev = None

        while current :

            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
    def checkPalindrome(self) :

        if self.head is None or self.head.next is None:
            return True

        slow = fast = self.head

        while fast.next and fast.next.next :

            slow = slow.next
            fast = fast.next.next
        
        second_half = ReversingSecondHalf(slow.next)
        
        p1 = self.head
        p2 = second_half

        while p2:

            if p1.data != p2.data:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
    

    def reverseBetween(self,left,right) :

        if left >= right or self.head is None:
            return

        current = self.head
        prev = None
        position = 1

        while position < left :

            prev = current
            current = current.next
            position +=1
      
        rhead = None
        rtail = current

        while position <= right:

            temp = current.next
            current.next = rhead
            rhead = current
            current = temp
            position += 1

        rtail.next = current

        if prev :

            prev.next = rhead
        
        else:
            self.head = rhead
            
    def leetcode155(self) :
        oddNode = self.head
        eveNode = None

        current = self.head

        postion = 1 

        while current:

            if postion % 2 == 0 :

                eveNode = current
            
            else :

                oddNode = current

            postion +=1
        return oddNode + eveNode
    
    def search (self,value) :
        
        current = self.head
        postition = 1
        while current :

            if current.data == value :
                return f"{current.data} found at position {postition}"
            current = current.next
            postition += 1
        return f"Value not found in the link List"

    def printList(self) :
        temp = self.head
        while temp :
            print(temp.data,end=",")
            temp = temp.next
        print()


if __name__ == "__main__":

    ll = LinkList()

    ll.insertAtStart(1)
    ll.insertAtStart(2)
    ll.insertAtStart(3)
    ll.insertAtStart(4)
    ll.insertAtStart(5)



    # ll.insertAtStart('2')
    # ll.insertAtStart('3')
    # ll.insertAtStart('4')
    # ll.insertAtStart('4')
    # ll.insertAtStart('3')
    # ll.insertAtStart('2')
    # ll.insertAtStart('1')
    # ll.printList() 
    ll.reverse()

    # ll.reverseInPositions(2,4)
    ll.printList()

    print("Deleted : "+ str(ll.deleteInPosition(2)))
    # ll.reverseBetween(3,6)
    ll.printList()



    # print(ll.checkPalindrome())

    # print(ll.leetcode155())
    # ll.reverse()
    # ll.insertAtEnd(0)
    # print(ll.deleteFromStart())
    # print(ll.search(2))

    # ll.printList()