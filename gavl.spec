Summary:	GMerlin Audio Video Library
Summary(pl.UTF-8):	Biblioteka audio/video GMerlin
Name:		gavl
Version:	0.2.4
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	ba7989a9344026827b34e797b0a58d87
Patch0:		%{name}-make.patch
URL:		http://gmerlin.sourceforge.net/gavl_frame.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GMerlin Audio Video Library.

%description -l pl.UTF-8
Biblioteka audio/video GMerlin.

%package devel
Summary:	Header files for gavl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gavl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gavl library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki gavl.

%package static
Summary:	Static gavl library
Summary(pl.UTF-8):	Statyczna biblioteka gavl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gavl library.

%description static -l pl.UTF-8
Statyczna biblioteka gavl.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libgavl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgavl.so
%{_libdir}/libgavl.la
%{_libdir}/gavl
%{_includedir}/gavl
%{_pkgconfigdir}/gavl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgavl.a
