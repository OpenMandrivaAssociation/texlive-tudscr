# revision 33755
# category Package
# catalog-ctan /macros/latex/contrib/tudscr
# catalog-date 2014-04-29 12:01:01 +0200
# catalog-license lppl
# catalog-version 2.01
Name:		texlive-tudscr
Version:	2.01
Release:	3
Summary:	Typeset documents in the corporate style of TU Dresden
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tudscr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tudscr.source.tar.xz
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
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-01.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-01.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-03.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-03.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-07.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-07.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-09.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-09.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-19.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-19.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-21.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-21.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-22.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-22.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-24.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-24.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-25.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-25.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-27.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-27.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-28.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-28.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-30.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/DDC-30.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_HKS41.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_HKS41.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_SW.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_SW.pdf
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_WS.eps
%{_texmfdistdir}/tex/latex/tudscr/logo/TU_Logo_WS.pdf
%{_texmfdistdir}/tex/latex/tudscr/mathswap.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrartcl.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrbase.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrbook.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrcolor.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrcomp.sty
%{_texmfdistdir}/tex/latex/tudscr/tudscrdoc.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrman.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrreprt.cls
%{_texmfdistdir}/tex/latex/tudscr/tudscrsupervisor.sty
%{_texmfdistdir}/tex/latex/tudscr/twocolfix.sty
%doc %{_texmfdistdir}/doc/latex/tudscr/README
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/dissertation.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/document.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/evaluation.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/mathswap.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/notice.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/task.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/examples/thesis.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/tudscr.tex
%doc %{_texmfdistdir}/doc/latex/tudscr/doc/tudscrman.xdy
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/dissertation.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/document.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/evaluation.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/mathswap.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/notice.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/task.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/examples/thesis.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/tudscr.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/tudscr_print.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/tudscrsource.pdf
%doc %{_texmfdistdir}/doc/latex/tudscr/tudscrsource.tex
#- source
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-base.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-color.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-comp.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-doc.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-fields.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-fonts.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-frontmatter.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-layout.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-locale.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-manual.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-mathswap.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-misc.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-pagestyle.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-supervisor.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-title.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-twocolfix.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr-version.dtx
%doc %{_texmfdistdir}/source/latex/tudscr/tudscr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
