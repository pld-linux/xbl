Summary:	3D geometry game
Summary(de):	3D-Geometriespiel
Summary(es):	Juego geom�trico en 3D
Summary(fr):	Jeu en g�ometrie 3D.
Summary(pl):	Tr�jwymiarowa gra na zasadach tetrisa
Summary(pt_BR):	Jogo geom�trico em 3d
Summary(tr):	�� boyutlu geometri oyunu
Name:		xbl
Version:	1.0j
Release:	8
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp710.univ-lyon1.fr/pub/xbl/%{name}-%{version}.tar.Z
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
URL:		http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A three dimensional version of a popular arcade game.

%description -l es
Una versi�n en tres dimensiones de un popular juego del tipo arcade.

%description -l de
Eine 3D-Version eines beliebten Spielhallen-Games.

%description -l fr
Version tri-dimensionnelle d'un c�l�bre jeu d'arcade.

%description -l pl
Tr�jwymiarowa wersja popularnej gry.

%description -l pt_BR
Uma vers�o em tr�s dimens�es de um popular jogo do tipo arcade.

%description -l tr
Pop�ler oyunun �� boyutlu bir s�r�m�.

%prep
%setup -q
%patch -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xbl-README
%attr(2755,root,games) %{_bindir}/xbl
%{_libdir}/X11/app-defaults/*
%{_mandir}/man6/xbl.6*
%{_applnkdir}/Games/xbl.desktop
%{_pixmapsdir}/*
# score files are owner by first player - so don't allow him to modify...
%attr(770,root,games) %dir /var/games/xbl
