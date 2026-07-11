%global tl_name wtref
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Extend LaTeXs cross-reference system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wtref
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wtref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wtref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the cross-reference system of LaTeX2e and
introduces concepts of namespace and scope. It also allows users to
customize reference formats. Prerequisite packages: xparse and xkeyval.

