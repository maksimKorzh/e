#!/bin/python3
import curses as u;s=u.initscr();s.nodelay(1);u.noecho();u.raw();s.keypad(1)
v=dict(b=[],r=0,c=0,i=0,m='N',x=0,y=0,R=0,C=0,f='o.txt',u=u,s=s);v.update({
104:'if c>0:c-=1',108:'if c<len(b[r]):c+=1',107:'if r!=0:r-=1',106:'if r<len(b)-1:r+=1',
100:'if len(b):del b[r];r=r if r<len(b) else r-1 if r-1>=0 else 0',36:'c=len(b[r])',
48:'c=0',21:'r=r-5 if r-5>0 else 0',4:'r=r+5 if r+5<len(b)-1 else len(b)-1',105:'m="I"',
120:'if len(b[r]):del b[r][c]\nif c and c>len(b[r])-1:c=len(b[r])-1',103:'r=0',71:'r=len(b)-1',
't':['if i!=((i)&0x1f) and i<128:b[r].insert(c,i);c+=1\nif i==263:\n if c==0 and r!=0:l=b[r]',
'[c:];del b[r];r-=1;c=len(b[r]);b[r]+=l\n elif c:c-=1;del b[r][c]\nif i==10:l=b[r][c:];b[r]=',
'b[r][:c];r+=1;c=0;b.insert(r,[]+l)'],'p':['R,C=s.getmaxyx();R-=1\nif r<y:y=r\nif ',
'r>=y+R:y=r-R+1\nif c<x:x=c\nif c>=x+C:x=c-C+1\nfor Y in range(R):\n for X in range(C):',
'\n  try:s.addch(Y,X,b[Y+y][X+x])\n  except:pass\n s.clrtoeol()\n try:s.addch(10)\n except:pass',
'\nu.curs_set(0);s.clrtoeol();s.addstr(R,0,m+" --"+f+"-- "+str(r+1)+":"+str(c+1));s.move(r-y,c-x)',
';u.curs_set(1);s.refresh();i=-1'],'a':['if not len(b):b=[[]]\nif c>len(b[r]):c=len(b[r])'],
'z':['try:\n with open(f) as i:\n  c=i.read().split("\\n");c=c[:-1] if len(c)>1 else c\n  ',
'for i in c:b.append([ord(c) for c in i]);r=len(b)-1;c=len(b[r])\nexcept:b.append([])'],'w':
['d=""\nfor l in b:d+="".join([chr(c) for c in l])+"\\n"\nwith open(f,"w") as i:i.write(d)']})
exec(''.join(['import sys\ndef w(n):','exec("".join(v["w"]),v)\ndef r(n):exec("".join(v["z"]),',
'v)\nif len(sys.argv)==2:v["f"]=sys.argv[1];r(sys.argv[1])\nif len(sys.argv)==1:v["b"].append(',
'[])\nwhile True:\n try:\n  exec("".join(v["p"]),v)\n  while (v["i"]==-1):v["i"]=s.getch()\n  ',
'if v["i"]==17:break\n  if v["i"]==27:v["m"]="N"\n  if v["i"]==23:w(v["f"])\n  if v["m"]=="N":',
'exec(v[v["i"]],v)\n  elif v["m"]=="I":exec("".join(v["t"]),v)\n  exec("".join(v["a"]),v)\n ',
'except:pass']),{'v':v,'s':s});u.endwin()
