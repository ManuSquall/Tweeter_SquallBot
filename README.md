# Tweeter SquallBot

This is Python bot script which connect to  twitter API with [Tweepy library](https://www.tweepy.org/) to perfom some actions. Actually it notify me by direct message about a list of account who unfollow me since the last check. I hosted on Azure like a webjob and define a CRON expression to schedule it.

### Prerequisites

Things you need to install:

```
- [Python 3](https://www.python.org/download/releases/3.0/) (i used 3.8.5 version)
- [Tweepy library](https://www.tweepy.org/) (a module to install with pip)
```

## Getting Started

First make sure you have a twitter account and a twitter dev account for tokens things to access the API, [click for a good article about it 🙂](https://medium.com/analytics-vidhya/accessing-the-twitter-api-with-tweepy-8421329afc5c).

After just download the repo. To make it work actually you will have to replace all string occurences of "manusquall" by your twitter name (this one with "@"). It's different from your screen name and is unique.

A "python .\squallbot.py" command should finally run it (in PowerShell if you are on windows) in the project directory.


### Illustrations
![output](/doc/Image1.png)
![hosting](/doc/Image2.png)

## Built With

* [Tweepy](https://www.tweepy.org/) - The library used

## Contributing

No CONTRIBUTING.md yet but feel free to submit pull requests.
## Authors

* **ManuSquall** - *Initial work* - [PurpleBooth](https://github.com/ManuSquall)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
* https://gist.github.com/PandaWhoCodes/46f58fdead71f4c71453d9ed1e21adf8
* https://kohera.be/tutorials-2/running-python-scripts-on-azure-with-azure-container-instances/
* https://docs.microsoft.com/en-us/azure/app-service/webjobs-create
* https://github.com/PurpleBooth/a-good-readme-template


