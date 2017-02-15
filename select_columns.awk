#!/usr/bin/awk -f
function push(A,B) { A[length(A)+1] = B }
BEGIN {
    FS=","
}
NR==1 {
    for (i=1; i<=NF; i++)
        if($i ~ pattern)
            selected[i] = $i
}
NR>=1 {
    for(i in selected)
        printf "%s%s", $i, ","
    print ""
}
