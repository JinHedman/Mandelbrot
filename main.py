import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton


# max_iter: maximum number of iterations
# c: complex number
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter



zoom = 1.0
# function for detecting mouse click events
def onclick(event):
    if event.button is MouseButton.LEFT:
        plt.close('all')
        global zoom     # Ugly but works
        zoom *= 0.5     # Multiply zoom by a factor less than 1 to zoom in

        print(event.xdata,event.ydata)
        draw_image(event.xdata-zoom,event.xdata+zoom,event.ydata-zoom,event.ydata+zoom,500,500,100)
        
    
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

# function for drawing the Mandelbrot set
def draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

# function for drawing the Nova set
def draw_nova(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[nova(complex(r, i),max_iter) for r in r1] for i in r2]))

#yres - number of pixels in y direction
#xres - number of pixels in x direction
#max_iter - maximum number of iterations (used to control the level of detail)
def draw_image(xmin,xmax,ymin,ymax,xres,yres,max_iter):
    d = draw_mandelbrot(xmin,xmax,ymin,ymax,xres,yres,max_iter)
    fig, ax = plt.subplots()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    ax.imshow(d[2], extent=(xmin, xmax, ymin, ymax), cmap='hot', interpolation='nearest')
    plt.show()


    
def main():
    draw_image(-2.0,1.0,-1.5,1.5,500,500,100)


if __name__ == "__main__":
    main()