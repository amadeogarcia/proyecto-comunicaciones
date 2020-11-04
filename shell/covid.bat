httrack -qgiC2I0H0Qu1%n%s "https://x-y.es/covid19/argentina.pais" -O1 "C:\Users\amade\Documents\web-comunicaciones\.httrack\x-y.es"
python3 "C:\Users\amade\Documents\GitHub\proyecto-comunicaciones\shell\separate.py"

:: -qg  -> Get the files indicated, do not seek other URLs;
:: -iC2 -> Update the mirror in the current directory;
:: -I0  -> Prevents the creation of an index of the sites mirrored;
:: -H0  -> Never abandon the download from a host to be abandoned;
:: -Q   -> Disables log files (not sure this works...);
:: -u1  -> Check all file types except directories;
:: -%n  -> Do not re-download locally erased files;
:: -%s  -> Various hacks to limit re-transfers when updating;
:: -O1  -> Output directory.