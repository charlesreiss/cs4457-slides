\ProvidesClass{mytalk2}[2025/08/21 version 0.04]
\NeedsTeXFormat{LaTeX2e}
\LoadClass[font-size=14pt]{ltx-talk}
\newcommand{\titlepage}[0]{}
\RequirePackage{fancyvrb}
\RequirePackage{pdfcomment}
\RequirePackage{tikz}
\RequirePackage{comment}
\RequirePackage{listings}
\RequirePackage{contour}
\RequirePackage{emoji}
\RequirePackage{sourcecodepro}
\RequirePackage{hyperref}
\geometry{lmargin=1cm,rmargin=1cm}
\tikzset{
    my callout/.style={draw,fill=blue!20!white,rectangle callout,callout absolute pointer=(pic cs:#1),below right=5pt of {pic cs:#1}},
    my callout2/.style={draw,fill=blue!20!white,rectangle callout,callout absolute pointer=(#1),below right=5pt of {#1}},
    ampersand replacement=\&,
    invisible/.style={opacity=0},
    visible on/.style={beameralt=#1{}{invisible}},
    alt/.code args={<#1>#2#3}{%
      \alt<#1>{\pgfkeysalso{#2}}{\pgfkeysalso{#3}} % \pgfkeysalso doesn't change the path
    },
    slidealt/.code args={<#1>#2#3}{%
      \alt<#1>{\pgfkeysalso{#2}}{\pgfkeysalso{#3}} % \pgfkeysalso doesn't change the path
    },
    beameralt/.code args={<#1>#2#3}{%
      \alt<#1>{\pgfkeysalso{#2}}{\pgfkeysalso{#3}} % \pgfkeysalso doesn't change the path
    },
    tight matrix node/.style={draw,rectangle,inner sep=1pt, outer sep=0pt,text width=1cm,minimum height=.4cm,anchor=center},
    tight matrix node noline/.style={rectangle,inner sep=1pt, outer sep=0pt,text width=1cm,minimum height=.4cm,anchor=center},
    tight matrix/.style={
        matrix of nodes,
        inner sep=1pt, outer sep=0pt,
        row sep=-\pgflinewidth,
        column sep=-\pgflinewidth,
        nodes={tight matrix node},
    },
    tight matrix no line/.style={
        matrix of nodes,
        inner sep=1pt, outer sep=0pt,
        row sep=-\pgflinewidth,
        column sep=-\pgflinewidth,
        nodes={tight matrix node noline},
    },
}
\NewDocumentCommand\myemph{D<>{all} +m}{\begingroup\only<#1>{\color{red!50!orange}\ifmmode\relax\else\itshape\fi}#2\endgroup}
\AddToHook{begindocument/before}{
    \EditInstance{item}{basic}
    { label-format =,
      label-boxed = false,
    }
    %\setlength\leftmargini{1em}%
    %\setlength\itemsep{1cm}
    \EditInstance{blockenv}{itemize}{ setup-code=\setlength\itemsep{0.75em} }
    %\ShowInstance
}

\newcommand{\myalttext}[2]{%
\pdftooltip{#1}{#2}%
}
\newcommand{\myalttextB}[3]{%
\only<1>{\pdftooltip{#1}{#2}}%
\only<2->{\pdftooltip{#1}{#3}}%
}

\newcommand{\myalttextC}[4]{%
\only<1>{\pdftooltip{#1}{#2}}%
\only<2>{\pdftooltip{#1}{#3}}%
\only<3->{\pdftooltip{#1}{#3}}%
}

\newcommand{\myalttextD}[5]{%
\only<1>{\pdftooltip{#1}{#2}}%
\only<2>{\pdftooltip{#1}{#3}}%
\only<3>{\pdftooltip{#1}{#3}}%
\only<4->{\pdftooltip{#1}{#4}}%
}

\NewEnvironmentCopy{FragileFrame}{frame*}

\usepackage{ifluatex}
\ifluatex
    \def\EmptyMapping{}
\else
    \def\EmptyMapping{\addfontfeatures{Mapping=}}
\fi

