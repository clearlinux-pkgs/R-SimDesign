#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-SimDesign
Version  : 2.17.1
Release  : 2
URL      : https://ftp.osuosl.org/pub/cran//src/contrib/SimDesign_2.17.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran//src/contrib/SimDesign_2.17.1.tar.gz
Summary  : Structure for Organizing Monte Carlo Simulation Designs
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-R.utils
Requires: R-RPushbullet
Requires: R-beepr
Requires: R-dplyr
Requires: R-future
Requires: R-future.apply
Requires: R-parallelly
Requires: R-pbapply
Requires: R-progressr
Requires: R-sessioninfo
Requires: R-snow
Requires: R-testthat
BuildRequires : R-R.utils
BuildRequires : R-RPushbullet
BuildRequires : R-beepr
BuildRequires : R-dplyr
BuildRequires : R-future
BuildRequires : R-future.apply
BuildRequires : R-parallelly
BuildRequires : R-pbapply
BuildRequires : R-progressr
BuildRequires : R-sessioninfo
BuildRequires : R-snow
BuildRequires : R-testthat
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Monte Carlo simulation experiments in R.
    The package controls the structure and back-end of Monte Carlo simulation experiments
    by utilizing a generate-analyse-summarise workflow. The workflow safeguards against 
    common simulation coding issues, such as automatically re-simulating non-convergent results, 
    prevents inadvertently overwriting simulation files, catches error and warning messages
    during execution, implicitly supports parallel processing with high-quality random number 
    generation, and provides tools for managing high-performance computing (HPC) array jobs
    submitted to schedulers such as SLURM. For a pedagogical introduction to the package see

%prep
%setup -q -n SimDesign

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732149889

%install
export SOURCE_DATE_EPOCH=1732149889
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SimDesign/CITATION
/usr/lib64/R/library/SimDesign/DESCRIPTION
/usr/lib64/R/library/SimDesign/INDEX
/usr/lib64/R/library/SimDesign/Meta/Rd.rds
/usr/lib64/R/library/SimDesign/Meta/data.rds
/usr/lib64/R/library/SimDesign/Meta/features.rds
/usr/lib64/R/library/SimDesign/Meta/hsearch.rds
/usr/lib64/R/library/SimDesign/Meta/links.rds
/usr/lib64/R/library/SimDesign/Meta/nsInfo.rds
/usr/lib64/R/library/SimDesign/Meta/package.rds
/usr/lib64/R/library/SimDesign/Meta/vignette.rds
/usr/lib64/R/library/SimDesign/NAMESPACE
/usr/lib64/R/library/SimDesign/NEWS.md
/usr/lib64/R/library/SimDesign/R/SimDesign
/usr/lib64/R/library/SimDesign/R/SimDesign.rdb
/usr/lib64/R/library/SimDesign/R/SimDesign.rdx
/usr/lib64/R/library/SimDesign/data/Rdata.rdb
/usr/lib64/R/library/SimDesign/data/Rdata.rds
/usr/lib64/R/library/SimDesign/data/Rdata.rdx
/usr/lib64/R/library/SimDesign/doc/Catch_errors.R
/usr/lib64/R/library/SimDesign/doc/Catch_errors.Rmd
/usr/lib64/R/library/SimDesign/doc/Catch_errors.html
/usr/lib64/R/library/SimDesign/doc/Fixed_obj_fun.R
/usr/lib64/R/library/SimDesign/doc/Fixed_obj_fun.Rmd
/usr/lib64/R/library/SimDesign/doc/Fixed_obj_fun.html
/usr/lib64/R/library/SimDesign/doc/HPC-computing.R
/usr/lib64/R/library/SimDesign/doc/HPC-computing.Rmd
/usr/lib64/R/library/SimDesign/doc/HPC-computing.html
/usr/lib64/R/library/SimDesign/doc/MultipleAnalyses.R
/usr/lib64/R/library/SimDesign/doc/MultipleAnalyses.Rmd
/usr/lib64/R/library/SimDesign/doc/MultipleAnalyses.html
/usr/lib64/R/library/SimDesign/doc/Parallel-computing.R
/usr/lib64/R/library/SimDesign/doc/Parallel-computing.Rmd
/usr/lib64/R/library/SimDesign/doc/Parallel-computing.html
/usr/lib64/R/library/SimDesign/doc/Saving-results.R
/usr/lib64/R/library/SimDesign/doc/Saving-results.Rmd
/usr/lib64/R/library/SimDesign/doc/Saving-results.html
/usr/lib64/R/library/SimDesign/doc/SimDesign-intro.R
/usr/lib64/R/library/SimDesign/doc/SimDesign-intro.Rmd
/usr/lib64/R/library/SimDesign/doc/SimDesign-intro.html
/usr/lib64/R/library/SimDesign/doc/index.html
/usr/lib64/R/library/SimDesign/help/AnIndex
/usr/lib64/R/library/SimDesign/help/SimDesign.rdb
/usr/lib64/R/library/SimDesign/help/SimDesign.rdx
/usr/lib64/R/library/SimDesign/help/aliases.rds
/usr/lib64/R/library/SimDesign/help/paths.rds
/usr/lib64/R/library/SimDesign/html/00Index.html
/usr/lib64/R/library/SimDesign/html/R.css
/usr/lib64/R/library/SimDesign/tests/tests/mpi/mpi.sh
/usr/lib64/R/library/SimDesign/tests/tests/mpi/simulation.R
/usr/lib64/R/library/SimDesign/tests/tests/mpi/slurm.slurm
/usr/lib64/R/library/SimDesign/tests/tests/mpi/slurm_par.slurm
/usr/lib64/R/library/SimDesign/tests/tests/mpi/slurm_test.R
/usr/lib64/R/library/SimDesign/tests/tests/mpi/slurm_test_par.R
/usr/lib64/R/library/SimDesign/tests/tests/test-01-core.R
/usr/lib64/R/library/SimDesign/tests/tests/test-02-aggregate.R
/usr/lib64/R/library/SimDesign/tests/tests/test-03-array.R
