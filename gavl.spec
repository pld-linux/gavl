#
# Conditional build:
%bcond_without	apidocs	# without doc
#
Summary:	GMerlin Audio Video Library
Summary(pl.UTF-8):	Biblioteka audio/video GMerlin
Name:		gavl
Version:	1.4.0
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	2752013a817fbc43ddf13552215ec2c0
Patch0:		%{name}-make.patch
Patch1:		%{name}-am.patch
Patch2:		x32.patch
URL:		http://gmerlin.sourceforge.net/gavl_frame.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -ffast-math

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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{!?with_apidocs:--without-doxygen} \
	--with-cpuflags=none
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libgavl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgavl.so.1

%files devel
%defattr(644,root,root,755)
%{?with_apidocs:%doc doc/apiref}
%attr(755,root,root) %{_libdir}/libgavl.so
%{_includedir}/gavl
%{_pkgconfigdir}/gavl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgavl.a
