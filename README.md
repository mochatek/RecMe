# RecMe

__Recommend Me__ :  A Django-built web-app which recommends movies based on contest-based-recommender strategy.

View the live demo: [RecMe](https://rekme.herokuapp.com/)

## Working
- User registers and login to the application.
- User views a list or movies (Malayalam & Tamil).
- User rates the watched movies on a scale of 10.
- Application will create a user-profile for every user based on their watch history and corresponding ratings.
- Application uses __Content-Based-Recommender__ strategy to find movies, which the user may like from the list of movies, the user hasn't watched.
- Application will recommend those movies, along with an expected rating.
- Application will then filter the recommended movies on an expected rating threshold (eg: 7.5), and lists them in descending order of expected ratings.

### Attributes used to build User-Profile

`language` , `genre` , `rating`

## Data Source

Dataset was built by scraping [Wikipedia](https://en.wikipedia.org)

__URL:__ `https://en.wikipedia.org/wiki/List_of_[lang]_films_of_[year]`

__Scraper Script__: [Wiki-Movie-Scraper](https://github.com/mochatek/RecMe/blob/master/wiki_movie_scraper.py)

## Content-Based-Recommender Strategy

If you need to know how this strategy work, I have made a graphical representation of it with an example. View it [here](https://github.com/mochatek/RecMe/blob/master/cbr.png)

If you want to use the same approach for your recommendation engine __but with ease__, I have made this python library: [cbrecommender](https://github.com/mochatek/cbrecommender)

## Installation

Download and Install [Python](https://www.python.org/downloads/)

Use the package manager [pip](https://pip.pypa.io/en/stable/reference/pip_download/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## How to Run

To start our application, run the command:

```
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/mochatek/RecMe/blob/master/LICENSE)
