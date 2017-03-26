# -----------------------------------------------------------------------------
# Copyright (c) 2017 Nicolas P. Rougier. All rights reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app, gl, glm, gloo


cone_vertex = """
uniform mat4 projection;
attribute vec2 translate;
attribute vec3 position;
attribute vec3 color;
varying vec3 v_color;
void main()
{
    v_color.rgb = color.rgb;
    gl_Position = projection * vec4(position.xy+translate, position.z ,1.0);
}
"""

cone_fragment = """
varying vec3 v_color;
void main()
{
    gl_FragColor = vec4(v_color.rgb, 1.0);
}
"""


n_point = 1000
width, height = 1024, 1024
window = app.Window(width=width, height=height)

@window.event
def on_draw(dt):
    window.clear()
    cones.draw(gl.GL_TRIANGLES, I)

    # Read back image
    RGB = np.zeros((window.height, window.width, 3), dtype=np.uint8)
    gl.glReadPixels(0, 0, window.width, window.height,
                    gl.GL_RGB, gl.GL_UNSIGNED_BYTE, RGB)
    V = (RGB[...,0]*256*256 + RGB[...,1]*256 + RGB[...,2]).ravel()

    # Get individual Voronoi cells as a list of flatten indices
    # This works because we took care of having unique colors
    # See also StackOverflow:
    #  "Get a list of all indices of repeated elements in a numpy array"
    idx_sort = np.argsort(V)
    sorted_V = V[idx_sort]
    _, idx_start = np.unique(sorted_V, return_index=True)
    regions = np.split(idx_sort, idx_start[1:])

    shape = window.height, window.width
    for i,region in enumerate(regions[1:]):
        Y, X = np.unravel_index(region, shape)
        C["translate"][i] = X.mean(), Y.mean()


@window.event
def on_close():
    np.save("test.npy",C["translate"])


@window.event
def on_resize(width, height):
    cones['projection'] = glm.ortho(0, width, 0, height, -5, +500)

def makecone(n=32, radius=1024):
    height = radius / np.tan(45 * np.pi / 180.0)
    V = np.zeros((1+n,3))
    V[0] = 0,0,0
    T = np.linspace(0,2*np.pi,n, endpoint=False)
    V[1:,0] = radius*np.cos(T)
    V[1:,1] = radius*np.sin(T)
    V[1:,2] = -height
    I  = np.repeat([[0,1,2]], n, axis=0).astype(np.uint32)
    I += np.arange(n,dtype=np.uint32).reshape(n,1)
    I[:,0] = 0
    I[-1] = 0,n,1
    return V, I.ravel()


n = n_point # number of cones (= number of points)
p = 24      # faces per cones

cones = gloo.Program(cone_vertex, cone_fragment)
C = np.zeros((n,1+p), [("translate", np.float32, 2),
                       ("position",  np.float32, 3),
                       ("color",     np.float32, 3)]).view(gloo.VertexBuffer)
I = np.zeros((n,3*p), np.uint32).view(gloo.IndexBuffer)
I += (1+p)*np.arange(n, dtype=np.uint32).reshape(n,1)

# Arbitrary but large scaling is important to better distinguish color later
# when they will converted back to bytes.
val = np.arange(1,n+1)*256
rgb = np.zeros((n,3), dtype=np.float32)
rgb[:,0] = (val//1)     % 256
rgb[:,1] = (val//256)   % 256
rgb[:,2] = (val//65536) % 256

for i in range(n):
    vertices, indices = makecone(p, radius=512)
    C["color"][i] = rgb[i] / 255.0
    C["position"][i] = vertices
    x = np.random.uniform(0, width)
    y = np.random.uniform(0, height)
    C["translate"][i] = x,y
    I[i] += indices.ravel()
cones.bind(C)

gl.glEnable(gl.GL_DEPTH_TEST)
app.run()
