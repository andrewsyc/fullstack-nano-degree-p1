## Synopsis

A python based movie trailer website that lists theatrical movie posters with the movie title below them. Clicking on the movie poster will activate a youtube popup of the movie trailer.

Movie trailer site is responsive and uses bootstrap.

## Code Example

Movie Entry Example:
million_dollar_baby = media.Movie("Million Dollar Baby", "Boxing Movie", "http://image.toutlecine.com/photos/m/i/l/million-dollar-baby-2004-12-g.jpg", "https://www.youtube.com/watch?v=IH7gQqpw7ok")

Array of all movies to be listed:
movies = [toy_story, terminator_genisys, prometheus, the_imitation_game, the_theory_of_everything, million_dollar_baby]

Creating the html page:
fresh_tomatoes.open_movies_page(movies)


## Motivation

Excellent project for learning on. I've web developed with standard html and php, not python though.

## Installation

Running of entertainment_center.py produces a static html page called fresh_tomatoes.py

## API Reference

There are currently no 3rd party functions as of yet.

## Tests

Several instances of media class were made in the entertainment_center.py class, as each one is a movie that is displayed on the site.
Website was tested with several different browser sizes.

## Contributors

Andrew Sychra, inspired from Udacity instructors

## License

The MIT License (MIT)

Copyright (c) <2015> <SRCHUB>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.