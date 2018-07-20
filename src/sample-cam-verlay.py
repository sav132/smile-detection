import wx
from cv2 import *

capture = cv2.VideoCapture(1)

overlay = cv2.imread("happy.jpeg")
posx = 0
posy = 0

xdir = 1
ydir = 1

xspeed = 1
yspeed = 1

S = (0.5, 0.5, 0.5, 0.5)
D = (0.5, 0.5, 0.5, 0.5)

class MyFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size = (640, 480))
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self.Bind(wx.EVT_PAINT, self.on_paint)
		self.update()

	def update(self):
		self.Refresh()
		self.Update()
		wx.CallLater(1, self.update)

	def on_paint(self, event):
		src = cv.QueryFrame(capture)
		if src:
			overlaid = self.OverlayImage(src, overlay, S, D)
			self.bitmap = wx.Bitmap('src.png')
			dc = wx.PaintDC(self)
			dc.DrawBitmap(self.bitmap, 0, 0)

	def OverlayImage(self, src, overlay, S, D):

		global posx, posy, xdir, ydir

		if posx+overlay.width+xdir*xspeed >= src.width:
			xdir = -1*xspeed
			posx = src.width - overlay.width
		elif posx < 0:
			xdir = 1*xspeed
			posx = 0
		else:
			posx = posx+xdir*xspeed

		if posy+overlay.height+ydir*yspeed >= src.height:
			ydir = -1*yspeed
			posy = src.height - overlay.height
		elif posy < 0:
			ydir = 1*yspeed
			posy = 0
		else:
			posy=posy+ydir*yspeed

		for x in range(overlay.width):

			if x+posx < src.width:

				for y in range(overlay.height):

					if y+posy < src.width:

						source = cv.Get2D(src, y+posy, x+posx)
						over   = cv.Get2D(overlay, y, x)
						merger = [0, 0, 0, 0]

						for i in range(3):
							if over[i] < 40:
								merger[i] = source[i]
							else:
								merger[i] = (S[i]*source[i]+D[i]*over[i])

						merged = tuple(merger)

						cv.Set2D(src, y+posy, x+posx, merged)
		cv.SaveImage('src.png', src) #Saves the image


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Spooky!')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()
