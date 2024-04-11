from world import World
from viewport import Viewport
from point import Point
from line import Line
from wireframe import Wireframe
from window_main import WindowMain
from transformator import Transformator
from obj_descriptor import ObjDescriptor

world = World()
viewport = Viewport()
main_window = WindowMain(world, viewport)
obj_descriptor = ObjDescriptor()

obj_descriptor.obj_to_object("../objects/quadrado.obj", world)
obj_descriptor.obj_to_object("../objects/triangulo.obj", world)
obj_descriptor.obj_to_object("../objects/linha.obj", world)
obj_descriptor.obj_to_object("../objects/pentagon.obj", world)

if __name__ == "__main__":
    main_window.post_init()
    main_window.main()
