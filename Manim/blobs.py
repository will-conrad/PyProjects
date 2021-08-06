from manim import *
from manim.opengl import *

SIMPLE_BLUE = "#00BDFA"


class MarchingSquaresAdvance1(Scene):
    def construct(self):
        self.rows = 64
        self.columns = 64
        self.mpoints = VGroup()
        self.circles = VGroup(*[Dot(radius=0.4, fill_opacity=0) for _ in range(5)])

        self.circles.to_edge(LEFT, buff=-2)
        self.width = config.frame_width * 1.2
        self.height = self.circles.height * 3
        self.set_coords()
        self.mpoints.add_updater(self.update_mpoints, index=0)
        self.mpoints.add_updater(self.update_boundary, index=1)
        self.add(self.circles, self.mpoints)

        animations1 = LaggedStart(
            *[circle.animate.move_to(ORIGIN) for circle in self.circles], lag_ratio=0.2
        )
        animations2 = LaggedStart(
            *[circle.animate.to_edge(RIGHT, buff=-2) for circle in self.circles],
            lag_ratio=0.2
        )
        self.play(animations1)
        self.play(animations2)
        # self.interactive_embed()

    def set_coords(self):
        rows = self.rows
        columns = self.columns
        width = self.width
        height = self.height
        x_step = width / columns
        y_step = height / rows
        x_coords = np.arange(-width / 2, width / 2 + x_step, x_step)
        y_coords = np.arange(-height / 2, height / 2 + y_step, y_step)
        self.x_coords = x_coords
        self.y_coords = y_coords

    def get_f(self, x, y):
        cir_data = [
            (c.get_center()[0], c.get_center()[1], c.radius) for c in self.circles
        ]
        return sum(
            [ri ** 2 / ((x - xi) ** 2 + (y - yi) ** 2) for xi, yi, ri in cir_data]
        )

    def get_fs(self):
        rows = self.rows + 1
        columns = self.columns + 1
        x_coords = self.x_coords
        y_coords = self.y_coords
        fs = np.array(
            [
                self.get_f(x_coords[j], y_coords[i])
                for i in range(rows)
                for j in range(columns)
            ]
        )
        return fs

    def update_mpoints(self, mob):
        rows = self.rows + 1
        columns = self.columns + 1
        fs = self.get_fs()
        fs = fs.reshape([rows, columns])
        lig_index = np.array(
            [(i, j) for i in range(rows) for j in range(columns) if fs[i, j] >= 1]
        )
        self.lig_index = lig_index
        self.fs = fs

    def get_corners(self, i, j):
        return [(i - 1, j - 1), (i - 1, j), (i, j), (i, j - 1)]

    def get_cor_f(self, i, j):
        ul = self.fs[i, j]
        ur = self.fs[i, j + 1]
        dr = self.fs[i + 1, j + 1]
        dl = self.fs[i + 1, j]
        n = 0
        for i, f in enumerate([ul, ur, dr, dl]):
            if f >= 1:
                n += 2 ** (3 - i)
        return n

    def update_boundary(self, mob):
        if not hasattr(self, "boundary"):
            setattr(self, "boundary", VGroup())
        else:
            self.remove(self.boundary)
        rows = self.rows + 1
        columns = self.columns + 1
        boundary = VGroup()
        corners = np.array([self.get_corners(i, j) for i, j in self.lig_index]).reshape(
            [-1, 2]
        )

        def get_line(start, end):
            return Line(start, end, stroke_width=1.5, color=BLUE)

        for i, j in corners:
            if i > (rows - 2) or i < 0 or j > (columns - 2) or j < 0:
                continue
            n = self.get_cor_f(i, j)
            l = None
            if n == 0:
                pass
            elif n == 1:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 2:
                start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 3:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 4:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 5:
                start1 = self.liner_interpolation((i, j), (i, j + 1))
                end1 = self.liner_interpolation((i, j), (i + 1, j))
                start2 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l1 = get_line(start1, end1)
                l2 = get_line(start2, end2)
                l = VGroup(l1, l2)
            elif n == 6:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 7:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j), (i + 1, j))
                l = get_line(start, end)
            elif n == 8:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j), (i + 1, j))
                l = get_line(start, end)
            elif n == 9:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 10:
                start1 = self.liner_interpolation((i, j), (i, j + 1))
                end1 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                start2 = self.liner_interpolation((i, j), (i + 1, j))
                end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l1 = get_line(start1, end1)
                l2 = get_line(start2, end2)
                l = VGroup(l1, l2)
            elif n == 11:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 12:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 13:
                start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            elif n == 14:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = get_line(start, end)
            else:
                pass
            if l is not None:
                boundary.add(l)

        points = boundary.get_all_points()
        if len(points) == 0:
            return
        lines = self.connect_close_points(points)
        self.boundary = lines
        self.boundary.set_fill(SIMPLE_BLUE, opacity=1)
        self.boundary.set_stroke(opacity=0)
        self.bring_to_back(self.boundary)

    def connect_close_points(self, points, distance=1):
        lines = VGroup()
        line = VGroup()
        line.append_points(points[:1])
        points = np.delete(points, 0, axis=0)
        while len(points) > 0:
            dist, idx = self.find_nearest_point(points, line.get_end())
            point = points[idx]
            if dist < distance:
                line.add_line_to(point)
            else:
                lines.add(line)
                line = VGroup()
                line.append_points([point])
            points = np.delete(points, idx, axis=0)
        lines.add(line)
        return lines

    def find_nearest_point(self, array, value):
        array = np.asarray(array)
        dist = np.abs(np.linalg.norm(array - value, axis=1))
        return dist.min(), dist.argmin()

    def liner_inter_func(self, s, t, n):
        if n == 0:
            sy = self.y_coords[s[n]]
            ty = self.y_coords[t[n]]
        else:
            sy = self.x_coords[s[n]]
            ty = self.x_coords[t[n]]
        fs = self.fs[s[0], s[1]]
        ft = self.fs[t[0], t[1]]
        return sy + (ty - sy) * (1 - fs) / (ft - fs)

    def liner_interpolation(self, s, t):
        if s[0] == t[0]:
            x = self.liner_inter_func(s, t, 1)
            y = self.y_coords[s[0]]
        elif s[1] == t[1]:
            x = self.x_coords[s[1]]
            y = self.liner_inter_func(s, t, 0)
        return np.array([x, y, 0])
