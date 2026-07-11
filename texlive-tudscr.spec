%global tl_name tudscr
%global tl_revision 64085

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.06o
Release:	%{tl_revision}.1
Summary:	Corporate Design of Technische Universitat Dresden
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tudscr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cbfonts)
Requires:	texlive(environ)
Requires:	texlive(etoolbox)
Requires:	texlive(geometry)
Requires:	texlive(graphics)
Requires:	texlive(greek-inputenc)
Requires:	texlive(iwona)
Requires:	texlive(koma-script)
Requires:	texlive(mathastext)
Requires:	texlive(mweights)
Requires:	texlive(oberdiek)
Requires:	texlive(opensans)
Requires:	texlive(trimspaces)
Requires:	texlive(xcolor)
Requires:	texlive(xpatch)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The TUD-Script bundle provides both classes and packages in order to
create LaTeX documents in the corporate design of the Technische
Universitat Dresden. It bases on the KOMA-Script bundle, which must
necessarily be present. For questions, problems and comments, please
refer to either the LaTeX forum of the Dresden University of Technology
or the GitHub "tudscr" repository. The bundle offers: the three document
classes tudscrartcl, tudscrreprt, and tudscrbook which serve as wrapper
classes for scrartcl, scrreprt, and scrbook, the class tudscrposter for
creating posters, the package tudscrsupervisor providing environments
and macros to create tasks, evaluations and notices for scientific
theses, the package tudscrfonts, which makes the corporate design fonts
of the Technische Universitat Dresden available for LaTeX standard
classes and KOMA-Script classes, the package fix-tudscrfonts, which
provides the same fonts to additional corporate design classes not
related to TUD-Script, the package tudscrcomp, which simplifies the
switch to TUD-Script from external corporate design classes, the package
mathswap for swapping math delimiters within numbers (similar to
ionumbers), the package twocolfix for fixing the positioning bug of
headings in twocolumn layout, and a comprehensive user documentation as
well as several tutorials.

