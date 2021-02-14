"""
Here's a paper I found helpful while exploring connections
between Chebyshev polynomials and Lissajous figures
http://boj.pntic.mec.es/~jcastine/Trabajos%20matematicos_archivos/cmj122-127.pdf

Followed a few different animation guides, linked

following ex from Wyoming U (attached? linked?)
there's already a good example of anims under
matplotlibs docs, but they use a class with
member functions which i think is a little
more complicated/less intuitive than what
I need here. 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random as rand

#data yielding func
def func_gen(xpi, xvi, xw, xw2, ypi, yvi, yw, yw2):
  # time var starting at t = 0
  t = 0
  i = 0
  for i in range(totstep):
    # calc func value at each time step
    # using solution from problem 2 of AD HW 1
    x = xpi*np.cos(xw*t) + (xvi/xw2)*np.sin(xw*t)
    y = ypi*np.cos(yw*t) + (yvi/yw2)*np.sin(yw*t)
    t += step
    yield t, x, y

#update func
def update(data):
  t, x, y = data
  xdata.append(x)
  ydata.append(y)
  
  line.set_data(xdata, ydata)
  head.set_data(x, y)
  return holder

if __name__ == "__main__":
  print("Some available presets are: circle, line, lemniscate, parabola, fish, abc, pretzel.")
  print("You can set all initial conditions and oscillator properties yourself if you'd like, but the presets will save you time. To set your own everything, give 'custom' as an argument to the presets argument. Your input will be ignored otherwise and random ICs will be used.")
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('--x_pos_i', '-xp', dest="xpi", required=False, default=0.0, action='store', help="x initial position")
  parser.add_argument('--y_pos_i', '-yp', dest="ypi", required=False, default=0.0, action='store', help="y initial position")
  parser.add_argument('--x_vel_i', '-xv', dest="xvi", required=False, default=0.0, action='store', help="x initial velocity")
  parser.add_argument('--y_vel_i', '-yv', dest="yvi", required=False, default=0.0, action='store', help="y initial velocity")
  parser.add_argument('--x_mass', '-xm', dest="xmass", required=False, default=1.0, action='store', help="Mass of X osc.")
  parser.add_argument('--y_mass', '-ym', dest="ymass", required=False, default=1.0, action='store', help="Mass of Y osc.")
  parser.add_argument('--x_spring', '-xk', dest="xk", required=False, default=1.0, action='store', help="Spring const of X osc.")
  parser.add_argument('--y_spring', '-yk', dest="yk", required=False, default=1.0, action='store', help="Spring const of Y osc.")
  parser.add_argument('--preset', '-p', dest="preset", required=False, default="None", action='store', help="preset?") 
  #now initialize, then animate
  args = parser.parse_args()
  
  # lists of initial coniditions and oscillator properties
  """
  list format
  var = [
  user input if given, 
  random dbl 0 to 3 otherwise,
  Circle, 
  Line, #1st Chebyshev polynomial  
  Lemniscate of Gerono, #figure 8
  Parabola, #2nd Chebyshev polynomial
  Tschirunhausen cubic, #fish in presets
  ABCs Logo, #Australian Broadcasting Corp. 
  Pretzel #it's sideways]
  """
  # init conds lists
  xpis = [float(args.xpi), rand.uniform(0, 3.0), 1.0, 1.0,\
1.0, -1.0, 1.0, 1.0, 1.0, 1.30, 3.00]
  ypis = [float(args.ypi), rand.uniform(0, 3.0), 0.0, 1.0,\
0.0, 0.0, 0.0, 0.0, 0.0, 0.07, 0.75]
  xvis = [float(args.xvi), rand.uniform(0, 3.0), 0.0, 1.0,\
0.0, 0.0, 0.0, 0.0, 0.0, 0.54, 0.64]
  yvis = [float(args.yvi), rand.uniform(0, 3.0), 1.0, 1.0,\
0.5, 2.0, 1.0, 1.0, 1.0, 0.47, 1.68]
  
  #osc props lists
  xmasses = [float(args.xmass), rand.uniform(1.1, 3.0), 1.0,\
1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.20, 1.63]
  ymasses = [float(args.ymass), rand.uniform(0.1, 3.0), 1.0,\
1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.20, 1.50]
  xks = [float(args.xk), rand.uniform(0.1, 3.0), 1.0, 1.0,\
1.0, 4.0, 4.0, 1.0, 8.0, 0.50, 2.72]
  yks = [float(args.yk), rand.uniform(0.1, 3.0), 1.0, 1.0,\
4.0, 1.0, 9.0, 9.0, 4.5, 2.14, 2.45]

  key = 0
  # i should be using case here
  if args.preset.lower() == "custom":
    key = 0
  elif args.preset.lower() == "none":
    key = 1
  elif args.preset.lower() == "circle":
    key = 2
  elif args.preset.lower() == "line":
    key = 3
  elif args.preset.lower() == "lemniscate":
    key = 4
  elif args.preset.lower() == "parabola":
    key = 5
  elif args.preset.lower() == "fish":
    key = 6
  elif args.preset.lower() == "abc":
    key = 7
  elif args.preset.lower() == "pretzel":
    key = 8
  elif args.preset.lower() == "blurry_fish":
    key = 9
  elif args.preset.lower() == "white_diamond":
    key = 10
  else:
    key = 1 #random ICs and osc props
  
  #init conds assignment
  xpi = xpis[key] # x init pos
  ypi = ypis[key] # y init pos
  xvi = xvis[key] # x init vel
  yvi = yvis[key] # y init vel
  
  #osc props assignment
  xmass = xmasses[key] # mass of xdir osc
  ymass = ymasses[key] # mass of ydir osc
  xk = xks[key] # spring const of xdir osc
  yk = yks[key] # spring const of ydir osc

  #derived osc consts  
  xw2 = xk/xmass
  xw = np.sqrt(xw2)
  yw2 = yk/ymass
  yw = np.sqrt(yw2)

  # anim consts (left these hardcoded, don't really 
  # want user messing with them unless 
  # they know what they're doing)
  step = 0.1 #min([xw,yw])/10
  totstep = 1000
 
  # make figs and set axes
  """ use the fact that energy is conserved to find the max 
  amplitude of the x and y oscillators. Namely,
  KE + PE = E, where KE = 0.5m*v**2, and PE = 0.5*k*x**2. So,
  KEi + PEi = KE(t) + PE(t) = PE(max) = 0.5*k*A**2 
  when PE is a max, KE is a min (zero).
  A is the max amplitude. The example above was 1D but is easily
  extended to 2D. """
  Ax2 = xpi**2 + xvi**2/xw2
  Ay2 = ypi**2 + yvi**2/yw2
  A = np.sqrt(Ax2+Ay2)+1.5
  
  fig = plt.figure()
  ax = plt.axes(xlim=(-A, A), ylim=(-A, A))
  ax.grid()
  ax.set_aspect('equal')

  title = "Lissajous Figure from Independent X&Y SHOs \npreset = {}".format(args.preset)
  plt.title(title)
  # makeshift legend of ICs and osc props
  plt.text(A, -A, " Initial Conditions:\n"
  " xi = {:0.2f}\n yi = {:0.2f}\n vx = {:0.2f}\n vy = {:0.2f}\n"
  " Osc. Properties:\n"
  " xmass = {:0.2f}\n ymass = {:0.2f}\n xk = {:0.2f}\n"
  " yk = {:0.2f}".format(xpi,ypi,xvi,yvi,xmass,ymass,xk,yk))

  xdata, ydata, xpoint, ypoint = [], [], [], []
  line, = ax.plot(xdata, ydata, lw=2, color='black') 
  head, = ax.plot(xpoint, ypoint, color='red', marker='o', markeredgecolor='r') 
  holder = [line, head]

  #anim func
  ani = anim.FuncAnimation(fig, update, func_gen(xpi, xvi, xw, xw2, ypi, yvi, yw, yw2), blit=True, interval=50, repeat=False)
  plt.show()
  print("ICs: (x, y, vx, vy) = ({:0.4f}, {:0.4f}, {:0.4f}, {:0.4f})".format(xpi, ypi, xvi, yvi))
  print("Osc. Props.: xmass = {:0.4f}, ymass = {:0.4f}, xk =  {:0.4f}, yk = {:0.4f}".format(xmass, ymass, xk, yk)) 
  print("X spring-to-mass ratio: {:0.3f}".format(xw2))
  print("Y spring-to-mass ratio: {:0.3f}".format(yw2))
