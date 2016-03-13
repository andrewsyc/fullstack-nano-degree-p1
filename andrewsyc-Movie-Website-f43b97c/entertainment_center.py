__author__ = 'andrewsyc'
import media
import fresh_tomatoes
import pydoc

"""
Creates instances of listed movies using media.py, creates a static html page using fresh_tomatoes.py
"""

#Listed below are 6 example movies used in making a front end movie trailer site.

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
terminator_genisys = media.Movie("Terminator Genisys",
                                 "A new and better reboot",
                                 "http://cdn-static.denofgeek.com/sites/denofgeek/files/styles/insert_main_wide_image/public/4/39//terminator_genisys.jpg?itok=dFuAGCMC",
                                 "https://www.youtube.com/watch?v=jNU_jrPxs-0")
prometheus = media.Movie("Toy Story",
                         "A story of a boy and his toys",
                         "http://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
                         "https://www.youtube.com/watch?v=sftuxbvGwiU")
the_imitation_game = media.Movie("The Imitation Game",
                                 "Alan Turing biopic",
                                 "http://www.filmmusicnotes.com/wp-content/uploads/2015/01/imitation_game.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")
the_theory_of_everything = media.Movie("The Theory of Everything",
                                       "Stephen Hawkings biopic",
                                       "http://i.space.com/images/i/000/041/533/original/poster-spacedotcom-theory-of-everything.jpeg?1408654495",
                                       "https://www.youtube.com/watch?v=OUpl0HDGq1Q")
million_dollar_baby = media.Movie("Million Dollar Baby",
                                  "Boxing Movie",
                                  "http://image.toutlecine.com/photos/m/i/l/million-dollar-baby-2004-12-g.jpg",
                                  "https://www.youtube.com/watch?v=IH7gQqpw7ok")

#Filling an array full of movie instance argumentes to be formated and displayed using the fresh_tomatoes.py given the open_movies_page an argument.
movies = [toy_story,
          terminator_genisys,
          prometheus,
          the_imitation_game,
          the_theory_of_everything,
          million_dollar_baby]

#Renders a static html page for beautiful viewing in the browser.
fresh_tomatoes.open_movies_page(movies)

