import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

num_cells = 19
num_sectors = 3
central_cell_radius = 1  #  cell radius is 1 unit
iterations_ring1 = 6
iterations_ring2 = 2*iterations_ring1

# Function to generate hexagonal cell coordinates
def generate_hexagonal_cells():
    cell_coordinates = []
    center_cell = [0, 0] #central cell coordinates
    cell_coordinates.append(center_cell)
    for i in range(iterations_ring1): #iterations of the first ring among the central cell
        angle = 2 * np.pi / iterations_ring1 * i
        x = (center_cell[0] + np.sqrt(3)) * np.cos(angle)
        y = (center_cell[1] + np.sqrt(3)) * np.sin(angle)
        cell_coordinates.append((x, y))

    for i in range(iterations_ring2): #iterations of the second ring of cells
        angle = 2 * np.pi / iterations_ring2 * i
        if (i % 2) == 0: #needed to specify distances between center and exterior cells
        	x = (center_cell[0] + 2*np.sqrt(3)) * np.cos(angle)
        	y = (center_cell[1] + 2*np.sqrt(3)) * np.sin(angle)
        else:
        	x = (center_cell[0] + 3) * np.cos(angle)
        	y = (center_cell[1] + 3) * np.sin(angle)
        cell_coordinates.append((x, y))
    return cell_coordinates
    
# Function to generate sectors within each cell
def generate_sectors(cell_coordinates):
    all_sectors = []
    for cell in cell_coordinates:
        cell_sectors = []
        for i in range(num_sectors):
            sector_angle = 2 * np.pi / num_sectors * i
            sector_x = cell[0] + np.sqrt(3)/2*np.cos(sector_angle)  
            sector_y = cell[1] + np.sqrt(3)/2*np.sin(sector_angle)  # from the center of each cell
            cell_sectors.append((sector_x, sector_y))
        all_sectors.append(cell_sectors)
    return all_sectors

# Display generated cell coordinates and sectors (for visualization purposes)
def print_coordinates_function():
	print("Cell Coordinates:")
	for i, cell in enumerate(cell_coords):
		print(f"Cell {i + 1}: {cell}")

	print("\nCell Sectors:")
	for i, cell in enumerate(cell_sectors):
		print(f"Cell {i + 1} Sectors:")
		for j, sector in enumerate(cell):
		    print(f"Sector {j + 1}: {sector}")

#Function to plot cells and sectors (for visualization purposes)
def plot_hexagonal_cells_and_sectors(cell_c, cell_s):

	fig, ax = plt.subplots(figsize=(8, 8))
	plt.scatter(cell_c[:, 0], cell_c[:, 1], marker='o', color='blue', label='Cell Centers')
	
	for i in range(num_cells):
		hexagon = RegularPolygon(cell_c[i], numVertices=6, radius=central_cell_radius, edgecolor='black', facecolor='none')
		ax.add_patch(hexagon)
		
	for i in range(num_cells):
		cell = cell_c[i]
		group = cell_s[i]
		for j in range(3):
			sector = group[j]
			xpoints = [cell[0], sector[0]]
			ypoints = [cell[1], sector[1]]
			plt.plot(xpoints, ypoints, linestyle = 'dotted', color='red')
			
	plt.axis('equal')
	plt.xlabel('X-axis')
	plt.ylabel('Y-axis')
	plt.title('Hexagonal Cells and Sectors')
	plt.legend()
	plt.grid(True)
	plt.show()

######################################################################################
#creating the lists
cell_coords = generate_hexagonal_cells()
cell_sectors = generate_sectors(cell_coords)

#np array transformation of te previous defined lists
cell_c = np.array(cell_coords)
cell_s = np.array(cell_sectors)

#printings and plotings
#print_coordinates_function()
plot_hexagonal_cells_and_sectors(cell_c, cell_s)

