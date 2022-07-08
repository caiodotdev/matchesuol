<p align="center">
  <a href="http://caiomarinho.herokuapp.com/">
    <img src="https://i.imgur.com/36ijmZl.png" alt="logo" />
  </a>
</p>

# Get Matchs from Uol Jogos Scrapper.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Maintenance](https://img.shields.io/badge/Django-v3.1.7-%3CCOLOR%3E)](https://img.shields.io/badge/Django-v3.1.7-%3CCOLOR%3E)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Website http://caiomarinho.herokuapp.com/](https://img.shields.io/website.svg?down_color=red&down_message=down&up_color=green&up_message=up&url=http%3A%2F%2Fcaiomarinho.herokuapp.com)](http://shields.io/)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)

[![PyPi version](https://badgen.net/pypi/v/pip/)](https://pypi.com/project/pip)
[![GitHub latest commit](https://badgen.net/github/last-commit/caiomarinhodev/caiomarinhome)](https://GitHub.com/caiomarinhodev/caiomarinhome/commit/)


### 📝 Description
---

The objective of this project is to extract the soccer matches of the day from the URI: "https://www.uol.com.br/esporte/futebol/central-de-jogos/",

and reply with TelegramBot a message containing all the matches of the day.

Template is written with django framework.


### 🚀 Status Project
---
<h4> 
🚀 Matches Bot Finished 🚀
</h4>

### 💻 Features
---

- [x] Login/Logout
- [x] WebScrapper to Uol Site
- [x] Telegram Bot Father Build
- [x] Telegram send message
- [x] Redis Stack
- [x] Celery Tasks Automation
- [x] Admin Page Control

### ⚡Tech Stack
---

The following tools were used in building the project:

- [Django](https://www.djangoproject.com/)
- [Redis](https://redis.io/)
- [Celery](https://github.com/celery/celery)
- [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [SeleniumIDE](https://www.selenium.dev/selenium-ide/)
- [Bootstrap](https://getbootstrap.com/)
- [Amazon S3 CDN](https://aws.amazon.com/)
- [Heroku](https://www.heroku.com/)

### Author
---

<a href="#">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/7137962?v=4" width="100px;" alt=""/></a>
 <br />
 <sub><b>Caio Marinho</b></sub></a> <a href="#" title="Caio Marinho">🚀

Made with ❤️ by Caio Marinho 👋🏽 Get in touch!

[![Linkedin Badge](https://img.shields.io/badge/-Caio%20Marinho-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/caiomarinho/)](https://www.linkedin.com/in/caiomarinho/) 
[![Gmail Badge](https://img.shields.io/badge/-caiomarinho8@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:caiomarinho8@gmail.com)](mailto:caiomarinho8@gmail.com)


### Application Demo
---
<p align="center">
  <kbd>
    <img style="border-radius: 5px" src="https://i.imgur.com/KnL2kC9.gif" alt="Intro">
  </kbd>
</p>


### Getting Started
---

Fi
rst clone the repository from Github and switch to the new directory:
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
