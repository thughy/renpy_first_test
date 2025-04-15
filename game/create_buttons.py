from PIL import Image, ImageDraw
import os

# Create button directory if it doesn't exist
button_dir = "gui/button"
if not os.path.exists(button_dir):
    os.makedirs(button_dir)

# Create overlay directory if it doesn't exist
overlay_dir = "gui/overlay"
if not os.path.exists(overlay_dir):
    os.makedirs(overlay_dir)

# Create idle button (gray)
idle = Image.new('RGBA', (300, 60), (50, 50, 50, 230))
draw = ImageDraw.Draw(idle)
draw.rectangle([(0, 0), (299, 59)], outline=(100, 100, 100, 255))
idle.save(os.path.join(button_dir, "idle.png"))

# Create hover button (blue)
hover = Image.new('RGBA', (300, 60), (0, 120, 180, 230))
draw = ImageDraw.Draw(hover)
draw.rectangle([(0, 0), (299, 59)], outline=(0, 180, 255, 255))
hover.save(os.path.join(button_dir, "hover.png"))

# Create confirm overlay
confirm = Image.new('RGBA', (1280, 720), (0, 0, 0, 180))
confirm.save(os.path.join(overlay_dir, "confirm.png"))

# Create main menu overlay
main_menu = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
main_menu.save(os.path.join(overlay_dir, "main_menu.png"))

# Create textbox
textbox = Image.new('RGBA', (800, 200), (40, 40, 40, 200))
draw = ImageDraw.Draw(textbox)
draw.rectangle([(0, 0), (799, 199)], outline=(100, 100, 100, 255))
textbox.save("gui/textbox.png")

# Create namebox
namebox = Image.new('RGBA', (200, 50), (0, 120, 180, 200))
draw = ImageDraw.Draw(namebox)
draw.rectangle([(0, 0), (199, 49)], outline=(0, 180, 255, 255))
namebox.save("gui/namebox.png")

print("Button images created successfully!")
