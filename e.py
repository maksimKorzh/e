#!/bin/python3
import curses as u,time,sys,os;os.environ['ESCDELAY']='10'
def m(stdscr):
  s=u.initscr();s.nodelay(1);u.noecho();u.raw();s.keypad(1);u.use_default_colors()
  v={'b':[],'r':0,'c':0,'i':0,'m':'N','x':0,'y':0,'R':0,'C':0,'s':s,'f':'out.txt','u':u,
  104:'if c>0:c-=1',108:'if c<len(b[r]):c+=1',107:'if r!=0:r-=1',106:'if r<len(b)-1:r+=1',
  100:'if len(b):del b[r];r=r if r<len(b) else r-1 if r-1 >= 0 else 0',36:'c=len(b[r])',
  48:'c=0',21:'r=r-5 if r-5>0 else 0',4:'r=r+5 if r+5<len(b)-1 else len(b)-1',105:'m="I"',
  't':['if i!=((i)&0x1f) and i<128:b[r].insert(c,i);c+=1\nif i==263:\n if c==0 and r!=0:',
  'l=b[r][c:];del b[r];r-=1;c=len(b[r]);b[r]+=l\n elif c:c-=1;del b[r][c]\nif i==10:',
  'l=b[r][c:];b[r]=b[r][:c];r+=1;c=0;b.insert(r,[]+l)'],'p':['R,C=s.getmaxyx();R-=1\n',
  'if r<y:y=r\nif r>=y+R:y=r-R+1\nif c<x:x=c\nif c>=x+C:x=c-C+1\nfor Y in range(R):\n ',
  'for X in range(C):\n  try:s.addch(Y,X,b[Y+y][X+x])\n  except:pass\n s.clrtoeol()\n ',
  'try:s.addch(10)\n except:pass\nu.curs_set(0);s.clrtoeol();s.addstr(R,0,m+" -- "+f+" ',
  '-- Row: "+str(r)+", Col: "+str(c));s.move(r-y,c-x);u.curs_set(1);s.refresh();i=-1'],
  'a':'if not len(b):b=[[]]\nif c>len(b[r]):c=len(b[r])','z':['try:\n with open(f) as i:',
  '\n  c=i.read().split("\\n");c=c[:-1] if len(c)>1 else c\n  for i in c:b.append([ord(c) ',
  'for c in i]);r=len(b)-1;c=len(b[r])\nexcept:b.append([])'],'w':['d=""\nfor l in b:',
  'd+="".join([chr(c) for c in l])+"\\n"\nwith open(f,"w") as i:i.write(d);\ns.clear();',
  's.refresh();import time;time.sleep(0.1)']}
  def w(n):exec(''.join(v['w']),v)
  def r(n):exec(''.join(v['z']),v)
  if len(sys.argv) == 2: v['f'] = sys.argv[1];r(sys.argv[1])
  if len(sys.argv) == 1: v['b'].append([])
  while True:
    try:
      exec(''.join(v['p']), v)
      while (v['i'] == -1): v['i'] = s.getch()
      if v['i'] == 17: break
      if v['i'] == 27: v['m'] = 'N'
      if v['i'] == 23: w(v['f'])
      if v['m'] == 'N': exec(v[v['i']], v)
      elif v['m'] == 'I': exec(''.join(v['t']), v)
      exec(v['a'], v)
    except:pass
u.wrapper(m)
