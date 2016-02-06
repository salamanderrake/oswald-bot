import socket
import os

server = 'irc.freenode.net'
channel = '#fahlmant'
botnick = 'oswald'
word = os.environ["OSWALD"]
if os.environ.get("TRAVIS"):
    travis = os.environ["TRAVIS"]



def ping():
    ircsock.send("PONG :pong\n")

def sendmsg(chan, msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(newnick): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def quitIRC():
  ircsock.send("QUIT :leaving\n")


def commands(nick,channel,message):
   if message.find('!help')!=-1:
      ircsock.send('PRIVMSG %s :%s: I have no commands right now!\r\n' % (channel,nick))
   elif message.find('!ping') !=-1:
      ircsock.send('PRIVMSG %s :%s: pong\r\n' % (channel,nick))

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + "My Bot\n ")
ircsock.send("NICK "+ botnick + "\n")
ircsock.send("NICKSERV IDENTIFY " + word + "\n" )
joinchan(channel)

while 1:
    ircmesg = ircsock.recv(2048)
    ircmesg = ircmesg.strip('\n\r')
    print(ircmesg)
    if ircmesg.find(' PRIVMSG ')!=-1:
        nick=ircmesg.split('!')[0][1:]
        channel=ircmesg.split(' PRIVMSG ')[-1].split(' :')[0]
        commands(nick,channel,ircmesg)

    if ircmesg.find(":Hello " + botnick) != -1:
        hello(botnick)
    if ircmesg.find("!gtfo") != -1:
        quitIRC()
        exit()
    if ircmesg.find("PING :") != -1:
        ping()
    if(travis is "travis"):
        break
