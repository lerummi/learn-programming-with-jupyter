# Maze generator -- Randomized Prim Algorithm

## Imports
import time
import random
import numpy as np
from IPython import display
import matplotlib.pyplot as plt

# Find number of surrounding cells
def surroundingCells(rand_wall, maze):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells


def erstelle_labyrinth(hoehe: int = 21, breite: int = 21, seed: int = 42) -> np.ndarray:

	wall = 'w'
	cell = 'c'
	unvisited = 'u'
	height = hoehe
	width = breite
	maze = []

	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(random.random()*height)
	starting_width = int(random.random()*width)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = 'w'
	maze[starting_height][starting_width - 1] = 'w'
	maze[starting_height][starting_width + 1] = 'w'
	maze[starting_height + 1][starting_width] = 'w'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(rand_wall, maze)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall, maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall, maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

				s_cells = surroundingCells(rand_wall, maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
		


	# Mark the remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = 'w'

	# Set entrance and exit
	for i in range(0, width):
		if (maze[1][i] == 'c'):
			maze[0][i] = 'c'
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == 'c'):
			maze[height-1][i] = 'c'
			break

	maze = np.array(maze)
	maze_ = np.zeros_like(maze, dtype=int)
	maze_[maze == "w"] = 1
	
	return maze_


def zeichne_labyrinth(maze: np.ndarray):

	ny, nx = maze.shape
	cx = np.arange(-0.5, ny + 0.5, 1)
	cy = np.arange(-0.5, nx + 0.5, 1)
	f, ax = plt.subplots(figsize=(5, 5))
	ax.pcolormesh(cy, cx, maze, cmap="Greys")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.xticks(np.arange(0, nx, 2))
	plt.yticks(np.arange(0, ny, 2))

	return f, ax


def wegelemente(maze: np.ndarray):

	x, y = (maze.T == 0).nonzero()
	x = [int(xi) for xi in x]
	y = [int(yi) for yi in y]
	return list(zip(x, y))
	

def eingang(maze: np.ndarray):


	weg = wegelemente(maze)

	# Eingang
	Y = 0
	for xi, yi in weg:
		if yi == Y:
			return xi, yi
		
	raise ValueError("Labyrinth hat keinen Eingang!")


def ausgang(maze: np.ndarray):

	weg = wegelemente(maze)

	# Eingang
	Y = maze.shape[0] - 1
	for xi, yi in weg:
		if yi == Y:
			return xi, yi
		
	raise ValueError("Labyrinth hat keinen Ausgang!")


def ist_freies_feld(x, y, maze) -> bool:

	return (x, y) in wegelemente(maze)


def zeige_weg(maze, naechstes_feld_functions):

	max_wegpunkte = 1000
	wegpunkt_i = 0

	f, ax = zeichne_labyrinth(maze)

	newax = f.add_axes(ax.get_position(), frameon=False)
	xlim = ax.get_xlim()
	ylim = ax.get_ylim()

	xi, yi = eingang(maze)
	Xa, Ya = ausgang(maze)
	dx = 0
	dy = 1
	xi = xi + dx
	yi = yi + dy

	while xi != Xa or yi != Ya:
		# Clear the previous plot on newax
		newax.clear()
		
		# Plot the latest point
		newax.plot(xi, yi, ".b")
		newax.set_xlim(xlim)
		newax.set_ylim(ylim)
		newax.set_xticks([])
		newax.set_yticks([])
		
		# Clear the output and display the updated plot
		display.clear_output(wait=True)
		display.display(plt.gcf())
		
		# Pause for a short time to visualize the update
		time.sleep(0.01)
		
		# Update the position
		xi, yi, dx, dy = naechstes_feld_functions(xi, yi, dx, dy, maze)
		
		wegpunkt_i = wegpunkt_i + 1
		if wegpunkt_i >= max_wegpunkte:
			break

	# After the loop ends, plot the final position
	newax.clear()
	newax.plot(xi, yi, ".b")
	newax.set_xlim(xlim)
	newax.set_ylim(ylim)
	newax.set_xticks([])
	newax.set_yticks([])
	display.clear_output(wait=True)
	display.display(plt.gcf())

	# Suppress the automatic display of the plot at the end
	plt.close(f)

	print("Geschafft!")


# Musterlösung
def gehe_nach(richtung, dx, dy):

    if richtung == "vor":
        dx_neu = dx
        dy_neu = dy
    elif richtung == "zurück":
        dx_neu = -dx
        dy_neu = -dy
    elif richtung == "links":
        dx_neu = dy
        dy_neu = -dx
    elif richtung == "rechts":
        dx_neu = -dy
        dy_neu = dx 

    return dx_neu, dy_neu

def naechstes_feld(xi, yi, dx, dy, maze):

    richtungen = ["links", "vor", "rechts", "zurück"]

    for richtung in richtungen:
        dx_neu, dy_neu = gehe_nach(richtung, dx, dy)
        x_neu = xi + dx_neu
        y_neu = yi + dy_neu
        if ist_freies_feld(x_neu, y_neu, maze):
            break

    return x_neu, y_neu, dx_neu, dy_neu