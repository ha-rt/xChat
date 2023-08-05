# xChat
An encrypted chatting app created in Python using Google Firebase.

## Want to create your own server on xChat??

If you want to create a server for you and your friends to chat on without people inturrupting you?! Follow the steps below to create a server.

1 - Open xChat, and log into your account

2 - Inside the server login screen, type in the desired name of your server. If it logs you into a server, or asks you for a password do the following.

2.5 - If it logged you into a server run "--switchserv", if it asks you for a password just hit enter.

3 - Once you find a server name that is available, you will be greeted with an input. Follow the password input, and boom you have your very own server.

/ WANT TO CHANGE YOUR PASSWORD? \

1 - To change the password of a server you must be logged in as the admin / owner account of the server, and run the command "--updatepass". DO NOT TYPE THE PASSWORD AFTER THE COMMAND, ONLY RUN THE COMMAND

2 - Give the information to the prompt, and boom you changed the password. 

## Want to create your own database on xChat, have privacy between friends??

Here are the steps to creating your own xChat server, and sharing it with friends! I ask that when creating servers, if you create new features please share them with the GitHub repository so we can get new amazing features added to xChat.

1 - Create a new file in the xChat main directory named "credentials.py".

2 - Open the new file, and type "FirebaseCredentials = {}".

3 - Get your Firebase JSON Credentials from Firebase, and open the JSON file.

4 - Paste the JSON data inside the brackets you created in the file.

5 - Create a new file inside the Encryption package named "Configuration.py"

6 - Inside the new file, type "ENCRYPTION_KEY = b''"

7 - Inside the string that you just created, paste in a Fernet viable encryption key (https://pythonistaplanet.com/fernet/)

Great! Now you have your own xChat database. Keep in mind you will have to create new accounts whenever creating new servers. I highly recommend now building your project. I use auto-py-to-exe

For users using created servers: WARNING [THE OWNER OF A DATABASE, AND ANY CONTRIBUTORS ON THEIR FIREBASE PROJECT ARE ABLE TO SEE THE PASSWORDS, AND USERNAMES OF YOUR ACCOUNTS USING THEIR ENCRYPTION KEY]

## How do I contribute?

You can contribute in anyway, just write some code and create a request. When contributing there are only 2 rules.

1 - You must be respectful to other peoples code, and respect the work they put into it.

2 - You must make your code cleanly, it should be easy to see what is going on inside it. Look at how the packages, and files are configured for how it works.

### Thank you for checking out xChat
