Name:		texlive-wtref
Version:	69214
Release:	1
Summary:	Extend LaTeX's cross-reference system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wtref
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wtref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wtref.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends the cross-reference system of LaTeX2e and
introduces concepts of namespace and scope. It also allows
users to customize reference formats. The package is part of
the WT Series. Prerequisite packages: xparse and xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/wtref
%doc %{_texmfdistdir}/doc/latex/wtref

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
