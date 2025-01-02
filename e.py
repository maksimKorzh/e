#!/bin/python3
import curses, time, sys
def main(stdscr):
  s = curses.initscr(); s.nodelay(1); curses.noecho(); curses.raw(); s.keypad(1)
  curses.use_default_colors()
  v = {'b': [], 'r': 0, 'c': 0, 'i': 0, 'm': 0, 'x': 0, 'y': 0, 'R': 0, 'C': 0, 's': s, 'curses': curses}
  src = 'noname.txt';
  n = {
    ord('h'): 'if c>0:c-=1',
    ord('l'): 'if c<len(b[r]):c += 1',
    ord('k'): 'if r!=0:r-=1;c=0',
    ord('j'): 'if r<len(b)-1:r+=1;c=0',
    ord('J'): 'l=b[r][c:];del b[r];r-=1;c=len(b[r]);b[r]+=l',
    ord('i'): 'm=1',
    't': [
      'if i!=((i)&0x1f) and i<128:b[r].insert(c,i);c+=1',
      'if i==263 and c:c-=1;del b[r][c]',
      'if i==10:l=b[r][c:];b[r]=b[r][:c];r+=1;c=0;b.insert(r,[]+l)'
    ],
    'v': [
      'R,C = s.getmaxyx()',
      'if r < y: y = r',
      'if r >= y + R: y = r - R+1',
      'if c < x: x = c',
      'if c >= x + C: x = c - C+1',
      'for rw in range(R):',
      '  brw = rw + y',
      '  for cl in range(C):',
      '    bcl = cl + x',
      '    try: s.addch(rw, cl, b[brw][bcl])',
      '    except: pass',
      '  s.clrtoeol()',
      '  try: s.addch(10)',
      '  except: pass',
      'curses.curs_set(0); s.move(r-y, c-x); curses.curs_set(1); s.refresh();i=-1'
    ]
  }
  if len(sys.argv) == 2: src = sys.argv[1]
  try:
    with open(sys.argv[1]) as f:
      cont = f.read().split('\n'); cont = cont[:-1] if len(cont) > 1 else cont
      for rw in cont: v['b'].append([ord(c) for c in rw]); r = len(v['b'])-1; c = len(v['b'][r])
  except: v['b'].append([])
  if len(sys.argv) == 1: v['b'].append([])
  while True:
    s.move(0, 0)
    exec('\n'.join(n['v']), v)
    while (v['i'] == -1): v['i'] = s.getch()
    try:
      if not v['m']: exec(n[v['i']], v)
      elif v['m'] == 1: exec('\n'.join(n['t']), v)
    except: pass

  #  elif ch == curses.KEY_END: c = len(b[r])
  #  elif ch == curses.KEY_HOME: c = 0
  #  elif ch == curses.KEY_PPAGE: r = r-5 if r-5 > 0 else 0
  #  elif ch == curses.KEY_NPAGE: r = r+5 if r+5 < len(b)-1 else len(b)-1
  #  elif ch == curses.KEY_DC and len(b): del b[r]; r = r if r < len(b) else r-1 if r-1 >= 0 else 0
  #  if not len(b): b = [[]]
  #  rw = b[r] if r < len(b) else None; rwlen = len(rw) if rw is not None else 0
  #  if c > rwlen: c = rwlen 
    if v['i'] == (ord('q') & 0x1f): sys.exit()
    if v['i'] == 27: v['m'] = 0
  #  elif ch == (ord('s') & 0x1f):
  #    cont = ''
  #    for l in b: cont += ''.join([chr(c) for c in l]) + '\n'
  #    with open(src, 'w') as f: f.write(cont); s.clear(); s.refresh(); time.sleep(0.1)
curses.wrapper(main)
