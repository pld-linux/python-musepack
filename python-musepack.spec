%define		module	pymusepack
Summary:	A Python module for the Musepack library
Summary(pl):	Modu� Pythona do biblioteki Musepack
Name:		python-%{module}
Version:	0.4
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	e534739c46f8b71a147faa600bed9405
URL:		http://www.sacredchao.net/~piman/
BuildRequires:	libmpcdec-devel
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for the the Musepack library.

%description -l pl
Modu� Pythona do biblioteki Musepack.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%{py_sitedir}/musepack
%attr(755,root,root) %{py_sitedir}/musepack/*.so
