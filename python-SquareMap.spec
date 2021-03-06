%define 	module	SquareMap
Summary:	Hierarchic visualization control for wxPython
Summary(pl.UTF-8):	Element grafiki wxPython do ilustrowania hierarchii
Name:		python-%{module}
Version:	1.0.3
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	adefc74e38f16dfdcb223108a56fbe46
URL:		http://pypi.python.org/pypi/SquareMap/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
#Requires:		python-libs
Requires:	python-modules
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hierarchic data visualization control intended for use with structures
where "parents" hold collections of weighted children.

%description -l pl.UTF-8
Element grafiki służący do reprezentowania struktur danych gdzie
"rodzice" zawierają zbiory dzieci o różnej wadze.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitescriptdir}/squaremap
%{py_sitescriptdir}/squaremap/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
