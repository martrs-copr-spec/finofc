%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname lml

Name:           python-lml
Version:        0.2.0
Release:        2%{?dist}
Summary:        Load me later: A lazy plugin management system
License:        New BSD
URL:            https://github.com/python-lml/lml
Source0:        https://github.com/python-lml/lml/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-isort

%{?python_enable_dependency_generator}


%define _description %{expand:
lml seamlessly finds the lml based plugins from your current python
environment but loads your plugins on demand. It is designed to support
plugins that have external dependencies, especially bulky and/or
memory hungry ones. lml provides the plugin management system only and the
plugin interface is on your shoulder.
}
%description
%_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m nose


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE  CHANGELOG.rst CONTRIBUTORS.rst
%doc README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue Mar 18 2025 Martin RS - 0.2.0
- Initial
