# -*- coding: utf-8 -*-
def generate(text_list, attention_list, latex_file, color='red'):
	assert(len(text_list) == len(attention_list))
	word_num = len(text_list)
	with open(latex_file,'w') as f:
		f.write(r'''\documentclass[varwidth]{standalone}
\special{papersize=210mm,297mm}
\usepackage{color}
\usepackage{tcolorbox}
\usepackage{CJK}
\usepackage{adjustbox}
\tcbset{width=0.9\textwidth,boxrule=0pt,colback=red,arc=0pt,auto outer arc,left=0pt,right=0pt,boxsep=5pt}
\begin{document}
\begin{CJK*}{UTF8}{gbsn}'''+'\n')
		string = r'''{\setlength{\fboxsep}{0pt}\colorbox{white!0}{\parbox{0.9\textwidth}{'''+"\n"
		for idx in range(word_num):
			string += "\\colorbox{%s!%s}{"%(color, attention_list[idx])+"\\strut " + text_list[idx]+"} "
		string += "\n}}}"
		f.write(string+'\n')
		f.write(r'''\end{CJK*}
\end{document}''')
#
# zero=['0']

# def list2bigram(mylist):
#     return ['-'.join(mylist[i:(i+2)]) for i in range(0,len(mylist)-1)]
#
# def list2trigram(mylist):
#     return ['-'.join(mylist[i:i+3]) for i in range(0,len(mylist)-2)]

words =\
['gon', 'na', 'have', 'to', 'do', 'another', 'unfollow', 'spree', 'later', 'today', ',', 'yeah', ',', 'those', 'be', 'always', 'fun', '.', 'damn', 'you']



# words=words+list2bigram(zero+words)+list2trigram(zero+words+zero)
# ＃gram才要

attention= \
[0.022435924038290977, 0.022435924038290977, 0.02277553267776966, 0.022435924038290977, 0.022435924038290977, 0.16578030586242676, 0.16578030586242676, 0.16578030586242676, 0.16578030586242676, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435924038290977, 0.022435955703258514, 0.022435924038290977, 0.022435924038290977]

print(len(words))
print(len(attention))

attention=[i*400 for i in attention ]
color = 'red'
generate(words, attention, "sample.tex", color)

print (' '.join(words))