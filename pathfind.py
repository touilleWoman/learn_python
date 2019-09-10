# import pygame

# def main():
# 	pygame.init()
# 	pygame.font.init()
# 	logo = pygame.image.load("logo.png")
# 	pygame.display.set_icon(logo)
# 	# pygame.display.set_caption("minimal program")


#     # create a surface on screen that has the size of 240 x 180
# 	screen = pygame.display.set_mode((640,480))
# 	background = pygame.Surface(screen.get_size())
# 	# background.fill((255, 255, 255))
# 	background = background.convert()
# 	# screen.blit(background, (0, 0))
#         # define a variable to control the main loop
# 	running = True

# 	# main loop
# 	while running:
# 	# event handling, gets all event from the event queue
# 	# for event in pygame.event.get():
# 		event = pygame.event.wait()
# 		if event.type == pygame.QUIT:
# 			running = False
# 			# mainloop = False
# 		elif event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				running = False
# 				# mainloop = False
# 	pygame.quit()




# tab = (
# 	(2,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,1,1,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,3,0,0),
# 	(0,0,0,0,0,0,0,0,0,0),
# 	(0,0,0,0,0,0,0,0,0,0)
# 	)



print('1 stand for obstacles, 3 need to find the fastest way to 2')

def init_map(max_x, max_y):
	tab = []
	for j in range(max_y):
		tab.append([])
		for i in range(max_x):
			tab[j].append([0, None])
	return(tab)

def show_first_val_of_map(tab):
	for j in range(len(tab)):
		for i in range(len(tab[j])):
			print(tab[j][i][0], end = ' ')
		print()

def find_pos(val, double_list):
	for j in range(10):
		for i in range(10):
			if double_list[i][j][0] == val:
				return (i, j)

def get_neighbour_lst(tab, current_x, current_y):
	nei_lst = []
	j = current_y - 1
	i = current_x - 1
	while j <= current_y + 1 :
		while i <= current_x + 1:
			if i == current_x and j == current_y:
				pass
			elif j < len(tab) and i < len(tab[j]):
				nei_lst.append([i, j])
			i = i + 1
		i = current_x - 1
		j = j + 1
	return (nei_lst)

def get_distance(des_x, des_y, current_x, current_y):
	distance_x = abs(des_x - current_x)
	distance_y = abs(des_y - current_y)
	if distance_x > distance_y :
		return (distance_y * 14 + 10 * (distance_x - distance_y))
	return( 14 * distance_x + 10 (distance_y - distance_x))





def pathfind_loop(tab, open_set, closed_set):
	WALL = 1
	EMPTY = 0
	DEST = 2
	START = 3

	start_x, start_y = find_pos(START, tab)
	des_x, des_y = find_pos(DEST, tab)
	current_x = start_x
	current_y = start_y
	tab[current_y][current_x][1] = 'open'
	print('start position',current_x, current_y)
	while True:
		if current_x == des_x and current_y == des_y:
			print('found')
			return
		nei_list = get_neighbour_lst(tab, current_x, current_y)
		i = 0
		f_cost = get_distance(des_x, des_y, current_x, current_y) + get_distance(start_x, start_y, current_x, current_y)
		while i < len(nei_list):
			if tab[nei_list[i][1]][nei_list[i][0]][0] == WALL:
				pass
			elif tab[nei_list[i][1]][nei_list[0]][1] == 'closed':
				pass
			elif
				newf_cost = get_distance(des_x, des_y, current_x, current_y) + get_distance(start_x, start_y, current_x, current_y)
				if newf_cost < f_cost:
					f_cost = newf_cost
					current_x = nei_list[i][0]
					current_y = nei_list[i][1]
					tab[current_y][current_x][1] = 'closed'
				else
					closed
			i = i + 1




def main():
	MAX_Y = 10
	MAX_X = 10
	open_set = set()
	closed_set = set()
	tab = init_map(MAX_X, MAX_Y)
	tab[0][0][0] = 2
	tab[3][3][0] = 1
	tab[3][4][0] = 1
	tab[7][7][0] = 3
	show_first_val_of_map(tab)
	pathfind_loop(tab, open_set, closed_set)
	return(tab)




if __name__=="__main__":
	main()


