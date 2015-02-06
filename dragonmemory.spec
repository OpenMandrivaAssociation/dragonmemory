%define	oname	DragonMemory

Name:		dragonmemory
Version:	1.0
Release:	4
Summary:	A memory game where you have to match identical chips
License:	GPLv3
Group:		Games/Boards
URL:		http://dragontech.net/index.php/games-en
Source0:	http://dragontech.net/index.php/games-en?file=tl_files/dragontech/Software/%{oname}/%{oname}-source.tgz
Source1:	dragonmemory.png
Patch0:		dragonmemory-1.0-linuxpath.patch
Patch1:		dragonmemory-1.0-makefile.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

%description
Dragon Memory is a memory game where you have to match identical chips from
a board. The game has very detailed graphics and a lot of levels to play.

%prep
%setup -q -n %{oname}
%patch0 -p1 -b .path
%patch1 -p1 -b .makefile

%build
export CPPFLAGS="%{optflags}"
%make

%install
mkdir -p %{buildroot}%{_gamesbindir}
cp %{name} %{buildroot}%{_gamesbindir}/

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}

cp -r fonts %{buildroot}%{_gamesdatadir}/%{name}/
cp -r gfx %{buildroot}%{_gamesdatadir}/%{name}/
cp -r music %{buildroot}%{_gamesdatadir}/%{name}/
cp -r sounds %{buildroot}%{_gamesdatadir}/%{name}/
cp -r themes %{buildroot}%{_gamesdatadir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dragon Memory
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/128x128/apps/
cp %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

%files
%doc Authors.txt License.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png


%changelog
* Tue Dec 06 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0-2mdv2011.0
+ Revision: 738216
- imported package dragonmemory

