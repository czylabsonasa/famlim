import sys

def olvas():
   minden=[]
   state=0
   for line in sys.stdin:
      arr=line.split('#')
      #print('#',line)
      arr=[s.strip() for s in arr]
      if 0==state:
         if 0==len(arr[0]):
            continue
         state=1
         egy=[arr[0],arr[1]]
         continue
      if 1==state:
         if 0==len(arr[0]):
            minden+=[egy]
            state=0
            continue
         if 0==len(arr[1]):
            arr[1]=arr[0]
         arr=arr[0:2]
         egy+=[arr]
         continue
   return minden
# end of olvas


thepre=r"""
%usepackage es egyebek
\input{globdef.tex}

%zarojel, FA...
\input{locdef.tex}

% zárójelek; rövidítések \de=differenciálegyenlet
\input{otherdef.tex}

% itt van a feladatok listája
\begin{document}\begin{spacing}{1.2}
"""

thepost=r"""
\end{spacing}
\end{document}
"""


def generate():
   print(d1 + r"\section*{Tartalom} \label{Tart}")
   for tema in minden:
      print(d3 + r"\nameref{{{label}}}\newline".format(label=tema[0]))
   print(d2 + r"\newpage")


   for tema in minden:
      tname=tema[1]
      tlabel=tema[0]
      print(d2 + r"\section*{{{name}}} \label{{{label}}}".format(name=tname, label=tlabel))
      tartlab="Tart"+tlabel
      tartnam="Tartalom-"+tlabel
      print(d2 + r"\section*{{{name}}} \label{{{label}}}".format(name=tartnam, label=tartlab))

      for p in range(2,len(tema)):
         probname=tema[p][1]
         problabel=tlabel+tema[p][0]
         print(d3 + r"\nameref{{{label}}}\newline".format(label=tlabel+tema[p][0]))
      print(d3 + r"\kek{")
      print(d3 + r"\hfill{{}}\nameref{{{label}}}".format(label="Tart"))
      print(d3 + r"}\newpage")



      for p in range(2,len(tema)):
         probname=tema[p][1]
         problabel=tema[p][0]
         if probname==problabel:
            probname=tlabel+"-"+probname
         print(d3 + r"\section*{{{name}}} \label{{{label}}}".format(name=probname, label=tlabel+problabel))
         print(d3 + r"\Fa{")
         print(d4 + r"\input{{DB/{tn}/{pn}Fa}}".format(tn=tlabel, pn=problabel))
         print(d3 + r"}")
         print(d3 + r"\Mo{")
         print(d3 + r"\nameref{{{name}}}".format(name=tlabel+problabel+"Mo"))
         print(d3 + r"\hfill\nameref{{{name}}}".format(name="Tart"+tema[0]))
         print(d3 + r"}")
         print(d3 + r"\newpage")

         print(d3 + r"\section*{{{name}}} \label{{{label}}}".format(name=probname+"-Mo", label=tlabel+problabel+"Mo"))
         print(d3 + r"\Mo{")
         print(d4 + r"\input{{DB/{tn}/{pn}Mo}}".format(tn=tlabel, pn=problabel))
         print(d3 + r"}")
         print(d3 + r"\Fa{")
         print(d3 + r"\nameref{{{name}}}".format(name=tlabel+problabel))
         print(d3 + r"}")
         print(d3 + r"\newpage")


# end of generate()

# main part
# segedek az indenthez (lenyegetelen)
d1="   "
d2=d1+d1
d3=d1+d1+d1
d4=d2+d2


print(thepre)
print(r"""
   \section*{Nevezetes határértékek}
""")

minden=olvas()
generate()
print(thepost)
