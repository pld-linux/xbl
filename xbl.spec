Summary:	3d geometry game 
Summary(pl):	Trójwymiarowa gra na zasadach tetrisa.
Name:		xbl
Version:	1.0j
Release:	6
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ftp710.univ-lyon1.fr/pub/xbl/%{name}-%{version}.tar.Z
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
Url:		http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A three dimensional version of a popular arcade game.

%prep
%setup -q
%patch -p1 -b .config

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(0755,root,root) %{_prefix}/X11R6/bin/xbl
%config %{_prefix}/X11R6/lib/X11/app-defaults/*
%{_prefix}/X11R6/man/man?/xbl.6*
%dir /var/lib/games/xbl
%config %{_applnkdir}/Games/xbl.desktop
