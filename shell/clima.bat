httrack "wttr.in/Rosario?0Fp" -qiC2I0H0Qu1%n%s -*.png -*/adobe-fonts.github.io/* -O1 "C:\Users\amade\Documents\web-comunicaciones\.httrack"

:: -q   -> Do not ask questions;
:: -iC2 -> Update a mirror in the current directory;
:: -I0  -> Prevents the creation of an index of the sites mirrored;
:: -H0  -> Never abandon the download from a host to be abandoned;
:: -Q   -> Disables log files (not sure this works...);
:: -u1  -> Check all file types except directories;
:: -%n  -> Do not re-download locally erased files;
:: -%s  -> Various hacks to limit re-transfers when updating;
:: -O1  -> Output directory.
