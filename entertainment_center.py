'''
We import fresh_tomatoes which was provided to generate our HTML page
We import media where we defined our movie class
'''

import fresh_tomatoes
import media

'''
these classes (defined in the media.py file) contain the information for the
movies that will be displayed on the site, each one contains:

movie title
summary
poster image url
youtube link to a trailer
'''

shining = media.Movie("The Shining",
                      "After taking a job as a lodge caretaker the Torrences \
                      must come together and learn the true meaning of \
                      Christmas as they stay for the winter",
                      "http://40.media.tumblr.com/2a5fb58e48e7ffc36e3afbe50f83d0fe/tumblr_nhzc3uHBcF1tk4n0bo4_1280.jpg",
                      "https://www.youtube.com/watch?v=rt15HCq4htw")

mad_max = media.Movie("Mad Max: Fury Road",
                      "After our zaney hero gets a bad blood transfusion his \
                      vacation to palm spings goes haywire.",
                      "http://cdn3-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/10636937_661847177254140_3001186770164503894_o.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

it_follows = media.Movie("It Follows",
                         "A group of teens have the summer of their lives after\
                         Jay meets the guy of her dreams",
                         "http://www.trriviera.com/it-follows-poster.jpg",
                         "https://www.youtube.com/watch?v=QX38jXwnRAM")

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of friends search the stars for excitement \
                        after one racoon's new desk job leaves him feeling \
                        like this may be his last great road trip",
                        "https://metrouk2.files.wordpress.com/2014/02/ad_127934252.jpg",
                        "https://www.youtube.com/watch?v=B16Bo47KS2g")

weekend_at_bernies = media.Movie("Weekend at Bernies",
                                 "Two friends go to great lengths to hide a \
                                 murder in this tragic tail of bad luck in \
                                 greed based on a true story.",
                                 "https://image.tmdb.org/t/p/original/h3hjMREZEUPtDkZBiYDzLq0THk0.jpg",
                                 "https://www.youtube.com/watch?v=YCTgcZ6ImsQ")

weekend_at_bernies_2 = media.Movie("Weekend at Bernies 2: Reloaded",
                                   "Two families are at each other's throats \
                                   as this follow up to the Oscar winner \
                                   showcases the trial and aftermath of the \
                                   notorious case.",
                                   "https://www.movieposter.com/posters/archive/main/16/A70-8099",
                                   "https://www.youtube.com/watch?v=ZlCADShkhjk")
'''
This lists all the movie objects so they can be called with
fresh_tomatoes.open_movies_page that will then generate our HTML.
'''

movies = [shining, mad_max, it_follows, guardians, weekend_at_bernies, weekend_at_bernies_2]

fresh_tomatoes.open_movies_page(movies)
