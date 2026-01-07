%define module bson
%bcond tests 1

Name:		python-bson
Version:	0.5.10
Release:	2
Summary:	BSON codec for Python
URL:		https://github.com/py-bson/bson
License:	Apache-2.0 AND BSD-3-Clause
Group:		Development/Python
Source0:	https://github.com/py-bson/bson/archive/%{version}/%{module}-%{version}.tar.gz

Patch0:		drop-python2.patch
Patch1:		support-py312.patch
Patch2:		fix2038.patch
Patch4:		support-py314.patch

BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(python-dateutil)
%endif
Requires:	python%{pyver}dist(python-dateutil)


%description
BSON codec for Python.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info
sed -i '1 {/^#!/d}' bson/*.py

%patchlist

%build
%py_build

%install
%py_install

%if %{with tests}
%check
%{__python} -m unittest -v
%endif

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
%license LICENSE LICENSE_APACHE
%doc README.rst
