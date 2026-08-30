#!/usr/bin/env python3
"""
Doctor's Residence Estate - prospect pack.
The document a CPAL realtor sends when a buyer says "send me details".

Two constraints drive every decision here:
  1. It is read on a phone. Type is set large enough that an A4 page scaled to a
     phone screen is still comfortable, which means fewer words per page and more pages.
  2. People decide emotionally and justify logically. Each section opens on what the
     reader feels, then hands them the numbers they will use to defend the decision.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

NAVY       = colors.HexColor('#003399')
NAVY_BLACK = colors.HexColor('#000E2B')
GOLD       = colors.HexColor('#D4AF2B')
GOLD_SOFT  = colors.HexColor('#F0DFA4')
VIOLET     = colors.HexColor('#3F3F95')
LATERITE   = colors.HexColor('#A8462A')
GREEN      = colors.HexColor('#1B6B3A')
PAPER      = colors.HexColor('#FCFBF7')
WARM       = colors.HexColor('#F3F0E6')
RUSTBG     = colors.HexColor('#FDF5EE')
INK        = colors.HexColor('#12141A')
SOFT       = colors.HexColor('#4E5462')
RULE       = colors.HexColor('#C9D3EA')
DRULE      = colors.HexColor('#26324D')
DSOFT      = colors.HexColor('#8A97B2')
DTEXT      = colors.HexColor('#DDE4F2')
WHITE      = colors.white

W, H = A4
M  = 18 * mm
CW = W - 2 * M

F   = '/home/claude/fonts'
IMG = '/home/claude/cpal/assets/img'
LOGO_LIGHT = f'{IMG}/cpal-logo-print.png'
COVER = f'{IMG}/cover-launch.jpg'
HERO  = f'{IMG}/hero-crop.jpg'
SIGN  = f'{IMG}/sign-crop.jpg'
CHAIR = f'{IMG}/chairman-print.jpg'
TV    = f'{IMG}/delta-tv-print.jpg'

for tag, fn in [('Disp', 'Archivo-Display.ttf'), ('Semi', 'Archivo-Semi.ttf'),
                ('Body', 'Newsreader-Regular.ttf'), ('BodyB', 'Newsreader-Medium.ttf'),
                ('Mono', 'PlexMono-Regular.ttf'), ('MonoB', 'PlexMono-Medium.ttf')]:
    pdfmetrics.registerFont(TTFont(tag, os.path.join(F, fn)))

# Sized for phone reading, not for a desk.
body  = ParagraphStyle('b',  fontName='Body', fontSize=14.6, leading=21.5, textColor=INK)
bodyB = ParagraphStyle('bb', parent=body, fontName='BodyB')
bodyS = ParagraphStyle('bs', parent=body, fontSize=13.6, leading=20, textColor=SOFT)
bodyW = ParagraphStyle('bw', parent=body, textColor=DTEXT)
noteS = ParagraphStyle('n',  parent=body, fontSize=13.6, leading=20)
noteW = ParagraphStyle('nw', parent=noteS, textColor=DTEXT)


class Pack:
    def __init__(self, path):
        c = self.c = canvas.Canvas(path, pagesize=A4)
        c.setTitle("Doctor's Residence Estate, Atuma-Iga - CPAL")
        c.setAuthor('Chuks Properties Academy Limited (RC 8324784)')
        c.setSubject("Land for sale at Atuma-Iga, Oshimili North, Delta State")
        c.setKeywords('land for sale Asaba, Atuma-Iga, Oshimili North, Delta State, CPAL')
        self.n = 0

    # ---------------------------------------------------------------- chrome
    def bg(self, col=PAPER):
        self.c.setFillColor(col); self.c.rect(-1, -1, W + 2, H + 2, stroke=0, fill=1)

    def foot(self, dark=False):
        self.n += 1
        c = self.c
        c.setStrokeColor(DRULE if dark else RULE); c.setLineWidth(0.6)
        c.line(M, 14 * mm, W - M, 14 * mm)
        c.setFont('Mono', 8); c.setFillColor(DSOFT if dark else SOFT)
        c.drawString(M, 9.4 * mm, 'CPAL   RC 8324784   0806 789 8622')
        c.drawRightString(W - M, 9.4 * mm, f'{self.n:02d}')

    def page(self, label=None, dark=False):
        self.c.showPage()
        self.bg(NAVY_BLACK if dark else PAPER)
        if label:
            c = self.c
            c.setFont('Mono', 8); c.setFillColor(DSOFT if dark else SOFT)
            c.drawString(M, H - 13 * mm, label.upper())
            c.drawRightString(W - M, H - 13 * mm, "DOCTOR'S RESIDENCE")
            c.setStrokeColor(DRULE if dark else RULE); c.setLineWidth(0.6)
            c.line(M, H - 16 * mm, W - M, H - 16 * mm)
        return H - 31 * mm

    # ------------------------------------------------------------- elements
    def wrap(self, text, font, size, width):
        out, cur = [], ''
        for w in text.split():
            t = (cur + ' ' + w).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
            else:
                if cur: out.append(cur)
                cur = w
        if cur: out.append(cur)
        return out

    def kicker(self, y, text, dark=False):
        c = self.c
        c.setStrokeColor(GOLD); c.setLineWidth(2)
        c.line(M, y + 2.6, M + 7 * mm, y + 2.6)
        c.setFont('MonoB', 9); c.setFillColor(GOLD_SOFT if dark else NAVY)
        c.drawString(M + 10.5 * mm, y, text.upper())
        return y - 11 * mm

    def title(self, y, text, size=27, col=INK, lead=None, width=None):
        c = self.c
        c.setFont('Disp', size); c.setFillColor(col)
        lead = lead or size * 1.03
        for ln in self.wrap(text, 'Disp', size, width or CW):
            c.drawString(M, y, ln); y -= lead
        return y - 4 * mm

    def para(self, y, text, style=None, width=None, x=None):
        p = Paragraph(text, style or body)
        _, h = p.wrap(width or CW, H)
        p.drawOn(self.c, x if x is not None else M, y - h)
        return y - h - 5 * mm

    def row(self, y, label, value, tag=None, tcol=GREEN, dark=False, width=None, lw=54 * mm, x=None):
        c = self.c
        x = x if x is not None else M
        width = width or CW
        c.setStrokeColor(DRULE if dark else RULE); c.setLineWidth(0.6)
        c.line(x, y + 7 * mm, x + width, y + 7 * mm)
        c.setFont('Mono', 9.6); c.setFillColor(DSOFT if dark else SOFT)
        c.drawString(x, y, label.upper())
        c.setFont('Mono', 11); c.setFillColor(colors.HexColor('#EDF1F8') if dark else INK)
        c.drawString(x + lw, y, value)
        if tag:
            c.setFont('MonoB', 8.6); c.setFillColor(tcol)
            c.drawRightString(x + width, y, tag.upper())
        return y - 11.6 * mm

    def note(self, y, text, accent=GOLD, fill=WHITE, style=None):
        p = Paragraph(text, style or noteS)
        _, h = p.wrap(CW - 14 * mm, H)
        box = h + 13 * mm
        self.c.setFillColor(fill); self.c.rect(M, y - box, CW, box, stroke=0, fill=1)
        self.c.setFillColor(accent); self.c.rect(M, y - box, 2 * mm, box, stroke=0, fill=1)
        p.drawOn(self.c, M + 8 * mm, y - box + (box - h) / 2)
        return y - box - 6 * mm

    def pull(self, y, text, sub=None, dark=False):
        """A single strong line closing a page, set below a rule."""
        c = self.c
        y -= 6 * mm
        c.setStrokeColor(DRULE if dark else RULE); c.setLineWidth(0.6)
        c.line(M, y, W - M, y); y -= 14 * mm
        c.setFont('Disp', 21); c.setFillColor(GOLD if dark else NAVY)
        for ln in self.wrap(text, 'Disp', 21, CW * 0.96):
            c.drawString(M, y, ln); y -= 24
        if sub:
            y -= 4 * mm
            c.setFont('Body', 13.6); c.setFillColor(DSOFT if dark else SOFT)
            for ln in self.wrap(sub, 'Body', 13.6, CW * 0.94):
                c.drawString(M, y, ln); y -= 19
        return y

    def benefit(self, y, head, text, dark=False, num=None):
        """Feature as the headline, benefit as the sentence under it."""
        c = self.c
        c.setStrokeColor(DRULE if dark else RULE); c.setLineWidth(0.6)
        c.line(M, y + 8 * mm, W - M, y + 8 * mm)
        ind = 0
        if num:
            c.setFont('Mono', 9.6); c.setFillColor(GOLD); c.drawString(M, y, num)
            ind = 12 * mm
        c.setFont('Semi', 13.4); c.setFillColor(WHITE if dark else INK)
        c.drawString(M + ind, y, head)
        st = ParagraphStyle('bn', parent=bodyS, fontSize=13.2, leading=19,
                            textColor=DSOFT if dark else SOFT)
        p = Paragraph(text, st)
        _, h = p.wrap(CW - ind, H)
        p.drawOn(c, M + ind, y - h - 3 * mm)
        return y - h - 15 * mm


def build(out):
    d = Pack(out); c = d.c

    # =========================================================== 01 COVER
    d.bg(NAVY_BLACK)
    c.drawImage(COVER, 0, H - 126 * mm, width=W, height=74 * mm, mask='auto')
    c.setFillColorRGB(0, 0.055, 0.169, alpha=0.3)
    c.rect(0, H - 126 * mm, W, 74 * mm, stroke=0, fill=1)
    c.setFillAlpha(1)

    c.drawImage(LOGO_LIGHT, M, H - 33 * mm, width=44 * mm, height=11.5 * mm,
                preserveAspectRatio=True, anchor='sw')
    c.setFont('Mono', 8.4); c.setFillColor(GOLD_SOFT)
    c.drawRightString(W - M, H - 24 * mm, 'RC 8324784')
    c.drawRightString(W - M, H - 29.5 * mm, 'ASABA, DELTA STATE')

    y = H - 142 * mm
    c.setFont('MonoB', 8.6); c.setFillColor(GOLD)
    c.drawString(M, y, 'NOW SELLING    PHASE 1, ALONG THE ROAD    44 OF 64 PLOTS LEFT')
    y -= 18 * mm
    for line, col in [("Doctor's", WHITE), ('Residence', WHITE), ('Estate', GOLD)]:
        c.setFont('Disp', 47); c.setFillColor(col)
        c.drawString(M, y, line); y -= 43
    y -= 4
    c.setFont('Body', 15); c.setFillColor(colors.HexColor('#B9C4DA'))
    c.drawString(M, y, 'Atuma-Iga, Oshimili North LGA, Delta State')
    y -= 22
    c.setFont('BodyB', 15); c.setFillColor(WHITE)
    c.drawString(M, y, 'Land you can stand on, with papers in your own name.')

    c.setFillColor(NAVY); c.rect(0, 24 * mm, W, 32 * mm, stroke=0, fill=1)
    stats = [('464', 'SQM PER PLOT'), ('N4.5M', 'ALL DOCUMENTS IN'),
             ('N500k', 'STARTS YOUR PLAN'), ('44', 'PLOTS LEFT')]
    colw = W / 4
    for i, (big, small) in enumerate(stats):
        cx = colw * i + colw / 2
        c.setFont('Disp', 21); c.setFillColor(WHITE); c.drawCentredString(cx, 42 * mm, big)
        c.setFont('Mono', 6.8); c.setFillColor(GOLD_SOFT); c.drawCentredString(cx, 35.5 * mm, small)
        if i:
            c.setStrokeColor(colors.HexColor('#1B4BB0')); c.setLineWidth(0.7)
            c.line(colw * i, 30 * mm, colw * i, 49 * mm)
    c.setFont('Mono', 7.6); c.setFillColor(DSOFT)
    c.drawString(M, 16 * mm, 'CHUKS PROPERTIES ACADEMY LIMITED    AUGUST 2026')
    c.drawRightString(W - M, 16 * mm, 'CPALGROUP.COM')
    d.n = 1

    # =========================================================== 02 THE PREMISE
    y = d.page('Why this document exists', dark=True)
    y = d.title(y, 'Everybody says they', 30, WHITE, 30)
    y = d.title(y + 5 * mm, 'will buy land.', 30, WHITE, 30)
    y = d.title(y + 5 * mm, 'Most never do.', 30, GOLD, 30)
    y -= 2 * mm

    for t in ["Not because they cannot afford it. Because they are afraid.",
              "Afraid of the story everybody already knows. Somebody paid. Somebody sent money to a number "
              "a friend vouched for. There was a receipt, then a photograph, then excuses, then silence.",
              "Or the land was real and the papers were not, and they found out four years later with a "
              "house already standing on it.",
              "So it gets postponed. Next year. When things settle. When I can go and see it myself."]:
        y = d.para(y, t, bodyW, CW * 0.94)

    y -= 9 * mm
    c.setStrokeColor(DRULE); c.setLineWidth(0.6); c.line(M, y, W - M, y); y -= 14 * mm
    c.setFont('Disp', 25); c.setFillColor(GOLD)
    for ln in d.wrap('Meanwhile the land does not wait.', 'Disp', 25, CW):
        c.drawString(M, y, ln); y -= 28
    y -= 6 * mm
    y = d.para(y, "Somebody else buys the plot you were thinking about. They clear it, they build on it, and "
                  "in time they hand it to their children. It is theirs for good, and the decision you kept "
                  "postponing was made for you by somebody who moved first.", bodyW, CW * 0.94)
    d.foot(dark=True)

    # =========================================================== 03 PREMISE II
    y = d.page('Why this document exists', dark=True)
    y = d.title(y, 'This pack is for the person who is tired of postponing.', 27, WHITE, 28)
    y -= 3 * mm

    c.setFont('Disp', 22); c.setFillColor(WHITE)
    for ln in d.wrap('It does not ask you to trust us.', 'Disp', 22, CW * 0.95):
        c.drawString(M, y, ln); y -= 25
    y -= 4 * mm
    y = d.para(y, "It shows you what we can prove, tells you plainly what is still outstanding, and hands you "
                  "the means to check both without our help. Read it with a suspicious mind. That is what it "
                  "was written for.", bodyW, CW * 0.94)

    y -= 4 * mm
    c.setStrokeColor(DRULE); c.setLineWidth(0.6); c.line(M, y, W - M, y); y -= 11 * mm
    c.setFont('MonoB', 9); c.setFillColor(GOLD_SOFT); c.drawString(M, y, 'INSIDE'); y -= 12 * mm
    for num, label in [('04', 'What you actually get for your money'),
                       ('05', 'The papers, and their honest status'),
                       ('06', 'Why you keep three million naira buying here'),
                       ('07', 'Payment: start with N500,000'),
                       ('08', 'What is standing on the land today'),
                       ('09', 'How buying works, step by step'),
                       ('11', 'The man whose name is on the company'),
                       ('12', 'Come and walk it')]:
        c.setFont('Mono', 9.6); c.setFillColor(GOLD); c.drawString(M, y, num)
        c.setFont('Body', 14); c.setFillColor(DTEXT); c.drawString(M + 14 * mm, y, label)
        y -= 11.5 * mm
    d.foot(dark=True)

    # =========================================================== 04 WHAT YOU GET
    y = d.page('What you get')
    y = d.kicker(y, 'The plot')
    y = d.title(y, '464 square metres, with your name on the paper.', 27, NAVY, 28)
    y = d.para(y, "Here is what each number on the flyer actually means once you are standing on the land.",
               bodyS, CW * 0.94)
    y -= 3 * mm

    y = d.benefit(y, '464 sqm, not 450',
                  'Room for the house you actually want, a boys&rsquo; quarters behind it, and a compound '
                  'wide enough for children to play in. Most estates around Atuma-Iga sell 450. You are '
                  'getting more ground for less money.')
    y = d.benefit(y, 'Documentation included in the price',
                  'No second invoice arriving after you have already paid for the land. What you are quoted '
                  'is what you pay, and the papers come with it.')
    y = d.benefit(y, 'Thirteen minutes from Summit Junction',
                  'Close enough to drive out on a Saturday morning, stand on your own ground, and be back '
                  'in Asaba before noon. Far enough out that the land is still priced sensibly.')
    y = d.benefit(y, '33KVA transformer already installed',
                  'You are not starting in darkness or budgeting for a generator before you have laid a '
                  'single block.')
    y = d.pull(y, 'Four hundred and sixty-four square metres of Delta State, in your name.',
               'That is the whole offer. Everything else in this pack is us proving it.')
    d.foot()

    # =========================================================== 05 DOCUMENTATION
    y = d.page('The papers')
    y = d.kicker(y, 'Documentation record')
    y = d.title(y, 'This is the page most companies hope you skim.', 27, NAVY, 28)
    y = d.para(y, "Read it slowly. Everything confirmed is marked confirmed. Everything outstanding is marked "
                  "outstanding, in a different colour, because you deserve to know before you pay and not "
                  "after.", bodyS, CW * 0.95)
    y -= 3 * mm

    for lb, vl, tg, tc in [
        ('Registration', 'RC 8324784', 'Registered', GREEN),
        ('Deed of Assignment', 'Issued on allocation', 'Confirmed', GREEN),
        ('Survey plan', 'Registered, per plot', 'Confirmed', GREEN),
        ('C of O', 'Estate-wide', 'In view', LATERITE),
        ('Internal road', 'Delta State Ministry of Works', 'Building', VIOLET),
        ('Street lighting', 'Commissioned by NDDC', 'In progress', VIOLET),
        ('Power', '33KVA transformer on site', 'Installed', GREEN),
        ('Availability', '44 of 64 plots left', 'Selling', GREEN)]:
        y = d.row(y, lb, vl, tg, tc, lw=48 * mm)
    y -= 3 * mm

    y = d.note(y, '<b>What &ldquo;C of O in view&rdquo; means for you.</b> The estate-wide Certificate of '
                  'Occupancy is being processed and has not been issued. What you hold in the meantime is a '
                  'Deed of Assignment and a registered survey plan in your own name, both real and both '
                  'registered. Any company that tells you a C of O is finished when it is not has already '
                  'told you what kind of company it is.', LATERITE, RUSTBG)
    y = d.pull(y, 'Nothing on this page is hidden from you.',
               'Take it to your lawyer. Take it to your surveyor. We would rather you did.')
    d.foot()

    # =========================================================== 06 GOVERNMENT PROOF
    y = d.page('The papers')
    y = d.kicker(y, 'Proof you can photograph')
    y = d.title(y, 'The road to your gate is a government contract.', 27, INK, 28)

    iw = 58 * mm
    c.drawImage(SIGN, M, y - 70 * mm, width=iw, height=70 * mm, mask='auto')
    c.setStrokeColor(RULE); c.setLineWidth(0.7); c.rect(M, y - 70 * mm, iw, 70 * mm, stroke=1, fill=0)
    tx, tw = M + iw + 9 * mm, CW - iw - 9 * mm
    ty = y
    ty = d.para(ty, "Not a developer&rsquo;s promise on a brochure. The Delta State Ministry of Works, Rural "
                    "and Riverine Roads, with RCT Nigeria Ltd as contractor.", body, tw, tx)
    ty = d.para(ty, "The board stands at Atuma-Iga. Photograph it yourself on inspection day and take the "
                    "picture home.", body, tw, tx)
    y = min(y - 74 * mm, ty - 3 * mm)

    y = d.note(y, '<b>Why this matters more than anything we could write.</b> You do not have to believe a '
                  'word of this document to believe that signboard. It is the difference between a promise '
                  'and a fact, and you can verify it without speaking to us at all.', NAVY, WARM)

    y = d.para(y, "Ask any estate to show you something a government agency has committed to in writing. "
                  "Most cannot. That single question will tell you more than an hour of conversation.",
               bodyS, CW * 0.95)
    y = d.pull(y, 'A government does not put up a board for land that is in dispute.',
               'Which is, in the end, the quietest reassurance in this entire document.')
    d.foot()

    # =========================================================== 07 PRICE
    y = d.page('What it costs')
    y = d.kicker(y, 'Against the neighbours')
    y = d.title(y, 'Buy here instead of next door and you keep three million naira.', 27, NAVY, 28)
    y = d.para(y, "That is not a promo we invented for a flyer. It is the gap between our price and what the "
                  "estate down the same road is asking for a <i>smaller</i> plot with the same class of title.",
               bodyS, CW * 0.95)
    y -= 4 * mm

    rows = [("Doctor's Residence, CPAL", '464 SQM   DEED + SURVEY', 'N4.5M', 9700, True),
            ('Another estate at Atuma-Iga', '450 SQM   DEED + SURVEY', 'N7.5M', 16700, False),
            ('An Oshimili North estate', '464 SQM   FULL C OF O', 'N12.5M', 26900, False),
            ('Cubana Millennium City', '560 SQM   FULL C OF O', 'N80M', 142900, False)]
    cap = 30000
    barx = M + 84 * mm
    barw = CW - 84 * mm - 27 * mm
    for name, spec, price, psm, ours in rows:
        c.setStrokeColor(RULE); c.setLineWidth(0.6); c.line(M, y + 9 * mm, W - M, y + 9 * mm)
        c.setFont('Semi', 12.4); c.setFillColor(NAVY if ours else INK)
        c.drawString(M, y + 2.4 * mm, name)
        c.setFont('Mono', 7.8); c.setFillColor(SOFT)
        c.drawString(M, y - 4 * mm, spec + '   ' + price)
        c.setFillColor(colors.HexColor('#E8E4D6')); c.rect(barx, y - 2.6 * mm, barw, 6.4 * mm, stroke=0, fill=1)
        c.setFillColor(GOLD if ours else colors.HexColor('#9FB0CE'))
        c.rect(barx, y - 2.6 * mm, barw * min(psm / cap, 1.0), 6.4 * mm, stroke=0, fill=1)
        if psm > cap:
            c.setFont('Mono', 6.4); c.setFillColor(WHITE)
            c.drawRightString(barx + barw - 2 * mm, y - 0.9 * mm, 'OFF SCALE')
        c.setFont('MonoB', 9.4); c.setFillColor(NAVY if ours else SOFT)
        c.drawRightString(W - M, y - 0.8 * mm, f'N{psm:,}')
        y -= 17 * mm

    c.setFont('Mono', 7.6); c.setFillColor(SOFT)
    c.drawRightString(W - M, y + 7 * mm, 'PER SQUARE METRE')
    y -= 3 * mm

    y = d.note(y, '<b>Three million naira is not an abstraction.</b> It is your fence and your gate. It is a '
                  'year of school fees. It is the foundation you would otherwise be waiting another two years '
                  'to afford. Buying here does not just cost less, it moves your build forward.', GOLD, WHITE)
    y = d.pull(y, 'Search "Atuma-Iga land" and compare us yourself.',
               'We are not asking you to take our word for the cheapest number in this pack.')
    d.foot()

    # =========================================================== 08 PRICE II
    y = d.page('What it costs')
    y = d.kicker(y, 'The honest part')
    y = d.title(y, 'Why we are cheaper, said plainly.', 27, INK, 28)

    y = d.para(y, "We are new. We are building a name in Asaba, and we would rather you tell three people "
                  "about us than pay us an extra two million.", body, CW * 0.95)
    y = d.para(y, "There is a second reason, and we are not going to hide it from you.", body, CW * 0.95)

    y = d.note(y, '<b>Our estate-wide C of O is still in view, and our internal infrastructure is not built '
                  'yet.</b> Estates that already hold a full C of O reasonably charge more than we do. You are '
                  'buying earlier, at a lower price, with more still outstanding. That is the trade. We would '
                  'rather put it in front of you than let you find it out later.',
               LATERITE, RUSTBG)

    y -= 1 * mm
    c.setFont('MonoB', 9); c.setFillColor(NAVY); c.drawString(M, y, 'WHAT THE N4.5M ALREADY COVERS'); y -= 12 * mm
    for lb, vl in [('Deed of Assignment', 'Included'), ('Registered survey plan', 'Included'),
                   ('Plot demarcation and beacons', 'Included'),
                   ('A second bill for papers later', 'None')]:
        c.setStrokeColor(RULE); c.setLineWidth(0.6); c.line(M, y + 6.6 * mm, W - M, y + 6.6 * mm)
        c.setFont('Body', 14); c.setFillColor(INK); c.drawString(M, y, lb)
        c.setFont('MonoB', 9); c.setFillColor(GREEN if vl == 'Included' else LATERITE)
        c.drawRightString(W - M, y, vl.upper())
        y -= 11.5 * mm

    y -= 4 * mm
    c.setFillColor(NAVY); c.rect(M, y - 24 * mm, CW, 24 * mm, stroke=0, fill=1)
    c.setFont('Disp', 17); c.setFillColor(WHITE)
    c.drawString(M + 8 * mm, y - 11 * mm, 'Same road. Bigger plot. Three million less.')
    c.setFont('Mono', 7.6); c.setFillColor(GOLD_SOFT)
    c.drawString(M + 8 * mm, y - 18 * mm, 'GO AND CHECK IT YOURSELF, THEN COME AND WALK THE LAND.')
    d.foot()

    # =========================================================== 09 PAYMENT
    y = d.page('Payment')
    y = d.kicker(y, 'How you can start')
    y = d.title(y, 'Start with N500,000. Finish at your own pace.', 27, NAVY, 28)
    y = d.para(y, "You do not need four and a half million naira sitting in an account today. You need five "
                  "hundred thousand and a decision.", bodyS, CW * 0.95)
    y -= 3 * mm

    y = d.benefit(y, 'No fixed monthly instalment',
                  'Pay what you can, when it comes. If your income arrives in irregular amounts, and for most '
                  'people it does, you are not tied to a debit date that ignores how you actually earn.')
    y = d.benefit(y, 'Six months to clear the balance',
                  'Long enough to be realistic, short enough that the plot is genuinely yours rather than '
                  'reserved indefinitely while somebody else waits behind you.')
    y = d.benefit(y, 'You can walk away and get most of it back',
                  'If you change your mind, your payment is refunded less a 20 percent administrative fee. '
                  'Allow three weeks. You are not trapped by a deposit.')
    y = d.pull(y, 'The plot stops being an idea the day you pay the first N500,000.',
               'Everything after that is just finishing what you started.')
    d.foot()

    # =========================================================== 10 PAYMENT TERMS
    y = d.page('Payment')
    y = d.kicker(y, 'The terms in full')
    y = d.title(y, 'Including the one that costs you money.', 27, INK, 28)
    y -= 1 * mm

    for lb, vl in [('Outright', 'N4,500,000'),
                   ('Minimum deposit', 'N500,000'),
                   ('Monthly schedule', 'None. Pay as you can.'),
                   ('Deadline', 'Six months'),
                   ('Past six months', '5% of price, per month'),
                   ('Withdrawal', 'Full payment less 20%'),
                   ('Refund time', 'Three weeks')]:
        y = d.row(y, lb, vl, lw=52 * mm)
    y -= 4 * mm

    y = d.note(y, '<b>What the late penalty really costs.</b> Five percent of N4,500,000 is N225,000 for every '
                  'month you run past the six-month deadline. That is a serious number and we have put it in '
                  'large type instead of small print. If six months looks tight for your situation, tell us '
                  'before you pay the deposit, not after.', LATERITE, RUSTBG)

    y = d.para(y, "Every line above appears in the agreement you sign before any money moves. Read it. Ask "
                  "about anything that is not clear. A question costs you nothing today and could save you a "
                  "great deal later.", bodyS, CW * 0.95)
    y = d.pull(y, 'We put the penalty on its own page rather than in a footnote.',
               'Companies that bury this clause are relying on you not finding it. We are relying on you '
               'clearing the balance.')
    d.foot()

    # =========================================================== 11 GROUND TRUTH
    y = d.page('On the ground', dark=True)
    y = d.kicker(y, 'Standing there today', dark=True)
    y = d.title(y, 'Finished, and not finished.', 28, WHITE, 28)
    y = d.para(y, "Most estate marketing shows you a rendering of a gate house that does not exist. We keep "
                  "the two lists apart, because you are going to find out either way.", bodyW, CW * 0.95)
    y -= 4 * mm

    cw2 = (CW - 12 * mm) / 2
    c.setFont('MonoB', 9); c.setFillColor(colors.HexColor('#6BCB93')); c.drawString(M, y, 'ON SITE NOW')
    c.setFillColor(colors.HexColor('#E09472')); c.drawString(M + cw2 + 12 * mm, y, 'PLANNED, NOT BUILT')
    y -= 12 * mm

    L = [('Power', '33KVA transformer'), ('Lighting', 'NDDC commissioned'),
         ('Internal road', 'State, under construction'), ('Access', 'Graded into the estate')]
    R = [('Gate house', 'Planned'), ('Security', 'Planned'),
         ('Pipe-borne water', 'Planned'), ('Sports facility', 'Planned')]
    yy = y
    for (la, lb), (ra, rb) in zip(L, R):
        for x, a, b, dim in [(M, la, lb, False), (M + cw2 + 12 * mm, ra, rb, True)]:
            c.setStrokeColor(DRULE); c.setLineWidth(0.6)
            c.line(x, yy + 6.6 * mm, x + cw2, yy + 6.6 * mm)
            c.setFont('Mono', 8.4); c.setFillColor(DSOFT); c.drawString(x, yy + 3 * mm, a.upper())
            c.setFont('Body', 13.4); c.setFillColor(DSOFT if dim else colors.HexColor('#EDF1F8'))
            c.drawString(x, yy - 3.4 * mm, b)
        yy -= 16 * mm
    y = yy - 3 * mm

    y = d.note(y, 'When something on the right is finished, it moves to the left, and this page changes. '
                  'Nothing gets quietly promoted before it is real.', GOLD, colors.HexColor('#0A1838'), noteW)
    y = d.pull(y, 'You will never be surprised by this estate.',
               'What is built is on the left. What is coming is on the right. That is the whole system.',
               dark=True)
    d.foot(dark=True)

    # =========================================================== 12 WHY HERE
    y = d.page('Why here', dark=True)
    y = d.kicker(y, 'Facts, not forecasts', dark=True)
    y = d.title(y, 'Asaba moved. This is where it moved to.', 28, WHITE, 28)
    y -= 1 * mm

    y = d.benefit(y, 'The Second Niger Bridge is finished',
                  'A 1.63km crossing built between 2018 and 2023 at a cost of N336 billion, with 46.9km of '
                  'link roads joining Asaba to Onitsha. When it opened, the federal works minister noted '
                  'publicly that property values on both sides had risen sharply. That is a matter of record.',
                  dark=True)
    y = d.benefit(y, 'Your access road is a live state contract',
                  'Delta State Ministry of Works, Rural and Riverine Roads. The board is on site and '
                  'photographed in this pack.', dark=True)
    y = d.benefit(y, 'Other developers came here first',
                  'Atuma-Iga now carries several estates from different companies. Independent developers do '
                  'not commit money to the same village by coincidence. You are not being asked to bet on an '
                  'area nobody else believes in.', dark=True)

    y = d.para(y, "<i>We will not quote you a return, a percentage, or a projected value. Nobody can honestly "
                  "promise those, and the companies that do are the ones you read about later. We point at "
                  "what already exists and let you decide what it is worth.</i>",
               ParagraphStyle('i', parent=bodyW, fontSize=13.2, leading=19, textColor=DSOFT), CW * 0.95)
    d.foot(dark=True)

    # =========================================================== 13 BUYING
    y = d.page('How buying works')
    y = d.kicker(y, 'The sequence')
    y = d.title(y, 'Four steps. Payment is never the first one.', 27, NAVY, 28)
    y = d.para(y, "You can stop at any point before step three and nothing has happened. That is deliberate.",
               bodyS, CW * 0.95)
    y -= 3 * mm

    y = d.benefit(y, 'Inspect the land', 'Monday, Thursday or Saturday. If you are abroad or upcountry, we '
                  'walk the plot on a live video call and you direct the camera. Ask for the beacon. Ask to '
                  'see the transformer. Record the call. We would prefer that you did.', num='01')
    y = d.benefit(y, 'Confirm the plot and the terms', 'You choose the plot and the payment route, and we put '
                  'it in writing before any money moves. Send the documents to your own lawyer or surveyor '
                  'first. Take your time.', num='02')
    y = d.benefit(y, 'Pay the corporate account', 'Chuks Properties Academy Limited only. Never an individual. '
                  'Never a representative. Never a realtor, however well you know them.', num='03')
    y = d.benefit(y, 'Receive your documentation', 'Deed of Assignment and registered survey plan on '
                  'allocation, in your name. Then it is yours, and it stays yours.', num='04')
    d.foot()

    # =========================================================== 14 FRAUD WARNING
    y = d.page('How buying works')
    y = d.kicker(y, 'Protect yourself')
    y = d.title(y, 'The scam that catches good people.', 27, LATERITE, 28)

    y = d.para(y, "It is almost never a fake estate. It is a real estate, a real plot, and a fake account "
                  "number forwarded in a WhatsApp status or a group chat.", body, CW * 0.95)
    y = d.para(y, "The buyer pays. The money is gone. The company never received a naira and cannot help.",
               body, CW * 0.95)

    y = d.note(y, '<b>So here is our rule, and it protects you from us as much as from anybody else.</b> CPAL '
                  'account details are confirmed to you directly by our office, on a recorded call or in '
                  'writing. If anyone sends you account details any other way, stop and call 0806 789 8622 '
                  'first. This applies even if the person sending it is a CPAL realtor you know and like.',
               LATERITE, RUSTBG)

    y -= 1 * mm
    c.setFont('MonoB', 9); c.setFillColor(NAVY); c.drawString(M, y, 'WHAT YOU RECEIVE, AND WHEN'); y -= 12 * mm
    for lb, vl in [('On signing', 'Written terms, in your name'),
                   ('On allocation', 'Deed and registered survey plan'),
                   ('On request', 'Beacons shown to you on site'),
                   ('In progress', 'C of O status, whenever you ask')]:
        y = d.row(y, lb, vl, lw=44 * mm)
    y = d.pull(y, 'One phone call is all it takes to never be that story.',
               'Call 0806 789 8622 and confirm before you send anything to anybody.')
    d.foot()

    # =========================================================== 15 CHAIRMAN
    y = d.page('Who is behind CPAL')
    y = d.kicker(y, 'Leadership')
    y = d.title(y, 'Dr Chukwuma Agba', 32, NAVY, 32)
    c.setFont('MonoB', 9); c.setFillColor(SOFT)
    c.drawString(M, y + 2 * mm, 'FOUNDER AND CHAIRMAN   THE PROPERTY DOCTOR')
    y -= 11 * mm

    iw = 64 * mm
    c.drawImage(CHAIR, M, y - 82 * mm, width=iw, height=82 * mm, mask='auto')
    c.setStrokeColor(RULE); c.setLineWidth(0.7); c.rect(M, y - 82 * mm, iw, 82 * mm, stroke=1, fill=0)
    tx, tw = M + iw + 9 * mm, CW - iw - 9 * mm
    ty = y
    for t in ["A decade in Nigerian real estate. He founded CPAL on one argument, the one running through "
              "this whole document: that the way to sell Nigerian land is to make every claim checkable "
              "before anybody is asked to pay.",
              "Author of <i>Doctor Sales Formula</i>. He read physics at the Federal University of "
              "Technology, Owerri, hails from Ideato South in Imo State, and is a family man with three "
              "children."]:
        ty = d.para(ty, t, ParagraphStyle('t', parent=body, fontSize=13.6, leading=19.6), tw, tx)
    y = min(y - 86 * mm, ty - 3 * mm)

    y = d.note(y, '<b>He does not hide behind the company.</b> If anything in this pack turns out to be wrong, '
                  'you have a name, a face, and an office address in Asaba you can walk into. That is not true '
                  'of most companies selling land in this market, and it is the whole point.', GOLD, WHITE)
    y = d.pull(y, 'A name you can hold responsible is worth more than a slogan.',
               'Emegoz Plaza, beside Ezenei Junction, Asaba. The door is a real door.')
    d.foot()

    # =========================================================== 16 TV + VIDEO
    y = d.page('Who is behind CPAL')
    y = d.kicker(y, 'On the record')
    y = d.title(y, 'Delta State Television, not a paid advert.', 27, INK, 28)

    tvw = CW * 0.56
    tvh = tvw * 445 / 950
    c.drawImage(TV, M, y - tvh, width=tvw, height=tvh, mask='auto')
    c.setStrokeColor(RULE); c.setLineWidth(0.7); c.rect(M, y - tvh, tvw, tvh, stroke=1, fill=0)
    ty = d.para(y, "Dr Agba on <i>Morning Ride</i>, Delta Broadcasting Service.", body,
                CW - tvw - 9 * mm, M + tvw + 9 * mm)
    ty = d.para(ty, "Go and look for the broadcast yourself rather than taking our word for it.",
                bodyS, CW - tvw - 9 * mm, M + tvw + 9 * mm)
    y = min(y - tvh, ty) - 10 * mm

    c.setStrokeColor(RULE); c.setLineWidth(0.6); c.line(M, y, W - M, y); y -= 12 * mm
    y = d.title(y, 'Watch the estate before you visit it.', 24, NAVY, 25)
    y = d.para(y, "Four films from Atuma-Iga: the launch of Doctor&rsquo;s Residence, prayers on launch "
                  "morning, the development going up around the site, and how clients are received on "
                  "inspection day.", body, CW * 0.95)
    y = d.para(y, "Ask your CPAL representative to send the links, or find them at cpalgroup.com.",
               bodyS, CW * 0.95)
    y = d.pull(y, 'Then come and stand on it.',
               'A video is useful. Your own two feet on your own plot settles it.')
    d.foot()

    # =========================================================== 17 CLOSE
    y = d.page('Come and see it', dark=True)
    y = d.kicker(y, 'Inspection', dark=True)
    for line, col in [('The land is there.', WHITE), ('The road is being built.', WHITE),
                      ('Your name is the', WHITE), ('only thing missing.', GOLD)]:
        c.setFont('Disp', 30); c.setFillColor(col); c.drawString(M, y, line); y -= 30
    y -= 8 * mm

    y = d.para(y, "Inspections run Mondays, Thursdays and Saturdays. Drive out, or send whoever you trust. "
                  "If you are outside Nigeria we schedule a live video walk around your time zone.",
               bodyW, CW * 0.95)
    y -= 2 * mm

    for lb, vl in [('Inspections', 'Mon, Thu, Sat'),
                   ('Virtual', 'Live video, your time zone'),
                   ('Phone & WhatsApp', '0806 789 8622'),
                   ('Second line', '0902 931 2069'),
                   ('Email', 'cpalrealities@gmail.com'),
                   ('Website', 'cpalgroup.com'),
                   ('Office', 'Emegoz Plaza, Ezenei Junction, Asaba')]:
        y = d.row(y, lb, vl, dark=True, lw=48 * mm)

    y -= 3 * mm
    c.setStrokeColor(DRULE); c.setLineWidth(0.6); c.rect(M, y - 23 * mm, CW, 23 * mm, stroke=1, fill=0)
    c.setFont('MonoB', 8.6); c.setFillColor(GOLD_SOFT)
    c.drawString(M + 7 * mm, y - 8.5 * mm, 'YOUR CPAL REPRESENTATIVE')
    c.setStrokeColor(colors.HexColor('#3A4767')); c.setLineWidth(0.6)
    c.line(M + 7 * mm, y - 16.5 * mm, M + CW * 0.55, y - 16.5 * mm)
    c.line(M + CW * 0.60, y - 16.5 * mm, W - M - 7 * mm, y - 16.5 * mm)
    c.setFont('Mono', 7); c.setFillColor(DSOFT)
    c.drawString(M + 7 * mm, y - 20.5 * mm, 'NAME')
    c.drawString(M + CW * 0.60, y - 20.5 * mm, 'PHONE')

    c.setFillColor(NAVY); c.rect(0, 14 * mm, W, 27 * mm, stroke=0, fill=1)
    c.setFont('Disp', 19); c.setFillColor(WHITE)
    c.drawCentredString(W / 2, 30 * mm, 'Book an inspection:  0806 789 8622')
    c.setFont('Mono', 7); c.setFillColor(GOLD_SOFT)
    c.drawCentredString(W / 2, 24 * mm, 'LAND IS SOLD AS OWNERSHIP. CPAL DOES NOT OFFER INVESTMENT RETURNS.')
    c.drawCentredString(W / 2, 19.5 * mm, 'CORRECT AS AT AUGUST 2026. CONFIRM CURRENT DETAILS WITH THE OFFICE.')
    d.n += 1
    c.setFont('Mono', 8); c.setFillColor(DSOFT)
    c.drawRightString(W - M, 9.4 * mm, f'{d.n:02d}')

    c.save()
    print('built', out)


if __name__ == '__main__':
    build('/home/claude/cpal/assets/docs/doctors-residence-prospect-pack.pdf')
