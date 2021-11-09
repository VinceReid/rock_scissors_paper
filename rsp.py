import pygame
import random

# CTRL B to start game

class rsp_game():

	def __init__(self):
		# Initialise game attributes
		self.rsp = ["rock", "scissors", "paper"]
		self.height = 600
		self.width = 900
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen_rect = self.screen.get_rect()
		self.screen_y = self.screen_rect.y 
		self.screen_x = self.screen_rect.x 
		self.margin = 10
		self.play_width = self.width - self.margin*2
		self.play_height = self.height - self.margin*2
		self.top_left_x = self.margin
		self.top_left_y = self.margin
		self.info_width = 400
		self.info_height = 150
		self.top_box_height = 50
		self.your_score = 0
		self.comp_score = 0
		self.result = ""
		self.previous_choice = [random.choice(self.rsp)]
		self.comp_previous_choice = []
		pygame.font.init()
		self.font = pygame.font.SysFont('comicsans', 30, bold=True)
		pygame.display.set_caption("Rock, Scissors, Paper")


	def main_menu(self):
		# Intro loop, prior to main run loop
		run = True
		while run:
			self.screen.fill((0, 0, 0))
			self.draw_margin()
			self.draw_text_top_center("ROCK | SCISSORS | PAPER", 80, (255, 0, 0), self.screen)
			self.draw_text_middle("Press any key to start", 80, (255, 255, 255), self.screen)
			self.draw_text_bottom("Press 'Q' to Quit at any time!", 50, (255, 255, 255), self.screen)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
					else:
						self.choose()
						
		pygame.quit()


# Main game loop
	def start_game(self):
		run = True
		while run:
			self.count_down()
			self.draw_screen()
			pygame.display.update()
			self.rsp = ["rock", "scissors", "paper"]
			self.improved_rand()
			self.computer_choice = self.random_choice()
			self.choice_made()
			self.check_result()
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()

			self.choose()

		pygame.quit()

	def random_choice(self):
		# return a random choice
		choice = random.choice(self.rsp)
		self.comp_previous_choice.append(choice)
		return choice


# draw text in various positions


	def draw_text_top_center(self, text, size, color, screen):
		font = pygame.font.SysFont('comicsans', size, bold=True)
		self.top_left_label = font.render(text, 0, color)
		x_pos = self.top_left_x + self.play_width/2 - (self.top_left_label.get_width() /2)
		y_pos = self.top_left_y + self.margin + self.top_left_label.get_height()/2
		self.text_box = pygame.Rect(x_pos, y_pos, self.top_left_label.get_width(), self.top_left_label.get_height())
		screen.blit(self.top_left_label, (x_pos, y_pos))

	def draw_text_middle(self, text, size, color, screen):
		font = pygame.font.SysFont('comicsans', size, bold=True)
		self.label = font.render(text, 1, color)
		x_pos = self.top_left_x + self.play_width/2 - (self.label.get_width() /2)
		y_pos = self.top_left_y + self.play_height/2 - (self.label.get_height() /2)
		self.text_box = pygame.Rect(x_pos, y_pos, self.label.get_width(), self.label.get_height())
		screen.blit(self.label, (x_pos, y_pos))

	def draw_text_top_left(self, text, size, color, screen):
		font = pygame.font.SysFont('comicsans', size, bold=True)
		self.top_left_label = font.render(text, 1, color)
		x_pos = self.top_left_x + self.play_width/4 - (self.top_left_label.get_width() /2)
		y_pos = self.top_left_y + self.margin + self.top_left_label.get_height()/2
		self.text_box = pygame.Rect(x_pos, y_pos, self.top_left_label.get_width(), self.top_left_label.get_height())
		screen.blit(self.top_left_label, (x_pos, y_pos))

	def draw_text_top_right(self, text, size, color, screen):
		font = pygame.font.SysFont('comicsans', size, bold=True)
		self.top_right_label = font.render(text, 1, color)
		x_pos = self.top_left_x + self.play_width/4*3 - (self.top_right_label.get_width() /2)
		y_pos = self.top_left_y + self.margin + self.top_right_label.get_height()/2
		self.text_box = pygame.Rect(x_pos, y_pos, self.top_right_label.get_width(), self.top_right_label.get_height())
		screen.blit(self.top_right_label, (x_pos, y_pos))

	def draw_text_bottom(self, text, size, color, screen):
		font = pygame.font.SysFont('comicsans', size, bold=True)
		self.label = font.render(text, 1, color)
		x_pos = self.top_left_x + self.play_width/2 - (self.label.get_width() /2)
		y_pos = self.top_left_y + self.play_height - self.margin - self.info_height/2 - (self.label.get_height() /2)
		self.text_box = pygame.Rect(x_pos, y_pos, self.label.get_width(), self.label.get_height())
		screen.blit(self.label, (x_pos, y_pos))


# Draw lines and boxes in various positions. 
	def draw_info_box(self):
		pygame.draw.rect(self.screen, (255, 0, 0), (self.width /2 - (self.info_width /2) , self.height - self.info_height - self.margin, self.info_width, self.info_height), 5)

	def draw_margin(self):
		pygame.draw.rect(self.screen, (255, 0, 0), (self.top_left_x, self.top_left_y, self.play_width, self.play_height), 5)

	def draw_line(self):
			pygame.draw.line(self.screen, (255, 0, 0), (self.top_left_x + self.play_width/2, self.top_left_y),
							(self.top_left_x + self.play_width/2, self.height - self.info_height - self.margin), 5)
	def draw_short_line(self):
		pygame.draw.line(self.screen, (255, 0, 0), (self.top_left_x + self.play_width/2, self.top_left_y),
						(self.top_left_x + self.play_width/2, self.top_box_height + self.margin*2), 5)	

	def draw_top_line(self):
			pygame.draw.line(self.screen, (255, 0, 0), (self.top_left_x, self.top_left_y + self.margin + self.top_box_height),
							(self.width - self.margin, self.top_left_y + self.margin + self.top_box_height), 5)


	def choice_made(self):
		# move selectet image across screen
		image_list = {"rock": "images/rock.bmp", "paper": "images/paper.bmp", "scissors": "images/scissors.bmp"}
		rand_image_list = {"rock": "images/comprock.bmp", "paper": "images/comppaper.bmp", "scissors": "images/compscissors.bmp"}
		for image in image_list.keys():
			if image == self.player_choice:
				self.choice = pygame.image.load(image_list[image])
				self.rect = self.choice.get_rect()
				self.rect.x = self.screen_x - self.rect.width
				self.rect.y = self.height/2 - (self.rect.height//2)

		for rand_image in rand_image_list.keys():
			if rand_image == self.computer_choice:
				self.rand_choice = pygame.image.load(rand_image_list[rand_image])
				self.rand_rect = self.rand_choice.get_rect()
				self.rand_rect.x = self.width
				self.rand_rect.y = self.height/2 - (self.rand_rect.height//2)

		while self.rand_rect.left > self.width/2 + 5:
			self.rand_rect_x = float(self.rand_rect.x)
			self.rand_rect_x -= 0.1
			self.rand_rect.x = self.rand_rect_x
			self.screen.blit(self.rand_choice, self.rand_rect)
			self.rect_x = float(self.rect.x)
			self.rect_x += 0.1
			self.rect.x = self.rect_x
			self.screen.blit(self.choice, self.rect)
			pygame.display.flip()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
				

	def choose(self):
		# select rock scissors or paper by hover and click, append choice to list. 
			run = True
			while run:
				# start the game
				mouse_pos = pygame.mouse.get_pos()
				self.draw_screen()
				self.draw_text_bottom("MAKE YOUR CHOICE!", 40, (0, 0, 255), self.screen)
				self.choose_image(mouse_pos)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							pygame.quit()

					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.left_hover:
							self.player_choice = "scissors"
							self.previous_choice.append(self.player_choice)
							self.start_game()
						if self.middle_hover:
							self.player_choice = "rock"
							self.previous_choice.append(self.player_choice)
							self.start_game()
						if self.right_hover:
							self.player_choice = "paper"
							self.previous_choice.append(self.player_choice)
							self.start_game()
						
			pygame.quit()


	def choose_image(self, mouse_pos):
		# load image for selection. dependant on mouse position. 

		choose_image = pygame.image.load("images/choose.bmp")
		choose_scissors = pygame.image.load("images/choosescissors.bmp")
		choose_rock = pygame.image.load("images/chooserock.bmp")
		choose_paper = pygame.image.load("images/choosepaper.bmp")
		choose_rect = choose_image.get_rect()
		choice = choose_image

		rect_x = self.width //4
		rect_y = self.height - choose_rect.height - self.info_height - self.margin

		choose_rect.x = rect_x
		choose_rect.y = rect_y
		choose_rect_section = choose_rect.width//3

		rect_left = pygame.Rect(rect_x, rect_y, choose_rect_section, choose_rect.height)
		rect_middle = pygame.Rect(rect_x + choose_rect_section, rect_y, choose_rect_section, choose_rect.height)
		rect_right = pygame.Rect(rect_x + choose_rect_section*2, rect_y, choose_rect_section, choose_rect.height)

		self.left_hover = rect_left.collidepoint(mouse_pos)
		self.middle_hover = rect_middle.collidepoint(mouse_pos)
		self.right_hover = rect_right.collidepoint(mouse_pos)

		if self.left_hover:
			choice = choose_scissors
		if self.middle_hover:
			choice = choose_rock
		if self.right_hover:
			choice = choose_paper

		self.screen.blit(choice, choose_rect)

		pygame.display.flip()


	def draw_screen(self):
		self.screen.fill((0, 0, 0))
		self.draw_margin()
		self.draw_short_line()
		self.draw_top_line()
		self.draw_info_box()
		self.draw_text_top_left("YOU", 50, (255, 255, 255), self.screen)
		self.draw_text_top_right("COMPUTER", 50, (255, 255, 255), self.screen)
		self.draw_score()


	def count_down(self):
		text = ["ROCK!", "PAPER!", "SCISSORS!", "GO!"]
		for word in text:
			self.draw_screen()
			self.draw_text_bottom(word, 40, (0, 255, 0), self.screen)
			pygame.display.update()
			pygame.time.delay(700)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()


	def check_result(self):
		if self.player_choice == self.computer_choice:
			self.result = "DRAW"
		if self.player_choice == "rock" and self.computer_choice == "paper":
			self.result = "YOU LOSE"
		if self.player_choice == "rock" and self.computer_choice == "scissors":
			self.result = "YOU WIN!"
		if self.player_choice == "paper" and self.computer_choice == "rock":
			self.result = "YOU WIN!"
		if self.player_choice == "paper" and self.computer_choice == "scissors":
			self.result = "YOU LOSE"
		if self.player_choice == "scissors" and self.computer_choice == "rock":
			self.result = "YOU LOSE"
		if self.player_choice == "scissors" and self.computer_choice == "paper":
			self.result = "YOU WIN!"

		self.update_score(self.result)
		self.draw_text_bottom(self.result, 50, (0, 0, 255), self.screen)
		pygame.display.update()
		pygame.time.delay(2000)


	def update_score(self, result):
		if result == "DRAW":
			self.your_score += 1
			self.comp_score += 1
		if result == "YOU WIN!":
			self.your_score += 1
		if result == "YOU LOSE":
			self.comp_score += 1


	def draw_score(self):

		# Display the score at the bottom left of the screen.
		self.your_score_image = self.font.render(f"Your Score: {self.your_score}", True,
								(255, 255, 255), (0, 0, 0))
		self.your_score_rect = self.your_score_image.get_rect()
		self.your_score_rect.left = self.top_left_x + self.margin
		self.your_score_rect.bottom = self.height - self.margin - 5

		# Display the computer score at the bottom right of the screen.
		self.comp_score_image = self.font.render(f"Computer Score: {self.comp_score}", True,
		(255, 255, 255), (0, 0, 0))

		self.comp_score_rect = self.comp_score_image.get_rect()
		self.comp_score_rect.right = self.width - self.margin - 5
		self.comp_score_rect.bottom = self.height - self.margin - 5

		# Blit images to screen
		self.screen.blit(self.your_score_image, self.your_score_rect)
		self.screen.blit(self.comp_score_image, self.comp_score_rect)

	def improved_rand(self):
		opposite_dict = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
		what_beats_dict = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

		choice = self.previous_choice[-2]

		print(f"Previous: {self.previous_choice[-2]}")
		self.rsp.remove(opposite_dict[choice])
		self.rsp.remove(choice)
		print(f"random: {self.rsp}")

		if self.your_score + self.comp_score > 2:

			if self.previous_choice[-2] == self.previous_choice[-3]:
				retaliate = opposite_dict[self.previous_choice[-2]]
				self.rsp = [retaliate]

			if self.previous_choice[-2] == self.comp_previous_choice[-1] and self.previous_choice[-3] == self.comp_previous_choice[-2]:
				self.rsp = [choice]

			if self.previous_choice[-4] == self.previous_choice[-3] and self.previous_choice[-2] == opposite_dict[self.comp_previous_choice[-1]]:
				self.rsp = [self.previous_choice[-3]]

		print(self.previous_choice)

		print(self.comp_previous_choice)


if __name__ == "__main__":
	game = rsp_game()
	game.main_menu()