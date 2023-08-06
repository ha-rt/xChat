<style>
H2{color:DarkOrange !important;}
</style>


# <img src="https://i.imgur.com/yJurJW4.png" style="width=100px;">
xChat is ah encrypted terminal chatting app, currently created by one person. It allows for chatting in servers, and has constant updates!

## xChat's firebase is currently down due to security issues, you **MUST** create your own database to use xChat, read below.

# <img src="https://i.imgur.com/AhcwcJm.png" style="width=100px;">

xChat current has a commands, but they arent very easy to find on the app currently! So in the mean time, here are all the commands that are currently inside xChat.

**CHAT COMMANDS**

- [--logout] This command allows you to logout, and log into another or the same account. (THIS COMMAND CAN BE RUN IN THE SERVER SELECTION AREA)
- [--switchserv] This command allows you to switch the server you are currently on.

**SERVER OWNER COMMANDS**
- [--updatepass] This command can be run in the main chat, and allows you to switch the password of your account (YOU MUST BE THE SERVER OWNER TO DO SO)

# <img src="https://i.imgur.com/H7zpGNE.png" style="width=100px;">

If you would like to join some xChat owned servers, or create your own, possibly _password protected_, server for you and your friends it is a simple setup! Just follow the steps below to create a custom xChat server.

- Open up xChat, log in, and hold on the server select menu.
- Type in the desired name of the server you would like to create.
- If it logs you into a server, or asks you for a password navigate back to the server select menu.
- Next, follow the password instructions for setting up your server. (Type "n" if you would like your server to have no password)
- Invite all your friends!

Want to log into a server?

- Open up xChat, log in, and wait on the server select menu.
- Type in your desired server
- Type in a password if applicable
- Chat with friends!

**xChat Owned Servers**
- [public] A public server for everyone on xChat!
- [messages] A global server for both v1, v2, and following versions! For versions above V2, there is no password. For versions below V2, just chat in the normal chatting area!

# <img src="https://i.imgur.com/ALzzw0z.png" style="width=100px;">

Want to have your friends, accounts, and servers outside of the xChat database? Well, you can do that too! xChat wont stop you! But before we start, a few rules must be stated.

- If you edit the main xChat code please provide the update with the xChat team, or contributors so that xChat can improve!
- You are **NOT TO CLAIM YOUR DATABASE IS THE MAIN XCHAT DATABASE**

**Setting up your database**

- To setup your database, go and navigate to <a href="firebase.google.com/">Firebase</a>
- Navigate to your console, and log in with google.
- Add a new project, and call it "xChat-{your-database-name}"
- On your projects dashboard, navigate to build, then Firestore Database
- Create your database, and start it in production mode.
- You've finished setting up your database.

**Linking your database to xChat**

- Download the _LATEST_ xChat source code, and extract it to your desired location.
- Remove the README.md file, and create a new python file named "credentials.py"
- Navigate back to your <a href="firebase.google.com/">Firebase</a> project dashboard.
- On your dashboard, open your project settings. Then navigate to the "Service Accounts" tab.
- Inside the service accounts tab, click on "Generate new private key"
- Download the JSON file to your xChat folder
- Open the JSON file in your favorite text editor and copy its contents.
- Open up the newely created "credentials.py" file, and insert your first bit of text into it "FirebaseCredentials = ", then paste your JSON data.
- Hit enter, then type your last bit of text "ENCRYPTION_KEY = b''".
- Inside the single quotes, paste in your decoded Fernet encryption key. <a href="https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/fernet.html">Learn how to generate a key</a>

**Finishing Up**
- Open the main.py file to ensure your script is working, if it isnt follow the steps again to ensure you did everything correctly.
- If you want to share your database, build xChat. I personally used auto-py-to-exe

_You now have your very own xChat Database_

# <img src="https://i.imgur.com/I74ZtZm.png" style="width=100px;">

Do you want to contribute to xChat? It would be greatly appreicated as I am a solo developer, and I am "new" to python. There are a few rules I have though to make sure everything is great for everyone.

**RULES**
- Be respectful to the code, someone (most likely me), has worked hard on that code so be respectful when working on it and try not to break it
- Be cleanly, use the rest of xChat as reference. Use classes, seperate files, AND <a href="https://en.wikipedia.org/wiki/Don%27t_repeat_yourself">DRY!!!</a>

# Thank you so much for checking out xChat!!
