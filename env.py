class two_link_arm_env(object):

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass

class Viewer(pyglet.window.Window):

    def __init__(self):
        super(vieweer, self).__init__(width=400,
                                      height=400,
                                      resizable=False,
                                      caption='Arm',
                                      vsync=Flase)

        pyglet.gl.glClearColor(1, 1, 1, 1)

    def on_draw(self):
        self.clear()

    
    