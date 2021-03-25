#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		_enable_debug_packages	0

Summary:	Benchmark - measure/compare run-time of OCaml functions
Summary(pl.UTF-8):	Biblioteka benchmark - mierzenie i porównywanie czasu działania funkcji ocamlowych
Name:		ocaml-benchmark
Version:	1.6
Release:	1
License:	LGPL v3 with linking exception
Group:		Development/Languages
Source0:	https://github.com/Chris00/ocaml-benchmark/archive/%{version}/benchmark-%{version}.tar.gz
# Source0-md5:	3e716610143aeda29bace893ae3b056b
URL:		https://github.com/Chris00/ocaml-benchmark
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-findlib
%requires_eq	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Benchmark provides functions to measure and compare the run-time of
OCaml functions. It is inspired by the Perl module of the same name.

%description -l pl.UTF-8
Biblioteka benchmark dostarcza funkcje do mierzenia i porównywania
czasu działania funkcji ocamlowych. Została zainspirowana modułem
Perla o tej samej nazwie.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/benchmark

dune install \
	--destdir $RPM_BUILD_ROOT

cat >>$RPM_BUILD_ROOT%{_libdir}/ocaml/benchmark/META <<EOF
directory="+benchmark"
EOF
ln -sr $RPM_BUILD_ROOT%{_libdir}/ocaml/benchmark/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/benchmark

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/benchmark/benchmark.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md src/benchmark.mli
%dir %{_libdir}/ocaml/benchmark
%{_libdir}/ocaml/benchmark/META
%{_libdir}/ocaml/benchmark/benchmark.cma
%{_libdir}/ocaml/benchmark/benchmark.cmi
%{_libdir}/ocaml/benchmark/benchmark.cmt
%{_libdir}/ocaml/benchmark/benchmark.cmti
%if %{with ocaml_opt}
%{_libdir}/ocaml/benchmark/benchmark.a
%{_libdir}/ocaml/benchmark/benchmark.cmx
%{_libdir}/ocaml/benchmark/benchmark.cmxa
%{_libdir}/ocaml/benchmark/benchmark.cmxs
%endif
%{_libdir}/ocaml/benchmark/dune-package
%{_libdir}/ocaml/benchmark/opam
%{_libdir}/ocaml/site-lib/benchmark
%{_examplesdir}/%{name}-%{version}
