option batch abort
option confirm off
open "comunicaciones-grupo2"
synchronize remote -filemask="*.html" "C:\Users\amade\Documents\web-comunicaciones\.httrack\wttr.in" "/home/grupo2/public_html/clima"
synchronize remote -filemask="*.html" "C:\Users\amade\Documents\web-comunicaciones\covid19" "/home/grupo2/public_html/covid19"
exit