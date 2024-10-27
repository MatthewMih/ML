# Creates 2d grid with images, alternating two parameters (x and y axes)
from PIL import Image
import numpy as np


def generate_image(param_a, param_b):
  pass
  return img # PIL image

params_a = [pass]
params_b = [pass]

all_images = []
for a in params_a:
  all_images.append([])
  for b in params_b:
    all_images[-1].append(generate_image(a, b))

# concatenations
w, h = all_images[0][0].size
I = len(all_images)
J = len(all_images[0])
grid = np.array((I*h, J*w, 3))
for i in range(I):
  for j in range(J):
    grid[i*h:(i + 1)*h, j*w:(j + 1)*w, :] = np.array(all_images[i][j])
grid = Image.fromarray(grid)

grid.save('grid.png')
