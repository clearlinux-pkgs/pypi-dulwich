#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
# Source0 file verified with key 0x306F216180425066 (jelmer@jelmer.uk)
#
Name     : pypi-dulwich
Version  : 0.21.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/53/a8/c96686cd8e2b0875dbd7d3248c158ff07f2c0ce41857700711a92e97b463/dulwich-0.21.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/a8/c96686cd8e2b0875dbd7d3248c158ff07f2c0ce41857700711a92e97b463/dulwich-0.21.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/53/a8/c96686cd8e2b0875dbd7d3248c158ff07f2c0ce41857700711a92e97b463/dulwich-0.21.3.tar.gz.asc
Summary  : Python Git Library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: pypi-dulwich-bin = %{version}-%{release}
Requires: pypi-dulwich-license = %{version}-%{release}
Requires: pypi-dulwich-python = %{version}-%{release}
Requires: pypi-dulwich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(urllib3)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Dulwich
=======
This is the Dulwich project.
It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

%package bin
Summary: bin components for the pypi-dulwich package.
Group: Binaries
Requires: pypi-dulwich-license = %{version}-%{release}

%description bin
bin components for the pypi-dulwich package.


%package license
Summary: license components for the pypi-dulwich package.
Group: Default

%description license
license components for the pypi-dulwich package.


%package python
Summary: python components for the pypi-dulwich package.
Group: Default
Requires: pypi-dulwich-python3 = %{version}-%{release}

%description python
python components for the pypi-dulwich package.


%package python3
Summary: python3 components for the pypi-dulwich package.
Group: Default
Requires: python3-core
Provides: pypi(dulwich)
Requires: pypi(urllib3)

%description python3
python3 components for the pypi-dulwich package.


%prep
%setup -q -n dulwich-0.21.3
cd %{_builddir}/dulwich-0.21.3
pushd ..
cp -a dulwich-0.21.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685560395
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dulwich
cp %{_builddir}/dulwich-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-dulwich/9e9b8604dc428d3f50acf86a2e36d56e008672d6 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dul-receive-pack
/usr/bin/dul-upload-pack
/usr/bin/dulwich

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dulwich/9e9b8604dc428d3f50acf86a2e36d56e008672d6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
