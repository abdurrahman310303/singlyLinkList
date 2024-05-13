class Music :

    def __init__(self,music) :

        self.music = music
        self.start = None

class CMS :

    def __init__(self) :
        self.head = None

    def addMusicAtStart (self, new_music_item) :
        new_music = Music(new_music_item)

        new_music.start = self.head

        self.head = new_music
    
    def addMusicAtEnd (self,new_music_item) :
        new_music = Music(new_music_item)

        cursor = self.head

        while cursor.start :
            cursor = cursor.start
        cursor.start = new_music
    
    def deleteFromStart (self) :
        if self.head is None :
            return f"The List is empty"
        self.head = self.head.start

    def deleteFromEnd (self) :
        
        if self.head is None :
            return f"The list is empty"
        if self.head.start is None :

            self.head = None

        temp = self.head
        while temp.start.start:  
            temp = temp.start
        temp.start = None 

       

    def showAllMusics(self) :
        cursor = self.head
        while cursor:
            print(cursor.music)
            cursor = cursor.start
        print()

if __name__ =="__main__" :

    musicMangement = CMS()

    # itr = 1
    # while itr <= 100:
    #     print('Iteration:', itr)
    #     print('Enter 1 to add at start')

    #     choice = input("Enter your choice: ")

    #     if choice == '1':
    #         name = input("Enter your name: ")
    #         # Add your logic to add 'name' at the start
    #         print(f"Added '{name}' at the start.")
    #     else:
    #         print("Invalid choice. Please enter '1' to add at start.")

    #     itr += 1


    musicMangement.addMusicAtStart("New Music 1")
    musicMangement.addMusicAtStart("New Music 2")
    musicMangement.addMusicAtStart("New Music 3")
    musicMangement.addMusicAtStart("New Music 4")
    musicMangement.addMusicAtEnd("New Music 5")
    musicMangement.addMusicAtStart("New Music 6")
    musicMangement.addMusicAtStart("New Music 7")
    musicMangement.addMusicAtStart("New Music 8")
    musicMangement.addMusicAtStart("New Music 9")
    musicMangement.addMusicAtEnd("New Music 10")


    musicMangement.deleteFromStart()
    musicMangement.deleteFromEnd()

    musicMangement.showAllMusics()  