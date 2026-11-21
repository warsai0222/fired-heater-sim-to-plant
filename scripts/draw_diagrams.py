"""Generate the H-101 PFD and P&ID sheets (Rev B: balanced draft + regenerative APH) as SVG (A3 landscape).

    python3 scripts/draw_diagrams.py          -> docs/diagrams/*.svg

Numbers and tags come from design/heater_design_reference.md and design/tag_register.csv.
Symbols follow ISA-5.1 conventions loosely (see the legend on each P&ID sheet).
Preliminary, for review: not for construction.
"""
from pathlib import Path

W, H = 1680, 1188  # A3 landscape, 0.25 mm per unit
OUT = Path(__file__).resolve().parent.parent / "docs" / "diagrams"

STYLE = """
<style>
 text{font-family:Arial,Helvetica,sans-serif;fill:#111}
 .t8{font-size:8px}.t9{font-size:9px}.t10{font-size:10px}.t11{font-size:11px}.t12{font-size:12px}
 .t14{font-size:14px}.t16{font-size:16px}.t20{font-size:20px}.b{font-weight:bold}.i{font-style:italic}
 .proc{stroke:#000;stroke-width:2.4;fill:none}
 .fuel{stroke:#000;stroke-width:1.8;fill:none}
 .util{stroke:#000;stroke-width:1.4;fill:none}
 .flue{stroke:#666;stroke-width:1.6;fill:none;stroke-dasharray:10 4}
 .sig{stroke:#000;stroke-width:1;fill:none;stroke-dasharray:6 3}
 .thin{stroke:#000;stroke-width:1;fill:none}
 .eq{stroke:#000;stroke-width:2;fill:#fff}
 .refr{stroke:#000;stroke-width:2;fill:#f3efe9}
 .box{stroke:#000;stroke-width:1;fill:#fff}
 .grid{stroke:#999;stroke-width:.6}
 .flame{stroke:#c0392b;stroke-width:1.4;fill:#f9d6c4}
 .tube{stroke:#333;stroke-width:1;fill:#fff}
 .hdr{fill:#e6eef4}
 .red{fill:#b03a2e}
</style>
<defs>
 <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker>
 <marker id="arg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M0,0 L10,5 L0,10 z" fill="#666"/></marker>
</defs>
"""


class Sheet:
    def __init__(self):
        self.e = []

    def add(self, s):
        self.e.append(s)

    # --- primitives -------------------------------------------------------
    def line(self, pts, cls="proc", arrow=False, grey=False):
        p = " ".join(f"{x},{y}" for x, y in pts)
        m = f' marker-end="url(#{"arg" if grey else "ar"})"' if arrow else ""
        self.add(f'<polyline points="{p}" class="{cls}"{m}/>')

    def text(self, x, y, s, cls="t10", anchor="start", rot=None):
        r = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
        s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        self.add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{r}>{s}</text>')

    def rect(self, x, y, w, h, cls="eq", rx=0):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>')

    def poly(self, pts, cls="eq"):
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.add(f'<polygon points="{p}" class="{cls}"/>')

    def circle(self, x, y, r, cls="tube"):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>')

    # --- ISA-style symbols ------------------------------------------------
    def bubble(self, x, y, letters, number, kind="field", r=19):
        """kind: field (plain circle), dcs (circle in square), sis (diamond in square)."""
        if kind == "dcs":
            self.rect(x - r, y - r, 2 * r, 2 * r, "box")
        if kind == "sis":
            self.rect(x - r, y - r, 2 * r, 2 * r, "box")
            self.poly([(x, y - r), (x + r, y), (x, y + r), (x - r, y)], "box")
        else:
            self.circle(x, y, r, "box")
        if kind == "dcs":
            self.line([(x - r, y), (x + r, y)], "thin")
        else:
            self.line([(x - r + 3, y), (x + r - 3, y)], "thin")
        fs = "t9" if len(number) > 4 else "t10"
        self.text(x, y - 4, letters, "t10 b", "middle")
        self.text(x, y + 12, number, fs, "middle")

    def valve(self, x, y, vertical=False, s=9, fill="#fff"):
        if vertical:
            self.poly([(x - s, y - s), (x + s, y - s), (x - s, y + s), (x + s, y + s)], "box")
        else:
            self.poly([(x - s, y - s), (x + s, y + s), (x + s, y - s), (x - s, y + s)], "box")
        if fill != "#fff":
            self.add(f'<circle cx="{x}" cy="{y}" r="2" fill="{fill}"/>')

    def control_valve(self, x, y, tag=None, fail=None, vertical=False, label_dy=-42):
        self.valve(x, y, vertical)
        if vertical:
            self.line([(x, y), (x + 20, y)], "thin")
            self.add(f'<path d="M{x+20},{y-10} A10,10 0 0,1 {x+20},{y+10} z" class="box"/>')
            if tag:
                self.text(x + 36, y + 4, tag, "t10 b")
            if fail:
                self.text(x + 36, y + 16, fail, "t9")
        else:
            self.line([(x, y), (x, y - 20)], "thin")
            self.add(f'<path d="M{x-11},{y-20} A11,11 0 0,1 {x+11},{y-20} z" class="box"/>')
            if tag:
                self.text(x, y + label_dy, tag, "t10 b", "middle")
            if fail:
                self.text(x, y + 22, fail, "t9", "middle")

    def onoff_valve(self, x, y, tag=None, fail=None, vertical=False):
        self.valve(x, y, vertical)
        if vertical:
            self.line([(x, y), (x + 18, y)], "thin")
            self.rect(x + 18, y - 8, 16, 16, "box")
            self.text(x + 26, y + 4, "S", "t9", "middle")
            if tag:
                self.text(x + 40, y + 4, tag, "t10 b")
            if fail:
                self.text(x + 40, y + 16, fail, "t9")
        else:
            self.line([(x, y), (x, y - 18)], "thin")
            self.rect(x - 8, y - 34, 16, 16, "box")
            self.text(x, y - 22, "S", "t9", "middle")
            if tag:
                self.text(x, y - 40, tag, "t10 b", "middle")
            if fail:
                self.text(x, y + 22, fail, "t9", "middle")

    def orifice(self, x, y):
        self.line([(x - 3, y - 11), (x - 3, y + 11)], "thin")
        self.line([(x + 3, y - 11), (x + 3, y + 11)], "thin")

    def blind(self, x, y, vertical=False):
        if vertical:
            self.circle(x - 6, y, 5, "box")
            self.add(f'<circle cx="{x+6}" cy="{y}" r="5" fill="#000"/>')
            self.line([(x - 1, y), (x + 1, y)], "thin")
        else:
            self.circle(x, y - 6, 5, "box")
            self.add(f'<circle cx="{x}" cy="{y+6}" r="5" fill="#000"/>')

    def stream(self, x, y, n):
        self.poly([(x, y - 11), (x + 13, y), (x, y + 11), (x - 13, y)], "box")
        self.text(x, y + 4, str(n), "t9 b", "middle")

    def offsheet(self, x, y, label, sub="", direction="right", w=150):
        h = 26
        if direction == "right":
            pts = [(x, y - h / 2), (x + w - 14, y - h / 2), (x + w, y), (x + w - 14, y + h / 2), (x, y + h / 2)]
            tx = x + 6
        else:
            pts = [(x + 14, y - h / 2), (x + w, y - h / 2), (x + w, y + h / 2), (x + 14, y + h / 2), (x, y)]
            tx = x + 18
        self.poly(pts, "box")
        self.text(tx, y - 1, label, "t9 b")
        if sub:
            self.text(tx, y + 10, sub, "t8")

    def sig(self, pts):
        self.line(pts, "sig")

    def frame(self, title, dwg, rev, sheet):
        self.rect(10, 10, W - 20, H - 20, "thin")
        self.rect(16, 16, W - 32, H - 32, "thin")
        x, y, w = 1110, 1012, 554
        self.rect(x, y, w, 160, "box")
        rows = [(1040, "DEMO REFINERY — UNIT 100 CRUDE DISTILLATION", "t12 b"),
                (1064, title, "t14 b"),
                (1088, f"Drawing No. {dwg}     Rev {rev}     Sheet {sheet}", "t11"),
                (1108, "Status: PRELIMINARY — FOR REVIEW (not for construction)", "t11 b red"),
                (1128, "Basis: design/heater_design_reference.md, design/tag_register.csv", "t9"),
                (1142, "Proposal §5 design basis (ASSUMED values, pending ChemE review)", "t9"),
                (1158, "Date 2026-11-20   |   Synthetic demo project — fictional plant", "t9")]
        for ty, s, c in rows:
            self.text(x + 12, ty, s, c)
        for ty in (1048, 1072, 1094, 1114):
            self.line([(x, ty), (x + w, ty)], "grid")

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="420mm" height="297mm">'
                + STYLE + '<rect width="100%" height="100%" fill="#fff"/>' + "\n".join(self.e) + "</svg>")


def heater_shell(s, x0, stack_top, scale=1.0, conv_rows=6, rad_tubes=True):
    """Draws stack, convection, hood, radiant box, floor and plenum. Returns key coordinates."""
    g = {}
    cx = x0 + 210          # heater centreline
    sw, cw, rw = 50, 270, 420
    st_y0, st_y1 = stack_top, stack_top + 150
    cv_y0, cv_y1 = st_y1 + 50, st_y1 + 180
    rd_y0, rd_y1 = cv_y1 + 40, cv_y1 + 280
    g.update(cx=cx, st=(cx - sw / 2, st_y0, cx + sw / 2, st_y1), cv=(cx - cw / 2, cv_y0, cx + cw / 2, cv_y1),
             rd=(cx - rw / 2, rd_y0, cx + rw / 2, rd_y1))
    # stack
    s.rect(cx - sw / 2, st_y0, sw, st_y1 - st_y0, "refr")
    s.poly([(cx - sw / 2, st_y1), (cx + sw / 2, st_y1), (cx + cw / 2, cv_y0), (cx - cw / 2, cv_y0)], "refr")
    # convection
    s.rect(cx - cw / 2, cv_y0, cw, cv_y1 - cv_y0, "refr")
    for r in range(conv_rows):
        yy = cv_y0 + 18 + r * ((cv_y1 - cv_y0 - 30) / (conv_rows - 1))
        for k in range(10):
            xx = cx - cw / 2 + 22 + k * ((cw - 44) / 9)
            if r < conv_rows - 2:   # studded rows
                s.circle(xx, yy, 7, "tube")
                s.circle(xx, yy, 3.5, "tube")
            else:                   # bare shield rows
                s.circle(xx, yy, 6, "tube")
    # hood
    s.poly([(cx - cw / 2, cv_y1), (cx + cw / 2, cv_y1), (cx + rw / 2, rd_y0), (cx - rw / 2, rd_y0)], "refr")
    # radiant box
    s.rect(cx - rw / 2, rd_y0, rw, rd_y1 - rd_y0, "refr")
    s.rect(cx - rw / 2 + 12, rd_y0 + 8, rw - 24, rd_y1 - rd_y0 - 8, "box")
    if rad_tubes:
        for k in range(18):
            yy = rd_y0 + 22 + k * 12.5
            s.circle(cx - rw / 2 + 26, yy, 5, "tube")
            s.circle(cx + rw / 2 - 26, yy, 5, "tube")
    # floor, burners, plenum, legs
    s.rect(cx - rw / 2, rd_y1, rw, 14, "refr")
    bx = [cx - rw / 2 + 52 + i * ((rw - 104) / 7) for i in range(8)]
    for i, x in enumerate(bx):
        s.add(f'<path d="M{x-9},{rd_y1} Q{x-8},{rd_y1-40} {x},{rd_y1-70} Q{x+8},{rd_y1-40} {x+9},{rd_y1} z" class="flame"/>')
        s.rect(x - 7, rd_y1 + 2, 14, 10, "box")
    s.rect(cx - rw / 2 + 20, rd_y1 + 14, rw - 40, 32, "box")
    for xl in (cx - rw / 2 + 30, cx + rw / 2 - 30):
        s.line([(xl, rd_y1 + 46), (xl, rd_y1 + 80)], "util")
    g.update(burners=bx, floor=rd_y1, plenum=(cx - rw / 2 + 20, rd_y1 + 14, cx + rw / 2 - 20, rd_y1 + 46))
    return g


# =====================================================================================
# Rev B helpers: fan, regenerative APH, damper
# =====================================================================================
def fan(s, x, y, tag, sub="", r=22, label_dy=38):
    s.circle(x, y, r, "box")
    s.add(f'<path d="M{x-r*0.55},{y+r*0.6} L{x+r*0.85},{y-r*0.2} M{x-r*0.55},{y-r*0.6} L{x+r*0.85},{y+r*0.2}" class="thin"/>')
    s.text(x, y + label_dy, tag, "t10 b", "middle")
    if sub:
        s.text(x, y + label_dy + 12, sub, "t8", "middle")


def aph(s, x0, y0, w=120, h=150, gas_right=True, label=True):
    """Regenerative APH: rectangle split into gas and air halves, hatched rotor band."""
    s.rect(x0, y0, w, h, "eq")
    s.line([(x0 + w / 2, y0), (x0 + w / 2, y0 + h)], "thin")
    for k in range(9):
        yy = y0 + 30 + k * ((h - 60) / 8)
        s.line([(x0 + 4, yy), (x0 + w - 4, yy - 10)], "grid")
    s.rect(x0 - 6, y0 + 28, w + 12, h - 56, "thin")
    g, a = ("GAS", "AIR") if gas_right else ("AIR", "GAS")
    s.text(x0 + w * 0.25, y0 + 14, a if gas_right else g, "t8 b", "middle")
    s.text(x0 + w * 0.75, y0 + 14, g if gas_right else a, "t8 b", "middle")
    if label:
        s.text(x0 + w / 2, y0 + h + 16, "E-102", "t11 b", "middle")
        s.text(x0 + w / 2, y0 + h + 28, "regenerative APH (rotor)", "t8", "middle")


def damper(s, x, y, vertical_duct=True, tag=None, sub=None, side="right"):
    if vertical_duct:
        s.line([(x - 14, y + 7), (x + 14, y - 7)], "proc")
    else:
        s.line([(x - 7, y - 14), (x + 7, y + 14)], "proc")
    s.add(f'<circle cx="{x}" cy="{y}" r="3" fill="#000"/>')
    if tag:
        tx = x + 22 if side == "right" else x - 22
        an = "start" if side == "right" else "end"
        s.text(tx, y - 2, tag, "t9 b", an)
        if sub:
            s.text(tx, y + 10, sub, "t8", an)


# =====================================================================================
# PFD (Rev B — balanced draft + regenerative APH)
# =====================================================================================
def draw_pfd():
    s = Sheet()
    s.frame("PROCESS FLOW DIAGRAM — H-101 CRUDE CHARGE HEATER", "U100-PFD-001", "B", "1 of 1")
    g = heater_shell(s, 620, 60)
    cx = g["cx"]
    cvx0, cvy0, cvx1, cvy1 = g["cv"]
    rdx0, rdy0, rdx1, rdy1 = g["rd"]
    stx0, sty0, stx1, sty1 = g["st"]
    px0, py0, px1, py1 = g["plenum"]

    s.text(stx0 - 10, sty0 + 14, "S-101 STACK", "t11 b", "end")
    yd = sty1 - 40
    damper(s, cx, yd, tag=None)
    s.text(stx0 - 10, yd - 2, "D-101 bypass damper", "t9 b", "end")
    s.text(stx0 - 10, yd + 10, "closed; opens on fan trip (FO)", "t8", "end")
    s.text(cvx1 + 8, cvy0 + 14, "CONVECTION", "t10 b")
    s.text(cvx1 + 8, cvy0 + 27, "studded + 2 shield rows", "t8")
    s.text(cvx1 + 8, cvy0 + 38, "SB-101A–F soot blowers", "t8")
    s.text(cx - 20, rdy0 + 40, "RADIANT SECTION (cabin)", "t11 b", "middle")
    s.text(cx - 20, rdy0 + 56, "80 tubes, 6\" Sch 40 A335 P9, 4 passes x 20", "t9", "middle")
    s.text(cx - 20, rdy0 + 69, "avg flux ≈ 34 kW/m², area ≈ 766 m²", "t9", "middle")
    s.text(cx - 20, rdy0 + 82, "bridgewall ≈ 845 °C (760–900)", "t9", "middle")
    s.text(cx, rdy1 - 82, "B-101A–H: 8 forced-draft gas burners (floor-fired)", "t9", "middle")
    s.text(px0 - 8, py0 + 14, "hot-air", "t9", "end")
    s.text(px0 - 8, py0 + 26, "windbox", "t9", "end")
    # emergency air doors D-102
    s.rect(px0 + 30, py1, 26, 8, "box")
    s.text(px0 + 24, py1 + 20, "D-102 emergency air doors (FO)", "t8", "end")

    # equipment summary box
    s.rect(30, 30, 430, 132, "box")
    s.rect(30, 30, 430, 20, "hdr")
    s.text(40, 45, "H-101 CRUDE CHARGE HEATER — DESIGN CASE (as-new, clean)", "t10 b")
    for k, row in enumerate([
        "Crude: Alaska North Slope, 50,000 bbl/d (286 t/h), 250 → 360 °C",
        "Absorbed 35.0 MW (radiant ≈ 26 / convection ≈ 9); APH duty ≈ 4.3 MW",
        "Fired 38.5 MW LHV, efficiency ≈ 91 % LHV, stack ≈ 155 °C",
        "Balanced draft: FD fan K-101 + ID fan K-102 (VFDs); arch −2.5 mmH2O",
        "Excess O2 3.0 % dry at arch (15 % excess air); hot air ≈ 300 °C",
        "TMT limit 600 °C; coil ΔP clean ≈ 6.0 bar/pass, limit 8.4 bar",
        "Fan trip → natural-draft runback ≤ 60 % firing; decoke by pigging ≈ 4 d"]):
        s.text(40, 66 + k * 14, row, "t10")

    # --- crude feed ----------------------------------------------------------------
    yc = cvy0 + 20
    s.offsheet(24, yc, "FROM PREHEAT TRAIN", "E-101 hot end / P-101A/B", "right", 160)
    s.line([(184, yc), (cvx0, yc)], "proc", arrow=True)
    s.stream(225, yc, 1)
    s.control_valve(330, yc, "FV-1101..1104", "4 pass flow valves (FO)")
    s.bubble(330, yc - 82, "FIC", "1101-04", "dcs")
    s.sig([(330, yc - 63), (330, yc - 52)])
    s.stream(420, yc, "2")
    s.text(440, yc - 8, "4 passes (A–D), 71.5 t/h each", "t9")
    for d in (-3, 3):
        s.line([(470 + d, yc - 7), (480 + d, yc + 7)], "thin")
    xo = cvx1 + 100
    s.line([(cvx1, cvy1 - 16), (xo, cvy1 - 16), (xo, rdy0 + 22), (rdx1 - 26, rdy0 + 22)], "proc", arrow=True)
    s.stream(xo, cvy1 + 20, 3)
    s.text(xo - 6, cvy1 - 22, "≈ 292 °C", "t9", "end")
    # outlet / transfer line
    yo = rdy1 - 20
    col_x = 1575
    s.line([(rdx1 - 26, yo), (col_x - 60, yo), (col_x - 60, 520), (col_x - 30, 520)], "proc", arrow=True)
    s.stream(rdx1 + 40, yo, 4)
    s.stream(col_x - 60, 600, 5)
    xt = 1460
    s.add(f'<circle cx="{xt}" cy="{yo}" r="3" fill="#000"/>')
    s.bubble(xt, yo - 58, "TIC", "1110", "dcs")
    s.line([(xt, yo - 39), (xt, yo)], "thin")
    s.text(rdx1 + 60, yo + 16, "transfer line 360 °C, 2.5 barg (V+L)", "t9")
    s.rect(col_x - 30, 230, 70, 560, "eq", rx=30)
    for yy in range(270, 760, 32):
        s.line([(col_x - 30, yy), (col_x + 20, yy)], "thin")
    s.text(col_x + 5, 215, "C-101", "t11 b", "middle")
    s.text(col_x + 5, 810, "ATMOSPHERIC COLUMN", "t9", "middle")
    s.text(col_x + 5, 822, "(boundary)", "t9", "middle")
    s.text(col_x - 26, 512, "flash zone", "t8")

    # --- flue gas: radiant → convection → offtake → APH → ID fan → stack ---------------
    s.line([(cx + 150, rdy0 + 110), (cx + 150, rdy0 - 6)], "flue", arrow=True, grey=True)
    s.stream(cx + 150, rdy0 + 128, 11)
    ax0, ay0, aw, ah = 1200, 290, 120, 150
    aph(s, ax0, ay0, aw, ah, gas_right=True)
    gx, axx = ax0 + 90, ax0 + 30          # gas-side and air-side centrelines
    yoff = yd + 18
    s.line([(stx1, yoff), (gx, yoff), (gx, ay0)], "flue", arrow=True, grey=True)
    s.stream(gx - 120, yoff, 12)
    s.text(stx1 + 8, yoff - 6, "flue ≈ 390 °C", "t9")
    idx, idy = 1350, ay0 + ah + 40
    s.line([(gx, ay0 + ah), (gx, idy), (idx - 22, idy)], "flue", arrow=True, grey=True)
    fan(s, idx, idy, "K-102 ID FAN", "VFD, ≈ 40 kW", label_dy=36)
    yret = sty0 + 70
    s.line([(idx + 22, idy), (1400, idy), (1400, yret), (stx1, yret)], "flue", arrow=True, grey=True)
    s.stream(1400, ay0 + 90, 13)
    s.stream(1100, yret, 14)
    s.text(1395, yret - 8, "≈ 155 °C to stack", "t9", "end")
    s.line([(cx, sty0 + 50), (cx, sty0 - 2)], "flue", arrow=True, grey=True)
    s.text(stx1 + 8, sty0 + 14, "to atmosphere", "t9")
    s.bubble(1362, ay0 + ah - 40, "TIC", "1345", "dcs")
    s.line([(1343, ay0 + ah - 34), (gx, ay0 + ah + 18)], "thin")
    s.text(1362, ay0 + ah - 66, "≥ 140 °C", "t8", "middle")
    s.bubble(idx, idy + 86, "PIC", "1311", "dcs")
    s.sig([(idx, idy + 67), (idx, idy + 22)])
    s.text(idx + 24, idy + 90, "arch draft", "t8")

    # --- air: ambient → FD fan → APH air side → hot air → windbox ----------------------
    fdx, fdy = axx, ay0 + ah + 130
    s.line([(1150, fdy), (fdx - 22, fdy)], "util", arrow=True)
    s.stream(1185, fdy + 18, 8)
    s.text(1150, fdy - 6, "ambient", "t8")
    fan(s, fdx, fdy, "K-101 FD FAN", "VFD, ≈ 30 kW", label_dy=36)
    s.line([(fdx, fdy - 22), (fdx, ay0 + ah)], "util", arrow=True)
    s.stream(fdx, ay0 + ah + 40, 9)
    yh = ay0 - 30
    xh = 1120
    s.line([(axx, ay0), (axx, yh), (xh, yh), (xh, (py0 + py1) / 2), (px1, (py0 + py1) / 2)], "util", arrow=True)
    s.stream(xh, 520, 10)
    s.text(xh + 8, yh - 6, "hot air ≈ 300 °C", "t9")
    s.bubble(1170, fdy - 56, "FIC", "1341", "dcs")
    s.sig([(1189, fdy - 56), (fdx - 14, fdy - 16)])
    xa = rdx0 - 115
    s.bubble(xa, rdy0 + 36, "AIC", "1321", "dcs")
    s.line([(xa + 19, rdy0 + 36), (rdx0 + 4, rdy0 + 36)], "thin")
    s.text(xa, rdy0 + 8, "arch O2 (dry)", "t9", "middle")
    s.sig([(xa, rdy0 + 55), (xa, py1 + 36), (1170, py1 + 36), (1170, fdy - 37)])
    s.text(720, py1 + 32, "AIC-1321 → FIC-1341 (O2 → combustion air → FD fan speed)", "t8")
    s.text(rdx0 - 12, rdy0 + 196, "tramp air", "t9 i", "end")
    s.text(rdx0 - 12, rdy0 + 208, "(leakage, Type B)", "t9 i", "end")
    s.line([(rdx0 - 44, rdy0 + 218), (rdx0 - 2, rdy0 + 218)], "util", arrow=True)

    # --- fuel gas --------------------------------------------------------------------
    yf = py1 + 50
    s.offsheet(24, yf + 30, "REFINERY FUEL GAS", "header ≈ 4.5 barg", "right", 160)
    s.line([(184, yf + 30), (215, yf + 30)], "fuel", arrow=True)
    s.rect(215, yf - 30, 50, 110, "eq", rx=22)
    s.text(278, yf + 50, "V-101", "t11 b")
    s.text(278, yf + 62, "FG KO drum", "t9")
    s.line([(265, yf - 10), (300, yf - 10), (300, yf), (g["burners"][-1], yf)], "fuel")
    s.stream(345, yf, 6)
    s.control_valve(420, yf, "PV-1202", "FC")
    s.bubble(420, yf - 82, "PIC", "1202", "dcs")
    s.sig([(420, yf - 63), (420, yf - 52)])
    s.onoff_valve(500, yf, "XV-1201/1202", "SIS double block")
    for x in g["burners"]:
        s.line([(x, yf), (x, py1 - 30)], "fuel")
    s.text(g["burners"][0] - 10, yf + 16, "burner manifold 1.2 barg, 2,860 kg/h, LHV 48.5 MJ/kg", "t9")
    s.sig([(xt, yo - 77), (xt, yo - 100), (1350, yo - 100), (1350, yf + 36), (440, yf + 36), (440, yf - 82), (439, yf - 82)])
    s.text(1080, yf + 32, "COT → fuel-gas pressure cascade", "t8")
    s.offsheet(24, yf + 64, "PILOT GAS", "0.7 barg", "right", 160)
    s.line([(184, yf + 64), (g["burners"][0] - 30, yf + 64)], "util", arrow=True)
    s.stream(560, yf + 64, 7)
    s.text(g["burners"][0] - 26, yf + 68, "to pilots B-101A–H", "t9")

    # --- LP steam ---------------------------------------------------------------------
    ysl = cvy0 + 90
    s.offsheet(24, ysl, "LP STEAM 3.5 barg", "", "right", 160)
    s.line([(184, ysl), (cvx0, ysl)], "util", arrow=True)
    s.stream(cvx0 - 40, ysl, 16)
    s.text(cvx0 - 56, ysl - 8, "soot blowing (+ SB-102A/B on APH)", "t9", "end")
    s.line([(cvx0 - 120, ysl), (cvx0 - 120, rdy0 + 150), (rdx0, rdy0 + 150)], "util", arrow=True)
    s.stream(cvx0 - 120, rdy0 + 110, 15)
    s.text(rdx0 - 6, rdy0 + 142, "snuffing / purge", "t9", "end")

    # --- stream table ---------------------------------------------------------------
    tx, ty = 30, 878
    cols = [("No.", 30), ("Stream", 250), ("Phase", 40), ("Mass flow", 84), ("T °C", 46), ("Pressure", 98),
            ("Notes", 520)]
    rows = [
        ("1", "Crude from preheat train", "L", "286 t/h", "250", "11.0 barg", "ANS, API 32.3; 4 pass flow valves FV-1101..1104"),
        ("2", "Pass inlets A–D", "L", "4 x 71.5 t/h", "250", "8.5 barg", "≈ 1.6 m/s, G ≈ 1,065 kg/m²s"),
        ("3", "Crossover (convection → radiant)", "L", "4 x 71.5 t/h", "≈ 292", "≈ 7.8 barg", "TT-1131..1134"),
        ("4", "Pass outlets A–D", "V+L", "4 x 71.5 t/h", "360", "≈ 2.6 barg", "TT-1111..1114; coil ΔP clean ≈ 6.0 bar"),
        ("5", "Transfer line to C-101", "V+L", "286 t/h", "360", "2.5 barg", "vapor fraction from model (TBP); sets C-101 flash-zone vaporization / cuts"),
        ("6", "Fuel gas to burners", "V", "2,860 kg/h", "40", "1.2 barg", "80 CH4/8 C2H6/2 C3H8/8 H2/2 N2 mol%, 48.5 MJ/kg"),
        ("7", "Pilot gas", "V", "≈ 25 kg/h", "40", "0.7 barg", "continuous pilots"),
        ("8", "Ambient air to FD fan", "V", "57,850 kg/h", "25", "atm", "FIC-1341"),
        ("9", "Cold air to APH", "V", "57,850 kg/h", "≈ 30", "+130 mmH2O", "cold-air bypass TV-1345 (closed at design)"),
        ("10", "Hot air to windbox", "V", "54,370 kg/h", "≈ 300", "+60 mmH2O", "15 % excess air; ≈ 6 % of FD air leaks to gas side in APH"),
        ("11", "Flue gas at bridgewall", "V", "57,230 kg/h", "≈ 845", "−2.5 mmH2O", "wet mol%: CO2 8.4, H2O 16.6, O2 2.5, N2 72.5"),
        ("12", "Flue gas, convection outlet → APH", "V", "57,230 kg/h", "≈ 390", "−20 mmH2O", "TT-1303, AT-1327"),
        ("13", "Flue gas, APH → ID fan", "V", "60,700 kg/h", "≈ 150", "−120 mmH2O", "includes APH leak air; TIC-1345 ≥ 140 °C"),
        ("14", "Flue gas, ID fan → stack", "V", "60,700 kg/h", "≈ 155", "+15 mmH2O", "stack CEMS AT-1326 (O2) / AT-1325 (NOx)"),
        ("15", "LP steam — snuffing / purge", "V", "intermittent", "150", "3.5 barg", "XV-1401 firebox, HV-1402 header boxes"),
        ("16", "LP steam — soot blowing", "V", "intermittent", "150", "3.5 barg", "SB-101A–F convection, SB-102A/B APH"),
    ]
    rh = 13
    tw = sum(w for _, w in cols)
    s.rect(tx, ty - 14, tw, rh * (len(rows) + 1) + 2, "box")
    s.rect(tx, ty - 14, tw, rh, "hdr")
    s.text(tx, ty - 19, "STREAM TABLE — design case Rev B (preliminary hand balance; physics model recomputes)", "t10 b")
    x = tx
    for name, w in cols:
        s.text(x + 4, ty - 4, name, "t8 b")
        x += w
        s.line([(x, ty - 14), (x, ty - 14 + rh * (len(rows) + 1) + 2)], "grid")
    for i, r in enumerate(rows):
        y = ty + 9 + i * rh
        s.line([(tx, y - 9), (tx + tw, y - 9)], "grid")
        x = tx
        for (name, w), v in zip(cols, r):
            s.text(x + 4, y, v, "t8")
            x += w
    return s


# =====================================================================================
# P&ID sheet 2 — combustion, fuel gas, burners, BMS (Rev B)
# =====================================================================================
def draw_pid2():
    s = Sheet()
    s.frame("P&ID — H-101 COMBUSTION, FUEL GAS, BURNERS & BMS", "U100-PID-102", "B", "2 of 3")
    s.text(30, 40, "P&ID U100-PID-102 — H-101 COMBUSTION, FUEL GAS, BURNERS, ANALYZERS & BMS", "t16 b")
    g = heater_shell(s, 690, 60)
    cx = g["cx"]
    cvx0, cvy0, cvx1, cvy1 = g["cv"]
    rdx0, rdy0, rdx1, rdy1 = g["rd"]
    stx0, sty0, stx1, sty1 = g["st"]
    px0, py0, px1, py1 = g["plenum"]
    s.text(cx, rdy0 + 60, "H-101 RADIANT SECTION", "t11 b", "middle")
    s.text(cx, rdy0 + 74, "(process coil on U100-PID-101)", "t9", "middle")
    s.text(stx0 - 8, sty0 + 14, "S-101", "t11 b", "end")
    s.line([(cx, sty0 + 40), (cx, sty0 - 2)], "flue", arrow=True, grey=True)

    # --- stack: bypass damper, offtake to APH, return from ID fan, CEMS --------------
    yd = sty1 - 40
    damper(s, cx, yd)
    s.line([(stx0, yd), (stx0 - 30, yd)], "thin")
    s.rect(stx0 - 46, yd - 8, 16, 16, "box")
    s.text(stx0 - 38, yd + 4, "S", "t9", "middle")
    s.text(stx0 - 52, yd - 2, "XV-1361 (D-101)", "t10 b", "end")
    s.text(stx0 - 52, yd + 10, "bypass damper, FO", "t9", "end")
    s.bubble(stx0 - 38, yd - 52, "ZT", "1361")
    s.line([(stx0 - 38, yd - 33), (stx0 - 38, yd - 8)], "thin")
    yoff = yd + 18
    s.line([(stx1, yoff), (stx1 + 150, yoff)], "flue", arrow=True, grey=True)
    s.offsheet(stx1 + 150, yoff, "TO E-102 APH", "U100-PID-103", "right", 130)
    yret = sty0 + 70
    s.offsheet(stx1 + 150, yret, "FROM K-102 ID FAN", "U100-PID-103", "left", 140)
    s.line([(stx1 + 150, yret), (stx1, yret)], "flue", arrow=True, grey=True)
    s.bubble(stx1 + 60, sty0 + 22, "AT", "1326")
    s.line([(stx1 + 41, sty0 + 22), (stx1, sty0 + 22)], "thin")
    s.bubble(stx1 + 110, sty0 + 22, "AT", "1325")
    s.line([(stx1 + 91, sty0 + 22), (stx1 + 79, sty0 + 22)], "thin")
    s.text(stx1 + 136, sty0 + 18, "stack CEMS", "t9")
    s.text(stx1 + 136, sty0 + 30, "O2 (dry) / NOx", "t9")
    # convection outlet instruments
    s.bubble(cvx1 + 70, cvy0 - 6, "TT", "1303")
    s.line([(cvx1 + 51, cvy0 - 6), (cvx1 - 30, cvy0 - 6)], "thin")
    s.bubble(cvx1 + 120, cvy0 - 6, "AT", "1327")
    s.line([(cvx1 + 101, cvy0 - 6), (cvx1 + 89, cvy0 - 6)], "thin")
    s.bubble(cvx1 + 170, cvy0 - 6, "PT", "1313")
    s.line([(cvx1 + 151, cvy0 - 6), (cvx1 + 139, cvy0 - 6)], "thin")
    s.text(cvx1 + 70, cvy0 + 26, "convection outlet ≈ 390 °C, O2 ≈ 3.2 %, −20 mmH2O", "t8")
    # convection
    s.bubble(cvx1 + 70, cvy1 - 40, "TT", "1302")
    s.line([(cvx1 + 51, cvy1 - 40), (cvx1, cvy1 - 40)], "thin")
    for k in range(6):
        yy = cvy0 + 16 + k * 20
        s.rect(cvx0 - 26, yy - 6, 22, 12, "box")
        s.text(cvx0 - 30, yy + 4, f"SB-101{'ABCDEF'[k]}", "t8", "end")
    s.line([(cvx0 - 15, cvy0 + 10), (cvx0 - 15, cvy0 + 116)], "util")

    # --- radiant: bridgewall, arch analyzers, draft, firebox pressure trip -------------
    xi = rdx1 + 75
    for L, N, kind, yy in [("TT", "1301B", "field", rdy0 + 30), ("AT", "1322", "field", rdy0 + 82),
                           ("AIC", "1321", "dcs", rdy0 + 140), ("PIC", "1311", "dcs", rdy0 + 200)]:
        s.bubble(xi, yy, L, N, kind)
        s.line([(xi - 19, yy), (rdx1, yy)], "thin")
    s.text(xi + 26, rdy0 + 34, "bridgewall ≈ 845 °C (760–900)", "t9")
    s.text(xi + 26, rdy0 + 86, "arch CO  Hi 200 / HH 1000 ppm", "t9")
    s.text(xi + 26, rdy0 + 130, "arch O2 dry, SP 3.0 % (Type A decision)", "t9")
    s.sig([(xi + 19, rdy0 + 140), (xi + 200, rdy0 + 140)])
    s.offsheet(xi + 200, rdy0 + 140, "TO FIC-1341 (FD fan)", "U100-PID-103", "right", 160)
    s.text(xi + 26, rdy0 + 190, "arch draft SP −2.5 mmH2O", "t9")
    s.sig([(xi + 19, rdy0 + 200), (xi + 200, rdy0 + 200)])
    s.offsheet(xi + 200, rdy0 + 200, "TO SC-1351 (ID fan)", "U100-PID-103", "right", 160)
    s.bubble(rdx0 - 50, rdy0 + 40, "TT", "1301A")
    s.line([(rdx0 - 31, rdy0 + 40), (rdx0, rdy0 + 40)], "thin")
    s.bubble(rdx0 - 50, rdy0 + 120, "PT", "1314", "sis")
    s.line([(rdx0 - 31, rdy0 + 120), (rdx0, rdy0 + 120)], "thin")
    s.text(rdx0 - 76, rdy0 + 116, "firebox HH +10 mmH2O", "t8", "end")
    s.text(rdx0 - 76, rdy0 + 127, "→ I-101 main fuel trip", "t8", "end")
    s.bubble(rdx0 - 50, rdy1 - 50, "PT", "1312")
    s.line([(rdx0 - 31, rdy1 - 50), (rdx0, rdy1 - 50)], "thin")
    s.text(rdx0 - 76, rdy1 - 46, "floor draft", "t9", "end")

    # --- windbox: hot air in, emergency air doors, windbox pressure -------------------
    ya = (py0 + py1) / 2
    s.offsheet(px1 + 70, ya, "HOT AIR FROM E-102", "PID-103, ≈ 300 °C", "left", 130)
    s.line([(px1 + 70, ya), (px1, ya)], "util", arrow=True)
    s.bubble(px1 + 150, ya - 50, "PT", "1342")
    s.line([(px1 + 136, ya - 37), (px1 + 30, ya)], "thin")
    s.text(px1 + 172, ya - 46, "windbox +60 mmH2O", "t8")
    xe = px1 - 15
    s.line([(xe, py1 + 74), (xe, py1)], "util", arrow=True)
    s.onoff_valve(xe, py1 + 36, None, None, vertical=True)
    s.text(xe + 20, py1 + 88, "XV-1362 (D-102) emergency", "t9 b")
    s.text(xe + 20, py1 + 100, "air doors, FO (natural draft)", "t8")
    s.bubble(xe + 90, py1 + 136, "ZT", "1362")
    s.line([(xe + 71, py1 + 132), (xe + 34, py1 + 44)], "thin")

    # --- LP steam: soot blowers, snuffing, header boxes ---------------------------------
    ys = 180
    s.offsheet(24, ys, "LP STEAM 3.5 barg", "from LP header", "right", 160)
    s.line([(184, ys), (cvx0 - 15, ys), (cvx0 - 15, cvy0 + 10)], "util")
    s.bubble(260, ys - 40, "PI", "1403")
    s.line([(260, ys - 21), (260, ys)], "thin")
    s.text(cvx0 - 22, ys - 8, "to soot blowers (SB-102A/B on PID-103)", "t9", "end")
    s.bubble(cvx0 - 110, cvy0 + 66, "HS", "1501", "dcs")
    s.text(cvx0 - 110, cvy0 + 100, "soot-blow sequencer", "t9", "middle")
    s.sig([(cvx0 - 91, cvy0 + 66), (cvx0 - 70, cvy0 + 66)])
    s.line([(560, ys), (560, rdy0 + 170), (rdx0, rdy0 + 170)], "util", arrow=True)
    s.onoff_valve(560, rdy0 + 80, None, None, vertical=True)
    s.text(548, rdy0 + 78, "XV-1401", "t9 b", "end")
    s.text(548, rdy0 + 90, "firebox snuffing", "t9", "end")
    s.text(548, rdy0 + 102, "(manual initiation)", "t9", "end")
    s.line([(420, ys), (420, ys + 80), (500, ys + 80)], "util", arrow=True)
    s.valve(420, ys + 45, vertical=True)
    s.text(432, ys + 49, "HV-1402", "t9 b")
    s.text(506, ys + 84, "to header boxes", "t9")

    # --- fuel gas train -----------------------------------------------------------------
    yl = py1 + 30
    yf = yl + 40
    s.offsheet(24, yf + 60, "REFINERY FUEL GAS", "header ≈ 4.5 barg", "right", 160)
    s.line([(184, yf + 60), (196, yf + 60)], "fuel")
    s.rect(196, yf - 10, 50, 120, "eq", rx=22)
    s.text(256, yf + 50, "V-101", "t11 b")
    s.text(256, yf + 62, "FG KO drum", "t9")
    s.line([(221, yf + 110), (221, yf + 126)], "fuel")
    s.text(230, yf + 136, "to closed drain", "t8")
    s.bubble(150, yf + 10, "LT", "1205")
    s.line([(169, yf + 10), (196, yf + 10)], "thin")
    s.text(150, yf - 16, "LSHH-1205 → I-101", "t8", "middle")
    s.line([(221, yf - 10), (221, yl), (g["burners"][-1], yl)], "fuel")
    s.text(232, yl - 6, '4"-FG-1201', "t9")
    s.orifice(285, yl)
    s.bubble(285, yl - 58, "FT", "1201")
    s.line([(285, yl - 39), (285, yl - 11)], "thin")
    s.bubble(325, yl + 50, "AT", "1203")
    s.line([(325, yl + 31), (325, yl)], "thin")
    s.text(325, yl + 82, "LHV", "t8", "middle")
    s.bubble(370, yl + 50, "TT", "1204")
    s.line([(370, yl + 31), (370, yl)], "thin")
    s.control_valve(420, yl)
    s.text(420, yl - 40, "PV-1202 FC", "t9 b", "middle")
    s.bubble(430, yl + 82, "PIC", "1202", "dcs")
    s.sig([(449, yl + 82), (460, yl + 82), (460, yl - 26), (431, yl - 26)])
    s.offsheet(250, yl + 132, "FROM TIC-1110", "U100-PID-101 (remote SP)", "right", 160)
    s.sig([(410, yl + 132), (430, yl + 132), (430, yl + 101)])
    s.onoff_valve(495, yl, "XV-1201", "FC")
    s.bubble(495, yl + 48, "I", "101", "sis", r=13)
    s.sig([(495, yl + 35), (495, yl + 20)])
    s.line([(530, yl), (530, yl - 100)], "fuel", arrow=True)
    s.onoff_valve(530, yl - 55, None, None, vertical=True)
    s.text(518, yl - 58, "XV-1203 FO", "t9 b", "end")
    s.text(530, yl - 106, "bleed to safe location", "t8", "middle")
    s.onoff_valve(565, yl, "XV-1202", "FC")
    s.bubble(565, yl + 50, "I", "101", "sis", r=13)
    s.sig([(565, yl + 37), (565, yl + 20)])
    s.bubble(612, yl - 55, "PT", "1206")
    s.line([(612, yl - 36), (612, yl)], "thin")
    s.bubble(656, yl - 55, "PT", "1207")
    s.line([(656, yl - 36), (656, yl)], "thin")
    s.text(634, yl - 84, "LL 0.25 / HH 2.5 barg → I-101", "t8", "middle")
    s.add(f'<circle cx="690" cy="{yl}" r="3" fill="#000"/>')
    s.sig([(690, yl), (690, yl + 110), (430, yl + 110), (430, yl + 101)])
    s.text(600, yl + 122, "PIC-1202 measures burner manifold pressure", "t8", "middle")
    for i, x in enumerate(g["burners"]):
        s.line([(x, yl), (x, py1 - 30)], "fuel")
        s.valve(x, yl - 14, vertical=True, s=5)
        s.bubble(x, yl + 72, "BS", str(1211 + i), r=17)
        s.sig([(x, yl + 55), (x, yl + 4)])
        s.text(x + 8, py0 + 26, "ABCDEFGH"[i], "t9 b")
    s.text(g["burners"][0] - 18, py0 + 26, "B-101", "t9 b", "end")
    s.text(g["burners"][0] - 20, yl + 104, "flame scanners → I-101 (≥ 3 of 8 lost = trip)", "t8")
    s.text(g["burners"][0] - 20, yl + 116, "burner manifold 1.2 barg; manual cock on each riser", "t8")

    # --- pilot gas ----------------------------------------------------------------------
    yp = yl + 200
    s.offsheet(24, yp, "PILOT GAS", "regulated 0.7 barg", "right", 160)
    s.line([(184, yp), (g["burners"][-1] + 20, yp)], "util", arrow=True)
    s.bubble(600, yp - 44, "PT", "1208")
    s.line([(600, yp - 25), (600, yp)], "thin")
    s.text(626, yp - 40, "LL 0.25 → I-101", "t8")
    s.onoff_valve(470, yp, "XV-1209", "FC")
    s.bubble(505, yp - 26, "I", "101", "sis", r=13)
    s.sig([(492, yp - 26), (478, yp - 26)])
    s.text(g["burners"][0], yp - 6, "pilot manifold → continuous pilots B-101A–H", "t8")

    # --- BMS logic + manual ESD ----------------------------------------------------------
    s.bubble(110, 560, "I", "101", "sis", r=22)
    s.text(110, 528, "BMS / SIS logic", "t9 b", "middle")
    s.text(140, 564, "inputs/outputs: see summary table", "t8")
    s.bubble(110, 630, "HS", "1290", "sis")
    s.text(140, 634, "manual ESD (control room + field)", "t8")
    s.sig([(110, 611), (110, 582)])

    # --- cause & effect summary -----------------------------------------------------------
    cx0, cy0, cw = 1300, 700, 364
    rows = [
        ("Initiator", "Effect"),
        ("FT-1151..1154 pass flow < 43 t/h (2 s)", "Main fuel trip"),
        ("PT-1206 FG < 0.25 / PT-1207 > 2.5 barg", "Main fuel trip"),
        ("LT-1205 KO drum level > 80 %", "Main fuel trip"),
        ("Flame loss ≥ 3 of 8 (BS-1211..1218)", "Main fuel trip"),
        ("PT-1314 firebox > +10 mmH2O (5 s)", "Main fuel trip"),
        ("PT-1208 pilot gas < 0.25 barg", "Total trip"),
        ("HS-1290 manual ESD", "Total trip"),
        ("XS-1341 FD / XS-1351 ID fan stop", "Natural-draft runback"),
        ("XS-1349 APH rotor stop", "Natural-draft runback"),
        ("Main fuel trip:", "close XV-1201/1202, open XV-1203"),
        ("Total trip:", "+ close XV-1209"),
        ("Natural-draft runback:", "open XV-1361 + XV-1362, stop"),
        ("", "other fan, firing ≤ 60 % (not a trip)"),
        ("Alarms only:", "TMT, COT, O2, CO, coil ΔP, APH"),
        ("", "outlet, fan speed — optimizer limits"),
    ]
    s.rect(cx0, cy0, cw, 34 + len(rows) * 17, "box")
    s.rect(cx0, cy0, cw, 20, "hdr")
    s.text(cx0 + 8, cy0 + 15, "I-101 BMS / SIS SUMMARY (doc safe_bms_cause_and_effect)", "t10 b")
    for k, (a, b) in enumerate(rows):
        y = cy0 + 36 + k * 17
        cls = "t8 b" if k == 0 or a.endswith(":") else "t8"
        s.text(cx0 + 8, y, a, cls)
        s.text(cx0 + 192, y, b, "t8 b" if k == 0 else "t8")
        if k in (0, 9, 13):
            s.line([(cx0, y + 7), (cx0 + cw, y + 7)], "grid")

    notes(s, [
        "1. Balanced draft (Rev B): ID fan K-102 holds arch draft (PIC-1311 → SC-1351); FD fan K-101 supplies hot combustion air",
        "   via E-102 (AIC-1321 → FIC-1341 → SC-1341). Fans, APH, cold-air bypass and ducts are on U100-PID-103.",
        "2. O2 chain: arch AIC-1321 (3.0 %) → convection outlet AT-1327 (≈ 3.2 %) → stack AT-1326 (≈ 4.4 %, after APH seal leakage).",
        "3. D-101 bypass damper XV-1361 and D-102 emergency air doors XV-1362 fail OPEN for natural-draft operation (≤ 60 % firing).",
        "4. Main fuel trip closes XV-1201/XV-1202 and opens bleed XV-1203 (double block and bleed). Pilots isolated by XV-1209.",
        "5. Burner manual cocks on each riser; single flame loss isolates that burner locally (not shown).",
        "6. Snuffing steam XV-1401 manually initiated (tube rupture / firebox fire). Soot blowers SB-101A–F daily via HS-1501.",
        "7. Symbols: see legend on U100-PID-101. Values per design/tag_register.csv (Rev B); preliminary, pending ChemE review.",
    ])
    return s


# =====================================================================================
# P&ID sheet 3 — air preheater, FD / ID fans, ducts, dampers (Rev B)
# =====================================================================================
def draw_pid3():
    s = Sheet()
    s.frame("P&ID — H-101 AIR PREHEATER, FD / ID FANS & DUCTS", "U100-PID-103", "B", "3 of 3")
    s.text(30, 40, "P&ID U100-PID-103 — H-101 REGENERATIVE AIR PREHEATER, FD / ID FANS, DUCTS & DAMPERS", "t16 b")
    ax0, ay0, aw, ah = 700, 300, 240, 300
    aph(s, ax0, ay0, aw, ah, gas_right=True, label=False)
    s.text(ax0 + aw / 2, ay0 + ah + 22, "E-102 REGENERATIVE AIR PREHEATER (Ljungström)", "t11 b", "middle")
    s.text(ax0 + aw / 2, ay0 + ah + 36, "duty ≈ 4.3 MW; seal leakage ≈ 6 % of air as new; vertical shaft, rotor ≈ 1 rpm", "t9", "middle")
    gx, axx = ax0 + aw * 0.75, ax0 + aw * 0.25
    # rotor drive
    s.circle(ax0 + aw / 2, ay0 - 40, 16, "box")
    s.text(ax0 + aw / 2, ay0 - 36, "M", "t10 b", "middle")
    s.line([(ax0 + aw / 2, ay0 - 24), (ax0 + aw / 2, ay0)], "thin")
    s.text(ax0 + aw / 2 + 20, ay0 - 30, "drive", "t8")
    s.bubble(ax0 + aw / 2, ay0 - 100, "XS", "1349", "sis")
    s.sig([(ax0 + aw / 2, ay0 - 81), (ax0 + aw / 2, ay0 - 56)])
    s.text(ax0 + aw / 2 + 24, ay0 - 104, "rotor stop", "t8")
    s.text(ax0 + aw / 2 + 24, ay0 - 94, "→ runback", "t8")

    # --- gas side ------------------------------------------------------------------------
    s.offsheet(1180, 160, "FROM CONVECTION OUTLET", "U100-PID-102 (≈ 390 °C)", "left", 190)
    s.line([(1180, 160), (gx, 160), (gx, ay0)], "flue", arrow=True, grey=True)
    s.text(gx + 8, 152, "flue duct (insulated)", "t9")
    for k, (x, y) in enumerate([(gx + 60, ay0 + 40), (gx + 60, ay0 + ah - 40)]):
        s.rect(ax0 + aw + 4, y - 7, 24, 14, "box")
        s.text(ax0 + aw + 34, y + 4, f"SB-102{'AB'[k]}", "t9 b")
    s.text(ax0 + aw + 34, ay0 + 58, "hot-end soot blower", "t8")
    s.text(ax0 + aw + 34, ay0 + ah - 22, "cold-end soot blower", "t8")
    s.line([(ax0 + aw + 16, ay0 + 33), (ax0 + aw + 16, ay0 - 60), (1180, ay0 - 60)], "util")
    s.offsheet(1180, ay0 - 60, "LP STEAM", "soot blowing, HS-1501", "left", 150)
    s.line([(ax0 + aw + 16, ay0 + ah - 47), (ax0 + aw + 16, ay0 + 47)], "util")
    s.bubble(gx + 160, ay0 + ah / 2, "PDT", "1347")
    s.line([(gx + 141, ay0 + ah / 2 - 8), (gx + 30, ay0 + 10)], "thin")
    s.line([(gx + 141, ay0 + ah / 2 + 8), (gx + 30, ay0 + ah - 10)], "thin")
    s.text(gx + 186, ay0 + ah / 2 + 4, "gas ΔP 80 mmH2O (Hi 120)", "t8")
    # gas outlet → ID fan
    idy = ay0 + ah + 150
    s.line([(gx, ay0 + ah), (gx, idy), (gx + 100, idy)], "flue", arrow=True, grey=True)
    s.bubble(gx - 70, ay0 + ah + 70, "TIC", "1345", "dcs")
    s.line([(gx - 51, ay0 + ah + 70), (gx, ay0 + ah + 70)], "thin")
    s.text(gx - 96, ay0 + ah + 74, "≈ 150 °C, LL 140", "t8", "end")
    s.bubble(gx + 50, idy - 50, "PT", "1352")
    s.line([(gx + 50, idy - 31), (gx + 50, idy)], "thin")
    idx = gx + 130
    fan(s, idx, idy, "K-102 ID FAN", "centrifugal, VFD; 40 kW abs. / 90 kW motor", label_dy=42)
    s.line([(idx + 22, idy), (1420, idy), (1420, 120), (1410, 120)], "flue", arrow=True, grey=True)
    s.offsheet(1240, 120, "TO STACK S-101", "U100-PID-102 (≈ 155 °C)", "left", 170)
    # ID fan instruments
    s.bubble(idx - 30, idy + 80, "SC", "1351", "field")
    s.sig([(idx - 22, idy + 63), (idx - 8, idy + 20)])
    s.bubble(idx + 30, idy + 80, "SI", "1351")
    s.bubble(idx + 80, idy + 80, "JI", "1351")
    s.bubble(idx + 130, idy + 80, "XS", "1351", "sis")
    s.offsheet(idx - 210, idy + 80, "FROM PIC-1311", "arch draft, U100-PID-102", "right", 160)
    s.sig([(idx - 50, idy + 80), (idx - 49, idy + 80)])

    # --- air side ------------------------------------------------------------------------
    fdy = idy
    fdx = axx - 160
    s.offsheet(30, fdy, "AMBIENT AIR", "via inlet filter / silencer", "right", 160)
    s.line([(190, fdy), (fdx - 22, fdy)], "util", arrow=True)
    s.bubble(260, fdy - 50, "TT", "1001")
    s.line([(260, fdy - 31), (260, fdy)], "thin")
    fan(s, fdx, fdy, "K-101 FD FAN", "centrifugal, VFD; 30 kW abs. / 75 kW motor", label_dy=42)
    s.line([(fdx + 22, fdy), (axx, fdy), (axx, ay0 + ah)], "util", arrow=True)
    s.orifice(fdx + 45, fdy)
    s.bubble(fdx + 45, fdy - 55, "FIC", "1341", "dcs")
    s.line([(fdx + 45, fdy - 36), (fdx + 45, fdy - 11)], "thin")
    s.sig([(fdx + 51, fdy - 55), (fdx, fdy - 55), (fdx, fdy - 22)] if False else [(fdx + 26, fdy - 55), (fdx + 14, fdy - 55), (fdx + 14, fdy - 18)])
    s.offsheet(fdx - 270, fdy - 110, "FROM AIC-1321", "arch O2, U100-PID-102 (SP)", "right", 170)
    s.sig([(fdx - 100, fdy - 110), (fdx + 45, fdy - 110), (fdx + 45, fdy - 74)])
    s.bubble(fdx - 30, fdy + 80, "SC", "1341")
    s.sig([(fdx - 22, fdy + 63), (fdx - 8, fdy + 20)])
    s.bubble(fdx + 30, fdy + 80, "SI", "1341")
    s.bubble(fdx + 80, fdy + 80, "JI", "1341")
    s.bubble(fdx + 130, fdy + 80, "XS", "1341", "sis")
    s.bubble(axx - 150, ay0 + ah / 2, "PDT", "1348")
    s.line([(axx - 131, ay0 + ah / 2 - 8), (axx - 20, ay0 + 10)], "thin")
    s.line([(axx - 131, ay0 + ah / 2 + 8), (axx - 20, ay0 + ah - 10)], "thin")
    s.text(axx - 176, ay0 + ah / 2 + 4, "air ΔP 50 (Hi 75)", "t8", "end")
    # hot air → windbox
    s.line([(axx, ay0), (axx, 160), (330, 160)], "util", arrow=True)
    s.offsheet(170, 160, "HOT AIR TO WINDBOX", "U100-PID-102 (≈ 300 °C)", "left", 160)
    s.line([(330, 160), (330, 160)], "util")
    s.bubble(axx - 60, 110, "TT", "1343")
    s.line([(axx - 60, 129), (axx - 60, 160)], "thin")
    # cold-air bypass TV-1345 (from FD discharge, after FIC-1341, around the APH into the hot-air duct)
    xb = axx - 80
    s.line([(xb, fdy), (xb, 210), (axx, 210)], "util")
    s.add(f'<circle cx="{xb}" cy="{fdy}" r="3" fill="#000"/>')
    s.add(f'<circle cx="{axx}" cy="210" r="3" fill="#000"/>')
    yb = ay0 + 60
    damper(s, xb, yb)
    s.line([(xb, yb), (xb - 30, yb)], "thin")
    s.add(f'<path d="M{xb-30},{yb-11} A11,11 0 0,0 {xb-30},{yb+11} z" class="box"/>')
    s.text(xb - 46, yb - 2, "TV-1345", "t9 b", "end")
    s.text(xb - 46, yb + 10, "cold-air bypass, FC", "t8", "end")
    s.sig([(gx - 70, ay0 + ah + 89), (gx - 70, ay0 + ah + 104), (xb - 120, ay0 + ah + 104), (xb - 120, yb), (xb - 41, yb)])

    # --- runback summary + notes -----------------------------------------------------------
    bx, by, bw = 1180, 788, 484
    rows = [
        "NATURAL-DRAFT RUNBACK (I-101, see U100-PID-102)",
        "Initiators: XS-1341 FD stop, XS-1351 ID stop, XS-1349 APH rotor stop",
        "Actions: open XV-1361 bypass damper (D-101) and XV-1362",
        "emergency air doors (D-102); stop the other fan; clamp",
        "PIC-1202 setpoint so firing ≤ 60 % of normal. Not a fuel trip.",
        "",
        "OPTIMIZER LIMITS ON THIS SHEET",
        "TIC-1345 APH gas outlet ≥ 140 °C (acid dew point margin)",
        "SI-1341 / SI-1351 fan speed ≤ 95 % (capacity)",
        "Fan power JI-1341 + JI-1351 is a cost term",
        "",
        "DEGRADATION FINGERPRINTS (Type B)",
        "Seal leakage ↑: AT-1326 − AT-1327 ↑ (≈ 1.2 new), SI-1351 ↑,",
        "  TIC-1345 ↓ (dilution), FIC-1341 ↑ for same burner air",
        "Fouling ↑: PDT-1347 ↑, TT-1343 ↓, TIC-1345 ↑, ID load ↑",
    ]
    s.rect(bx, by, bw, 20 + len(rows) * 13.4, "box")
    for k, r in enumerate(rows):
        s.text(bx + 10, by + 18 + k * 13.4, r, "t9 b" if r.isupper() or r.startswith(("NATURAL", "OPTIMIZER", "DEGRADATION")) else "t9")
    notes(s, [
        "1. Regenerative APH: gas and air halves counter-current; rotor drive with rotation monitor XS-1349 (rotor stop = runback + APH fire watch).",
        "2. FD fan K-101 sets combustion air (FIC-1341, cascaded from AIC-1321 arch O2); ID fan K-102 holds arch draft (PIC-1311 on PID-102).",
        "3. TV-1345 cold-air bypass (TIC-1345 SP 148 °C, Lo alarm 145, limit 140) opens in cold weather / low load; closed at design.",
        "4. FIC-1341 measures FD discharge air, which includes APH seal leakage — burner air = FIC-1341 minus leakage.",
        "5. SB-102A/B steam soot blowers (hot and cold end) sequenced with SB-101A–F; offline water-wash connections not shown.",
        "6. Duct expansion joints, inlet filter/silencer, fan inlet dampers and seal-air systems not shown.",
        "7. Symbols: see legend on U100-PID-101. Values per design/tag_register.csv (Rev B); preliminary, pending ChemE review.",
    ])
    return s


# =====================================================================================
# P&ID sheet 1 — process coil
# =====================================================================================
def draw_pid1():
    s = Sheet()
    s.frame("P&ID — H-101 PROCESS COIL (4 PASSES)", "U100-PID-101", "B", "1 of 3")
    s.text(30, 40, "P&ID U100-PID-101 — H-101 CRUDE CHARGE HEATER, PROCESS COIL", "t16 b")
    hx = 200
    rows = [255, 440, 625, 810]
    passes = "ABCD"
    cvx0, cvx1, rdx0, rdx1, ox = 615, 790, 890, 1170, 1330
    # inlet header
    s.offsheet(24, 80, "FROM PREHEAT TRAIN", "E-101 / P-101A/B", "right", 160)
    s.line([(184, 80), (hx, 80), (hx, rows[-1])], "proc")
    s.text(hx + 8, 74, '16"-P-1100-A1 inlet header', "t9")
    s.bubble(hx + 60, 135, "TT", "1100")
    s.line([(hx + 41, 135), (hx, 135)], "thin")
    s.bubble(hx + 115, 135, "PT", "1100")
    s.line([(hx + 96, 135), (hx + 79, 135)], "thin")
    s.bubble(hx + 330, 70, "FY", "1100", "dcs")
    s.text(hx + 353, 66, "Σ FIC-1101..1104", "t9")
    s.text(hx + 353, 78, "(total charge)", "t9")

    # heater section boxes
    s.rect(cvx0, 150, cvx1 - cvx0, 770, "refr")
    s.rect(cvx0 + 8, 158, cvx1 - cvx0 - 16, 754, "box")
    s.text((cvx0 + cvx1) / 2, 140, "H-101 CONVECTION SECTION", "t11 b", "middle")
    s.rect(rdx0, 150, rdx1 - rdx0, 770, "refr")
    s.rect(rdx0 + 8, 158, rdx1 - rdx0 - 16, 754, "box")
    s.text((rdx0 + rdx1) / 2, 140, "H-101 RADIANT SECTION", "t11 b", "middle")
    s.text((cvx0 + cvx1) / 2, 936, "studded + 2 bare shield rows / pass", "t9", "middle")
    s.text((rdx0 + rdx1) / 2, 936, "20 tubes / pass, 6\" Sch 40 A335 P9", "t9", "middle")

    for i, (y, p) in enumerate(zip(rows, passes)):
        n = 1101 + i
        s.line([(hx, y), (cvx0 + 22, y)], "proc")
        s.text(hx + 6, y - 22, f'6"-P-{n}-A1', "t8")
        s.valve(hx + 60, y)
        s.orifice(hx + 95, y)
        s.bubble(hx + 95, y - 62, "FT", str(n))
        s.line([(hx + 95, y - 43), (hx + 95, y - 11)], "thin")
        s.bubble(hx + 160, y - 62, "FIC", str(n), "dcs")
        s.sig([(hx + 114, y - 62), (hx + 141, y - 62)])
        s.control_valve(hx + 160, y)
        s.sig([(hx + 160, y - 43), (hx + 160, y - 31)])
        s.text(hx + 160, y + 24, f"FV-{n}", "t9 b", "middle")
        s.text(hx + 160, y + 35, "FO", "t9", "middle")
        s.valve(hx + 205, y)
        s.orifice(hx + 245, y)
        s.bubble(hx + 245, y - 62, "FT", str(1151 + i))
        s.line([(hx + 245, y - 43), (hx + 245, y - 11)], "thin")
        s.sig([(hx + 264, y - 62), (hx + 280, y - 62)])
        s.text(hx + 283, y - 66, "to I-101", "t8")
        s.text(hx + 283, y - 56, "LL 43 t/h", "t8")
        s.bubble(hx + 290, y + 52, "PT", str(n))
        s.line([(hx + 290, y + 33), (hx + 290, y)], "thin")
        s.blind(hx + 318, y)
        s.valve(hx + 345, y)
        s.text(hx + 345, y - 16, f"XV-1105{p}", "t9 b", "middle")
        s.line([(hx + 378, y), (hx + 378, y + 30)], "proc")
        s.line([(hx + 370, y + 30), (hx + 386, y + 30)], "proc")
        s.text(hx + 372, y + 44, "pig launcher", "t8", "middle")
        s.text(hx + 372, y + 54, "conn. (blinded)", "t8", "middle")
        # convection serpentine
        conv = [(cvx0 + 22, y)] + [(cvx0 + 22 + k * 22, (y - 42) if k % 2 == 0 else (y + 42)) for k in range(7)]
        conv += [(cvx1 - 22, y)]
        s.line(conv, "proc")
        s.text(cvx0 + 16, y - 50, f"PASS {p}", "t10 b")
        # crossover
        s.line([(cvx1 - 22, y), (rdx0 + 20, y)], "proc")
        s.text(cvx1 + 6, y - 8, f'6"-P-{n}-X', "t8")
        s.bubble(840, y + 52, "TT", str(1131 + i))
        s.line([(840, y + 33), (840, y)], "thin")
        # radiant serpentine
        rad = [(rdx0 + 20, y)] + [(rdx0 + 30 + k * 28, (y - 45) if k % 2 == 0 else (y + 45)) for k in range(9)]
        rad += [(rdx1 - 20, y)]
        s.line(rad, "proc")
        for j, (k_, tag) in enumerate([(2, "A"), (6, "B")]):
            xx, yy = rdx0 + 30 + k_ * 28, y - 45
            s.add(f'<circle cx="{xx}" cy="{yy}" r="3" fill="#000"/>')
            s.bubble(xx + 36, yy - 16, "TI", f"{1121+i}{tag}")
            s.line([(xx, yy), (xx + 19, yy - 8)], "thin")
        s.text(rdx0 + 16, y + 64, "skin TCs at hot zone (peak flux)", "t8")
        # outlet
        s.line([(rdx1 - 20, y), (ox, y)], "proc")
        s.bubble(1205, y - 52, "TT", str(1111 + i))
        s.line([(1205, y - 33), (1205, y)], "thin")
        s.line([(1240, y), (1240, y + 30)], "proc")
        s.line([(1232, y + 30), (1248, y + 30)], "proc")
        s.text(1244, y + 44, "pig receiver", "t8", "middle")
        s.text(1244, y + 54, "conn. (blinded)", "t8", "middle")
        s.valve(1275, y)
        s.text(1275, y - 16, f"XV-1106{p}", "t9 b", "middle")
        s.blind(1302, y)
        s.bubble(1205, y + 76, "PDI", str(n), "dcs")
        s.text(1227, y + 76, f"= PT-{n} − PT-1110", "t8")
        s.text(1227, y + 86, "Hi 7.8 / HH 8.4 bar", "t8")
    # outlet header + transfer line
    s.line([(ox, rows[0]), (ox, 970), (1450, 970)], "proc")
    s.text(ox + 8, 992, '20"-P-1110-A2 transfer line', "t9")
    s.offsheet(1450, 970, "TO C-101 FLASH ZONE", "atmospheric column", "right", 170)
    s.add(f'<circle cx="1375" cy="970" r="3" fill="#000"/>')
    s.bubble(1375, 915, "TIC", "1110", "dcs")
    s.line([(1375, 934), (1375, 970)], "thin")
    s.sig([(1394, 915), (1410, 915), (1410, 880)])
    s.offsheet(1400, 867, "TO PIC-1202", "U100-PID-102 (remote SP)", "right", 160)
    s.add(f'<circle cx="1425" cy="970" r="3" fill="#000"/>')
    s.bubble(1440, 925, "PT", "1110")
    s.line([(1430, 941), (1425, 970)], "thin")
    s.bubble(1250, 985, "TDA", "1111-14", "dcs")
    s.text(1212, 1004, "pass outlet deviation ±6 °C", "t8", "end")

    legend(s, 1420, 60)
    notes(s, [
        "1. Pass flow valves FV-1101..1104 fail OPEN; no bypass around pass FVs (prevents unmeasured low flow).",
        "2. FT-1151..1154 are independent SIS transmitters (separate taps); LL 43 t/h (60 %) trips main fuel via I-101.",
        "3. Skin TCs TI-1121A..1124B: knife-edge pad welded, 2 per pass at the predicted peak-flux / hottest tube.",
        "   TMT Hi 585 °C, limit 600 °C (alarm + IOW, not a trip). SOR hottest tube ≈ 430 °C.",
        "4. PDI-1101..1104 are DCS calculations (pass inlet PT minus common outlet PT-1110). Clean SOR ≈ 6.0 bar.",
        "5. XV-1105A–D / XV-1106A–D manual isolation + spectacle blinds for mechanical pigging; launcher/receiver",
        "   connections blinded in normal operation. Crossovers external for pigging access.",
        "6. Combustion, fuel gas, burners and BMS on U100-PID-102; APH, FD/ID fans on U100-PID-103. Values per tag_register.csv.",
    ])
    return s




def legend(s, x, y, w=240):
    items = [
        ("proc", "Process line (crude)"), ("fuel", "Fuel gas line"), ("util", "Utility line (steam, air)"),
        ("sig", "Electrical / DCS signal"), ("flue", "Flue gas path")]
    hgt = 535
    s.rect(x, y, w, hgt, "box")
    s.rect(x, y, w, 20, "hdr")
    s.text(x + 8, y + 15, "LEGEND (ISA-5.1 style)", "t10 b")
    yy = y + 40
    for cls, lab in items:
        s.line([(x + 12, yy), (x + 62, yy)], cls)
        s.text(x + 72, yy + 4, lab, "t9")
        yy += 20
    yy += 10
    s.bubble(x + 32, yy + 4, "TT", "xxxx", r=17)
    s.text(x + 60, yy + 8, "Field instrument", "t9")
    yy += 42
    s.bubble(x + 32, yy + 4, "TIC", "xxxx", "dcs", r=17)
    s.text(x + 60, yy + 8, "DCS function (shared display)", "t9")
    yy += 42
    s.bubble(x + 32, yy + 4, "I", "101", "sis", r=17)
    s.text(x + 60, yy + 8, "SIS / BMS interlock", "t9")
    yy += 40
    s.valve(x + 32, yy)
    s.text(x + 60, yy + 4, "Gate / block valve", "t9")
    yy += 32
    s.control_valve(x + 32, yy + 10, None)
    s.text(x + 60, yy + 4, "Control valve, diaphragm actuator", "t9")
    yy += 38
    s.onoff_valve(x + 32, yy + 10)
    s.text(x + 60, yy + 4, "On/off shutdown valve (solenoid)", "t9")
    yy += 30
    s.line([(x + 12, yy), (x + 52, yy)], "proc")
    s.orifice(x + 32, yy)
    s.text(x + 60, yy + 4, "Flow element (orifice)", "t9")
    yy += 26
    s.blind(x + 32, yy)
    s.text(x + 60, yy + 4, "Spectacle blind", "t9")
    yy += 26
    s.stream(x + 32, yy, 1)
    s.text(x + 60, yy + 4, "Stream number (PFD)", "t9")
    yy += 22
    s.text(x + 12, yy + 4, "FO / FC = fail open / fail closed", "t9")
    s.text(x + 12, yy + 18, "Letters: F flow, P pressure, T temp, A analysis,", "t9")
    s.text(x + 12, yy + 30, "L level, Z position, B burner/flame, H hand;", "t9")
    s.text(x + 12, yy + 42, "I indicate, C control, T transmit, Y compute,", "t9")
    s.text(x + 12, yy + 54, "D(I) differential, DA deviation alarm.", "t9")


def notes(s, lines, x=30, y=1012, w=1068):
    s.rect(x, y, w, 160, "box")
    s.text(x + 10, y + 18, "NOTES", "t10 b")
    for k, n in enumerate(lines):
        s.text(x + 10, y + 36 + k * 15, n, "t9")



if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("U100-PFD-001_H101_PFD", draw_pfd), ("U100-PID-101_H101_process_coil", draw_pid1),
                     ("U100-PID-102_H101_combustion_fuel_burners_bms", draw_pid2),
                     ("U100-PID-103_H101_air_preheater_fans", draw_pid3)]:
        (OUT / f"{name}.svg").write_text(fn().svg(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")
