import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=CxwTLktovTU&ab_channel=DisneyPlus")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "The last airbender",
                     "https://m.media-amazon.com/images/I/51vtp5pgmnL._AC_.jpg",
                     "https://www.youtube.com/watch?v=-egQ79OrYCs&ab_channel=hollywoodstreams")

pirates = media.Movie("Pirates of the caribbean",
                      "At World's End",
                      "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQlOw-O1tdmzrkCgS5iezwNZ3-4iaRQKdCpVU1tQW-9yzGqJOk8",
                      "https://www.youtube.com/watch?v=rF6k1bXAVIg&ab_channel=%5B%E2%96%BA%5DLBA-LaBande-Annonce",)

harry_potter = media.Movie("Harry Potter",
                           "The Sorcerer's Stone",
                           "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTYGx6w4wW7xmC8h_UdhyzyxhOV4QZofI0lrgZ7JgMkCyqGG5M_",
                           "https://www.youtube.com/watch?v=VyHV0BRtdxo&ab_channel=RottenTomatoesClassicTrailers")

facebook = media.Movie("The Social Network",
                       "Facebook",
                       "http://www.movienewsletters.net/photos/086829R1.jpg",
                       "https://www.youtube.com/watch?v=lB95KLmpLR4&ab_channel=SonyPicturesEntertainment")

social_dilemma = media.Movie("The social dilemma",
                             "We tweet, we like, and we share",
                             "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSlr2S2rTPojczGtrzbf14XwnH-O9ze4FypnKUT3AGPyTgp2X8t",
                             "https://www.youtube.com/watch?v=uaaC57tcci0&ab_channel=Netflix")

movies = [toy_story, avatar, facebook, social_dilemma, pirates, harry_potter]
fresh_tomatoes.open_movies_page(movies)

#avatar.show_trailer()
#pirates.show_trailer()

