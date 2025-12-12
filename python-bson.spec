%define module bson
%bcond_without test

Name:		python-bson
Version:	0.5.10
Release:	2
Summary:	BSON codec for Python
URL:		https://github.com/py-bson/bson
License:	Apache-2.0 AND BSD-3-Clause
Group:		Development/Python
Source0:	https://github.com/py-bson/bson/archive/%{version}/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(six)
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

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
%{__python} -m unittest -v
%endif

%files
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}*.*-info
%license LICENSE LICENSE_APACHE
%doc README.rst
