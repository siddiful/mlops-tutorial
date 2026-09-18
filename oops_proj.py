class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input('''Welcome to Chatbook !! How would you like to proceed
                        1. Press 1 to sign up
                        2. Press 2 to sign in
                        3. Press 3 to write a post
                        4. Press 4 to msg a friend
                        5. Press any other key to exit
                        
                        ''')
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.mypost()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email = input('Enter email: ')
        pwd = input('Enter pwd: ')
        self.username = email
        self.password = pwd
        print('You have signed up successfully \n')
        self.menu()
    
    def signin(self):
        if self.username=='' and self.password=='':
            print('Please signup first by pressing 1 in main menu')
        else:
            uname = input('Enter username: ')
            pwd = input('Enter pwd: ')
            if uname == self.username and pwd == self.password:
                print('You have signed in successfully')
                self.loggedin = True
            else:
                print('Please enter correct credentials')
        print('\n')
        self.menu()

    def mypost(self):
        if self.loggedin==True:
            txt = input('Enter your post here: ')
            print(f'Your post is now live: {txt}')
        else:
            print('Please sign in first to post anything !!')
        
        print('\n')
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt = input('Enter your msg here: ')
            frnd = input('Whom to send this msg: ')
            print(f'Your msg has been sent to {frnd}')
        else:
            print('Please sign in first to post anything !!')
        
        print('\n')
        self.menu()


#user1 = chatbook()