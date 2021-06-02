# Python View Bot  🤖 <img alt="PyPI" src="https://warehouse-camo.cmh1.psfhosted.org/18509a25dde64f893bd96f21682bd6211c3d4e80/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f64796e61636f6e662e737667">

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

-   Enter your password which you used to hash in step 2
-   Enter the site you want to view $please enter a url only$
-   Enter the number of views





[![https://github.com/Bunty9](https://img.shields.io/badge/Made%20With%20❤️%20By-Bunty9-red)](https://github.com/Bunty9)

