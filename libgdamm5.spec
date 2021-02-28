# TODO:
# - package examples
#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
%bcond_without	static_libs	# don't build static library

Summary:	C++ wrappers for libgda 5.x
Summary(pl.UTF-8):	Interfejsy C++ dla libgda 5.x
Name:		libgdamm5
Version:	4.99.11
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/4.99/libgdamm-%{version}.tar.xz
# Source0-md5:	c36682e4dd633f78f7d53404149edfea
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	glibmm-devel >= 2.46.1
BuildRequires:	libgda5-devel >= 5.0.2
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.46.1
Requires:	libgda5 >= 5.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgda 5.x.

%description -l pl.UTF-8
Interfejsy C++ dla libgda 5.x.

%package devel
Summary:	Header files for libgdamm5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdamm5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.46.1
Requires:	libgda5-devel >= 5.0.2

%description devel
Header files for libgdamm5 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgdamm5.

%package static
Summary:	Static libgdamm5 library
Summary(pl.UTF-8):	Statyczna biblioteka libgdamm5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdamm5 library.

%description static -l pl.UTF-8
Statyczna biblioteka libgdamm5.

%package apidocs
Summary:	libgdamm 5 API documentation
Summary(pl.UTF-8):	Dokumentacja API libgdamm 5
Group:		Documentation
BuildArch:	noarch

%description apidocs
libgdamm 5 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgdamm 5.

%prep
%setup -q -n libgdamm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	%{!?with_apidocs:--disable-documentation} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgdamm-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdamm-5.0.so.13

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdamm-5.0.so
%{_libdir}/libgdamm-5.0
%{_includedir}/libgdamm-5.0
%{_pkgconfigdir}/libgdamm-5.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdamm-5.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/libgdamm-5.0
%{_docdir}/libgdamm-5.0
%endif
