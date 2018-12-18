import media
import fresh_tomatoes



vertigo = media.Movie("Vertigo",
					  "Detective Scottie who suffers from acrophobia is hired to investigate the strange activities of an old friend's wife. She commits suicide while Scottie becomes dangerously obsessed with her.",
					  "https://goo.gl/AyAqSk",
					  "https://www.youtube.com/watch?v=UHhsEYDg8GI")

the_dark_knight = media.Movie("The Dark Knight",
							  "After Gordon, Dent and Batman begin an assault on Gotham's organised crime, the mobs hire the Joker, a psychopathic criminal mastermind, who wants to bring all the heroes down to his level.",
							  "https://goo.gl/jVKzoY",
							  "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

pay_it_forward = media.Movie("Pay It Forward",
							 "Inspired by a school assignment, young Trevor comes up with an idea that changes many lives. He decides that instead of returning a favour, he will pay it forward by doing good deeds for three people.",
							 "https://goo.gl/Pf4YFL",
							 "https://www.youtube.com/watch?v=qfW0wCV9iFI")

good_will_hunting = media.Movie("Good Will Hunting",
								"Will Hunting, a genius in mathematics, solves all the difficult mathematical problems. When he faces an emotional crisis, he takes help from psychiatrist Dr Sean Maguireto, who helps him recover.",
								"https://goo.gl/fmaqTU",
								"https://www.youtube.com/watch?v=QSMvyuEeIyw")

raman_raghav_2 = media.Movie("Raman Raghav 2.0",
							 "Ramanna, a maniac murderer, finds a soulmate in Raghavan, a policeman, who inspects his murder cases. He tries to make Raghavan realize how they both are similar.",
							 "https://goo.gl/axnwzj",
							 "https://www.youtube.com/watch?v=FWfLKcXuBoY")

arrival = media.Movie("Arrival",
					  "Louise Banks, a linguistics expert, along with her team, must interpret the language of aliens who've come to earth in a mysterious spaceship.",
					  "https://goo.gl/NoPwki",
					  "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

silence_of_the_lambs = media.Movie("The Silence of the Lambs",
								   "Clarice Starling, an FBI agent, seeks help from Hannibal Lecter, a psychopathic serial killer and former psychiatrist, in order to apprehend another serial killer who has been claiming female victims.",
								   "https://goo.gl/w4Li1f",
								   "https://www.youtube.com/watch?v=ZWCAf-xLV2k")

dead_poets_society = media.Movie("Dead Poets Society",
								 "John Keating, a progressive English teacher, encourages his students to break free from the norms, go against the status quo and live unapologetically.",
								 "https://goo.gl/H9DXwQ",
								 "https://www.youtube.com/watch?v=wrBk780aOis")

the_birds = media.Movie("The Birds",
						"Melanie, a rich socialite, follows Mitch, a lawyer, to his home in Bodega Bay to play a practical joke on him. Things take a bizarre turn when the birds in the area begin to attack the people there.",
						"https://goo.gl/v7TLn4",
						"https://www.youtube.com/watch?v=pwyQHPielSg&t")

movies = (vertigo, the_dark_knight, pay_it_forward, good_will_hunting, 
		  raman_raghav_2, arrival, silence_of_the_lambs, dead_poets_society, the_birds)


fresh_tomatoes.open_movies_page(movies)