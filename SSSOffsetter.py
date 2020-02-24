import json

# This code changes the offset of the spriteSourceSize

print("What is the X-Offset?: ")
x_value = input()
print('x_value:', x_value)
print("What is the Y-Offset?: ")
y_value = input()
print('y_value:', y_value)

original_sss = {}

with open('original.json') as original:
    filedata = json.load(original)
    for sss in filedata['frames']:
        spriteSourceSize = sss['spriteSourceSize']
        original_x_value = spriteSourceSize['x']
        spriteSourceSize['x'] = int(float(original_x_value) + float(x_value or 0))
        original_y_value = spriteSourceSize['y']
        spriteSourceSize['y'] = int(float(original_y_value) + float(y_value or 0))

with open('animation_atlas_variant00.json', 'w') as output:
    json.dump(filedata, output, indent=2)