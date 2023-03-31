Name:		texlive-elegantpaper
Version:	62989
Release:	2
Summary:	An Elegant LaTeX Template for Working Papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elegantpaper
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantpaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantpaper.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ElegantPaper is designed for writing working papers, especially
for economics students. This template is based on the standard
LaTeX article class. The goal of this template is to make the
writing process easier and more comfortable.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/elegantpaper
%doc %{_texmfdistdir}/doc/latex/elegantpaper

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
