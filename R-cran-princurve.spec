%define		fversion	%(echo %{version} |tr r -)
%define		modulename	princurve
Summary:	Fits a Principal Curve in Arbitrary Dimension
Summary(pl):	Dopasowywanie krzywej g³ównej w dowolnym wymiarze
Name:		R-cran-%{modulename}
Version:	1.1r7
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	705919e7815e9fc00945030035ab96a5
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fits a principal curve to a data matrix in arbitrary dimensions.

%description -l pl
Dopasowywanie krzywej g³ównej w dowolnym wymiarze.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,ChangeLog}
%{_libdir}/R/library/%{modulename}
