"""
// A program to check if two given line segments intersect 

"""
class Point:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y


class LineIntersect:

	def __init__(self, p1, q1, p2, q2):
		self.p1 = p1	
		self.q1 = q1
		self.p2 = p2
		self.q2 = q2

	def find_orientation(p, q, r):
    	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y); 

    	if (val == 0) return 0;

    	return (val)

	def on_segment(self, pline1, qline1, rline2):
		if max(pline1.x, qline1.x) >= rline2.x >= min(pline1.x, qline1.x):
			return True
		return False

	def do_intersect(self):
		d1 = find_orientation(self.p1, self.q1, self.p2)
		d2 = find_orientation(self.p1, self.q1, self.q2)
		d3 = find_orientation(self.p2, self.q2, self.p1)
		d4 = find_orientation(self.p2, self.q2, self.q1)

		if (d1 and d2 < 0) and (d3 and d4 < 0):
			return True

		elif d1 ==0 and on_segment(self.p1, self.q1, self.p2):
			return True

		elif d2 == 0 and on_segment(self.p1, self.q1, self.q2):
			return True

		elif d3 == 0 and on_segment(self.p2, self.q2, self.p1):
			return True

		elif d4 == 0 and on_segment(self.p2, self.q2, self.q1):
			return True
		else :
			return false

p1 = new Point(1, 1)
q1 = new Point(10, 1)

p2 = new Point(1, 2)
q2 = new Point(10, 2)

line_intersect = new LineIntersect(p1, q1, p2, q2)
print (line_intersect.do_intersect())
