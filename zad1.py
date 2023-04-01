import math


def count_panele(floor_width, floor_length, panel_width, panel_length, panels_in_the_box):
    floor_area = (floor_width * floor_length) * 1.1
    panel_area = panel_width * panel_length
    panels_number = math.ceil(floor_area / panel_area)
    number_of_boxes = math.ceil(panels_number / panels_in_the_box)
    print(f"Potrzeba {number_of_boxes} pudelek z panelami")


count_panele(12.0, 15.0, 1.2, 1.5, 8)
