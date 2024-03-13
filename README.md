# karma
Fun implementation for discord bots in python. It gives certain words a positive or negative value


## Example

![Karma](karma-example.png)

## Usage

In a discord chat, give props to a word, a name, a piece of software or anything you support or like, for example:

```
pizza++
linux++
```

You can also downvote stuff you don't like

```
ubuntu--
windows--
winter--
```

a text database will be created and points will be added to the words, so, for instance, if the word pizza received 2 upvotes yesterday
and one today, the total count for pizza will be 3 points. If someone downvotes it once, the total count will be two. 


A top 5 (work in progress) can be issued by typing ```!karma```

At the moment it displays everything, but it should only display the top positive 5 entries

Karma for a specific word can be checked out individually by typing !karma <word> ```!karma pizza```


Please check the issues section for more information.

This is meant to be integrated in a discord bot written in python.



