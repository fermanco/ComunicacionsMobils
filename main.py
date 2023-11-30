import numpy as np
import matplotlib.pyplot as plt

num_cells = 19
num_sectors = 3
central_cell_radius = 1  #  cell radius is 1 unit

# Function to generate hexagonal cell coordinates
def generate_hexagonal_cells():
    cell_coordinates = []
    for i in range(num_cells):
        angle = 2 * np.pi / num_cells * i
        x = central_cell_radius * np.cos(angle)
        y = central_cell_radius * np.sin(angle)
        cell_coordinates.append((x, y))
    return cell_coordinates

# Function to generate sectors within each cell
def generate_sectors(cell_coordinates):
    all_sectors = []
    for cell in cell_coordinates:
        cell_sectors = []
        for i in range(num_sectors):
            sector_angle = 2 * np.pi / num_sectors * i
            sector_x = cell[0] + 0.5 * np.cos(sector_angle)  
            sector_y = cell[1] + 0.5 * np.sin(sector_angle)  # from the center of each cell
            cell_sectors.append((sector_x, sector_y))
        all_sectors.append(cell_sectors)
    return all_sectors


cell_coords = generate_hexagonal_cells()
cell_sectors = generate_sectors(cell_coords)

# Display generated cell coordinates and sectors (for visualization purposes)
print("Cell Coordinates:")
for i, cell in enumerate(cell_coords):
    print(f"Cell {i + 1}: {cell}")

print("\nCell Sectors:")
for i, cell in enumerate(cell_sectors):
    print(f"Cell {i + 1} Sectors:")
    for j, sector in enumerate(cell):
        print(f"Sector {j + 1}: {sector}")

from matplotlib.patches import RegularPolygon

cell_c = np.array(cell_coords)
cell_s = np.array(cell_sectors)


def plot_hexagonal_cells_and_sectors(cell_sectors):
    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(0, num_cells):
        hexagon = RegularPolygon(cell_c[i], numVertices=6, radius=central_cell_radius, edgecolor='blue', facecolor='none')
        ax.add_patch(hexagon)


    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Hexagonal Cells and Sectors')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_hexagonal_cells_and_sectors(cell_sectors)

