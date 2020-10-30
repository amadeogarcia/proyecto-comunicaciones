option batch abort
option confirm off
open "comunicaciones-grupo2"
synchronize remote -filemask="*.html" "C:\Users\amade\Documents\GitHub\proyecto-comunicaciones\clima" "/home/grupo2/public_html/clima"
synchronize remote -filemask="*.html" "C:\Users\amade\Documents\GitHub\proyecto-comunicaciones\covid19\files" "/home/grupo2/public_html/covid19/files"
exit