# Python View Bot

## Step1

```bash
$ pip install -r requirements.txt
```

## Step2

Let’s hash a new password so that random access to the port by outside agents is prevented.

```bash
tor --hash-password <enter your password here>
```

## Step3

Configure TOR
Go to the TOR configuration file (torrc) and make necessary changes.
Where the torrc file is placed depends on the operating system you use and where you are receiving tor from. Mine was at ./etc/tor/torrc

-   Enable the “ControlPort” listener for TOR to listen on port 9051, as this is the port to which TOR will listen for any communication from applications talking to the Tor controller.
-   Update the hashed password
-   Implement cookie authentication

```bash
SOCKSPort 9050
HashedControlPassword <your hashed passsword obtained earlier here>
CookieAuthentication 1
```

## Step4

Save and exit and restart TOR.

```bash
$ sudo /etc/init.d/tor restart
```

## Step5

Now run the python file to start the program

```bash
$ python yt.py
```

Enter your password which you used to hash in step 2
Enter the site you want to view <please enter a url only>
Enter the number of views
