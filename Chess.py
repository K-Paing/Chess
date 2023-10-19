import pygame
from sys import exit

class king(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_king.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

class queen(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_queen.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

class bishop(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_bishop.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

class knight(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_knight.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

class rook(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_rook.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

class pawn(pygame.sprite.Sprite):
	def __init__(self,square,color):
		super().__init__()
		global squares
		self.color = color
		self.square = square
		self.image = pygame.image.load('graphics/white_pawn.png')
		self.image.set_colorkey((148,141,255))
		self.rect = self.image.get_rect(center = squares[self.square].center)

	# def move(self):
	# 	if self.rect.collidepoint(pygame.mouse.get_pos()):
	# 		return self.rect
	# 		print(self.rect.center)
	# 		#if move pawn to correct place:
	# 		#pawn_rect.center = squares[??].center
	# def update(self):
	# 	self.move()

pygame.init() #always need this line
screen = pygame.display.set_mode((1100,1100)) #pygame.display.set_mode((width,height))
pygame.display.set_caption('Chess') #titles the window 
clock = pygame.time.Clock() #needed to set fps limit
squares = {}
active_piece = None

for i,letter in zip(range(100,900,100),'abcdefgh'):
	for j,number in zip(range(100,900,100),'87654321'):
		if i % 200 == 100 and j % 200 == 0:
			squares[letter+number] = pygame.draw.rect(screen,'Grey',[i,j,100, 100])
		elif i % 200 == 0 and j % 200 == 100:
			squares[letter+number] = pygame.draw.rect(screen,'Grey',[i,j,100, 100])
		elif i % 200 == 100 and j % 200 == 100:
			squares[letter+number] = pygame.draw.rect(screen,'Brown',[i,j,100, 100])
		else:
			squares[letter+number] = pygame.draw.rect(screen,'Brown',[i,j,100, 100])

#adding in White Pawns
white_pawns = pygame.sprite.Group()
white_pawns.add(pawn('a2','white'))
white_pawns.add(pawn('b2','white'))
white_pawns.add(pawn('c2','white'))
white_pawns.add(pawn('d2','white'))
white_pawns.add(pawn('e2','white'))
white_pawns.add(pawn('f2','white'))
white_pawns.add(pawn('g2','white'))
white_pawns.add(pawn('h2','white'))

#adding in White Rooks
white_rooks = pygame.sprite.Group()
white_rooks.add(rook('a1','white'))
white_rooks.add(rook('h1','white'))

#adding in White Knights
white_knights = pygame.sprite.Group()
white_knights.add(knight('g1','white'))
white_knights.add(knight('b1','white'))

#adding in White Bishops
white_bishops = pygame.sprite.Group()
white_bishops.add(bishop('f1','white'))
white_bishops.add(bishop('c1','white'))

#adding in White_Queen
white_queens = pygame.sprite.Group()
white_queens.add(queen('d1','white'))

#adding in White_King
white_kings = pygame.sprite.Group()
white_kings.add(king('e1','white'))


#White Pieces
White_pieces = [white_pawns.sprites(),white_rooks.sprites(),white_knights.sprites(),white_bishops.sprites(),white_queens.sprites(),white_kings.sprites()]

while True:
	for i,letter in zip(range(100,900,100),'abcdefgh'):
		for j,number in zip(range(100,900,100),'87654321'):
			if i % 200 == 100 and j % 200 == 0:
				squares[letter+number] = pygame.draw.rect(screen,'Grey',[i,j,100, 100])
			elif i % 200 == 0 and j % 200 == 100:
				squares[letter+number] = pygame.draw.rect(screen,'Grey',[i,j,100, 100])
			elif i % 200 == 100 and j % 200 == 100:
				squares[letter+number] = pygame.draw.rect(screen,'Brown',[i,j,100, 100])
			else:
				squares[letter+number] = pygame.draw.rect(screen,'Brown',[i,j,100, 100])



	for event in pygame.event.get(): 
		if event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse is clicking a piece
			if event.button == 1:
				for white in White_pieces:
					for piece in white:
						if piece.rect.collidepoint(event.pos):
				 			active_piece=piece.rect
				# for white_rook1 in white_rooks.sprites():
				# 	if white_rook1.rect.collidepoint(event.pos):
				# 		active_piece=white_rook1.rect
				# for white_pawn1 in white_pawns.sprites():
				# 	if white_pawn1.rect.collidepoint(event.pos):
				# 		active_piece=white_pawn1.rect

		if event.type == pygame.MOUSEMOTION:	#moves the chess piece	
			if active_piece != None:
		 		active_piece.move_ip(event.rel)

		if event.type ==pygame.MOUSEBUTTONUP: #puts down the active piece
			if event.button ==1:
				active_piece = None

		if event.type == pygame.QUIT: #this if statement allows you to quit the game 
			pygame.quit()
			exit()

	white_pawns.draw(screen)
	#white_pawns.update()
	
	white_rooks.draw(screen)

	white_knights.draw(screen)

	white_bishops.draw(screen)

	white_queens.draw(screen)

	white_kings.draw(screen)
	#white_pawns.update()
	#pygame.draw.circle(screen, (74,74,74), squares['a1'].center,20) #to highlight areas you can move to
	# screen.blit(white_pawn,white_pawna2_rect)
	# screen.blit(white_pawn,white_pawnb2_rect)
	


	pygame.display.update() #updated the display 
	clock.tick(60)