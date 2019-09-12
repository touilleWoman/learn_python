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




def init_map(max_x, max_y):
	tab = []
	for j in range(max_y):
		tab.append([])
		for i in range(max_x):
			tab[j].append([0, None, None])
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
				nei_lst.append((i, j))
			i = i + 1
		i = current_x - 1
		j = j + 1
	return (nei_lst)

def get_distance(des_x, des_y, current_x, current_y):
	distance_x = abs(des_x - current_x)
	distance_y = abs(des_y - current_y)
	if distance_x > distance_y :
		return (distance_y * 14 + 10 * (distance_x - distance_y))
	return(14 * distance_x + 10 * (distance_y - distance_x))


def get_current(open_set, tab):
	current = None
	min_fcost = None
	for val in open_set:
		if current == None:
			current = val
			min_fcost = tab[val[1]][val[0]][1]
		else:
			if tab[val[1]][val[0]][1] == None:
				pass
			elif min_fcost == None:
				min_fcost = tab[val[1]][val[0]][1]
			elif tab[val[1]][val[0]][1] < min_fcost:
				min_fcost = tab[val[1]][val[0]][1]
				current = val
	return (current)



def pathfind_loop(tab, start, dest):
	WALL = 1
	EMPTY = 0
	DEST = 2
	START = 3
	open_set = set()
	closed_lst = []

	# start[0], start_y[1] = find_pos(START, tab)
	# des_x, des_y = find_pos(DEST, tab)
	open_set.add(start)
	while True:
		current = get_current(open_set, tab)
		open_set.remove(current)
		closed_lst.insert(0, current)
		if current[0] == dest[0] and current[1] == dest[1]:
			print('reached destination')
			return (closed_lst)
		nei_list = get_neighbour_lst(tab, current[0], current[1])
		i = 0
		while i < len(nei_list):
			if tab[nei_list[i][1]][nei_list[i][0]][0] == WALL:
				pass
			elif nei_list[i] in closed_lst :
				pass
			elif nei_list[i] not in open_set :
				f_cost = get_distance(dest[0], dest[1], nei_list[i][0], nei_list[i][1])
				+ get_distance(start[0], start[1], nei_list[i][0], nei_list[i][1])
				tab[nei_list[i][1]][nei_list[i][0]][1] = f_cost
				tab[nei_list[i][1]][nei_list[i][0]][2] = current # parent of node
				open_set.add(nei_list[i])
			i = i + 1

def retrace(closed_lst, start, tab):
	path = []
	first = closed_lst.pop(0)
	parent = tab[first[1]][first[0]][2]
	i = 0
	while parent != start:
		path.insert(0, parent)
		for one in closed_lst:
			if one == parent:
				parent = tab[one[1]][one[0]][2]
				break
	return(path)


def main():
	MAX_Y = 10
	MAX_X = 10
	tab = init_map(MAX_X, MAX_Y)
	start = (7, 6)
	dest = (0, 0)
	tab[start[1]][start[0]][0] = 2
	tab[3][3][0] = 1
	tab[3][4][0] = 1
	tab[dest[1]][dest[0]][0] = 3
	show_first_val_of_map(tab)
	print('1 stand for wall, 3 need to find the fastest way to 2')
	closed_lst = pathfind_loop(tab, start, dest)
	path = retrace(closed_lst, start, tab)
	print('path', path)
	return(tab)




if __name__=="__main__":
	main()


