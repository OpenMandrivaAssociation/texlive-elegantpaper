%global tl_name elegantpaper
%global tl_revision 78191

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12
Release:	%{tl_revision}.1
Summary:	An Elegant LaTeX Template for Working Papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elegantpaper
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantpaper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantpaper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ElegantPaper is designed for writing working papers, especially for
economics students. This template is based on the standard LaTeX article
class. The goal of this template is to make the writing process easier
and more comfortable.

