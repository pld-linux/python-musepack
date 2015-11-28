%define		module	pymusepack
Summary:	A Python module for the Musepack library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki Musepack
Name:		python-musepack
Version:	0.4
Release:	6
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	e534739c46f8b71a147faa600bed9405
URL:		http://www.sacredchao.net/~piman/
BuildRequires:	libmpcdec-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
Provides:	python-pymusepack = %{version}-%{release}
Obsoletes:	python-pymusepack <= 0.4-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for the the Musepack library.

%description -l pl.UTF-8
Moduł Pythona do biblioteki Musepack.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py config
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/musepack/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%dir %{py_sitedir}/musepack
%attr(755,root,root) %{py_sitedir}/musepack/*.so
%{py_sitedir}/musepack/*.py[co]
