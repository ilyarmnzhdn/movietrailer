import media
import fresh_tomatoes.py

# Creating film(object) John Wick.
john_wick = media.Movie("John Wick: Chapter 2", "After returning to the crimin"
                        "al underworld to repay a debt, John Wick discovers th"
                        "at a large bounty has been put on his life.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=nMqETeQrgqU")

# Creating film(object) Logan.
logan = media.Movie("Logan", "In the near future, a weary Logan cares for an a"
                    "iling Professor X in a hide out on the Mexican border. Bu"
                    "t Logan's attempts to hide from the world and his legacy"
                    " are up-ended when a young mutant arrives, being pursued"
                    " by dark forces.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI1MjkzMjczMV5BMl5BanBnXkFtZTgwNDk4NjYyMTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=bKIXd3lAFEI")

# Creating film(object) Guardians of the Galaxy.
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy", "Set to the b"
                                      "ackdrop of Awesome Mixtape #2, 'Guardia"
                                      "ns of the Galaxy Vol. 2' continues the "
                                      "team's adventures as they unravel the m"
                                      "ystery of Peter Quill's true parentage."
                                      "",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2MjY2NDc0M15BMl5BanBnXkFtZTgwNzQ5MzczMTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                      "https://www.youtube.com/watch?v=dW1BIid8Osg")

# Creating array of the movies.
movies = [john_wick, logan, guardians_of_the_galaxy]

# Sending array of the movies to fresh_tomatoes for converting it to HTML.
fresh_tomatoes.open_movies_page(movies)
