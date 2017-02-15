#!/usr/bin/awk -f
function push(A,B) { A[length(A)+1] = B }
BEGIN {
    FS=","
}
NR==1 {
    k=1
    for (i=1; i<=NF; i++)
    {
        if($i ~ pattern)
        {
            k++
            selected[k] = i
        }
    }
}
NR>=1 {
    for(i in selected)
        if(selected[i])
            printf "%s%s", $selected[i], (i==length(selected))?FS:""
    print ""
}
