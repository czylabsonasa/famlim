import sys

thepre=r"""
%usepackage es egyebek
\input{common/alldef.tex}

\begin{document}\begin{spacing}{1.4}
\pagecolor{BGSZ}
"""

thepost=r"""
\end{spacing}
\end{document}
"""




def olvas():
   minden=[]
   for line in sys.stdin:
      #
      # SZÉTSZEDI a sort a #-ok mentén
      arr=line.split('#')
      #print('#',line)
      #
      # a sztringeket EGYSZERŰSÍTI
      arr=[s.strip() for s in arr]
      #print('a:',arr)
      #
      # ha NULLA #-van a sorban (megjegyzés)
      if 1==len(arr):
         continue
      #
      # itt len(arr)>1 teljesül
      #
      # ha ez a ZÁRÓ sora az adott szintnek
      if 0==len(arr[0]):
         #print('m:',minden)
         seged=[]
         while True:
            x=minden.pop()
            if 'T'==x[2] and []==x[3]:
               #print('s:',seged)
               x[3]=seged[::-1]
               minden.append(x)
               break
            seged.append(x)
         continue
      #
      # HIBÁS input
      if len(arr)<3:
         sys.exit('hibás input')
      # NINCS HOSSZÚ név
      if 0==len(arr[1]):
         arr[1]=arr[0]
      #
      minden.append([arr[0], arr[1], arr[2], []])
      #
   # for zárása
   return minden
# end of olvas

minden=olvas()[0]
title=minden[1]


#~ print(minden)
#~ sys.exit('debug')


def kiir(akt, ind):
   if []==akt:
      return
   for elem in akt:
      print(ind+elem[0])
      kiir(elem[3],ind+'  ')

#~ kiir(minden,'')
#~ sys.exit('exit debug')

def travlist(akt, path, lab, plab, mname):
   if []==akt:
      return
   print(r'\section*{{{name}}} \label{{{label}}}'.format(name=mname, label=lab))
   #print(r'Tartalom\newline')
   for elem in akt:
      print(r'\nameref{{{label}}}'.format(label=lab+elem[0]))
      #DBG
      print(' [ '+elem[0]+' '+elem[2]+' ]')
      if elem != akt[-1]:
         print(r'\newline')

   if '' != plab:
      print(r'\vspace{0.5cm}')
      print(r'\LINK{')
      print(r'\hfill\nameref{{{label}}}'.format(label=plab))
      print(r'}')
   print(r'\newpage')

   for elem in akt:
      if [] != elem[3]:
         travlist(elem[3], path+'/'+elem[0], lab+elem[0], lab, elem[1])
      else:
         if 'F'==elem[2]:
            nFa=r"\mtit{Fa}"+elem[1]
            nMo=r"\mtit{Mo}"+elem[1]
            #print(r'\section*{{{name}}} \label{{{label}}}'.format(name=elem[1]+'-Fa', label=lab+elem[0]))
            print(r'\section*{{{name}}} \label{{{label}}}'.format(name=nFa, label=lab+elem[0]))
            print(r'\Fa{')
            print(r'\input{{{mfile}}}'.format(mfile=path+'/'+elem[0]+'Fa'))
            print(r'}')
            print(r'\vspace{0.5cm}')
            print(r'\LINK{')
            print(r'\nameref{{{name}}}'.format(name=lab+elem[0]+'Mo'))
            print(r'\hfill\nameref{{{name}}}'.format(name=lab))
            print(r'}')
            print(r'\newpage')
            #itt is
            print(r'\section*{{{name}}} \label{{{label}}}'.format(name=nMo, label=lab+elem[0]+'Mo'))
            print(r'\Mo{')
            print(r'\input{{{f}}}'.format(f=path+'/'+elem[0]+'Mo'))
            print(r'}')
            print(r'\vspace{0.5cm}')
            print(r'\LINK{')
            print(r'\nameref{{{name}}}'.format(name=lab+elem[0]))
            print(r'\hfill\nameref{{{name}}}'.format(name=lab))
            print(r'}')
            print(r'\newpage')
         else:
            nDesc=r'\mtit{Desc}'+elem[1]
            print(r'\section*{{{name}}} \label{{{label}}}'.format(name=nDesc, label=lab+elem[0]))
            print(r'\Desc{')
            print(r'\input{{{f}}}'.format(f=path+'/'+elem[0]+'Desc'))
            print(r'}')
            print(r'\vspace{0.5cm}')
            print(r'\LINK{')
            print(r'\hfill\nameref{{{name}}}'.format(name=lab))
            print(r'}')
            print(r'\newpage')


print(thepre)
travlist(minden[3],'DB','DB','', title)
print(thepost)
