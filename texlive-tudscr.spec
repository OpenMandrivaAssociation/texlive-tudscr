Name:		texlive-tudscr
Version:	64085
Release:	2
Summary:	Typeset documents in the corporate style of TU Dresden
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tudscr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides classes and packages, whose aim is to
typeset LaTeX documents in the Corporate Design of the
Technische Universitat Dresden. It bases on the KOMA-Script
document classes. The fonts Univers and DIN-Bold are necessary.
(The fonts are available on request for staff and students of
the Technische Universitat Dresden.) The bundle offers: the
three document classes tudscrartcl, tudscrreprt and tudscrbook
which serve as drop-in replacements for scrartcl, scrreprt and
scrreprt. the package tudscrsupervisor, which provides
environments and macros to create tasks, evaluations and
notices for scientific theses, the package mathswap for
swapping math delimiters within numbers (cf. ionumbers), and
the package twocolfix that the position of headings in two
column layout.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tudscr
%doc %{_texmfdistdir}/doc/latex/tudscr
#- source
%doc %{_texmfdistdir}/source/latex/tudscr

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
