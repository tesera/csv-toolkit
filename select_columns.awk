#!/usr/bin/awk -f
BEGIN {
    FS=","
    nout=split(cols,out,",")
}
NR==1 {
    for (i=1; i<=NF; i++)
        ix[$i] = i
}
NR>=1 {
    for(i=1; i<=nout; i++)
        printf "%s%s", $ix[out[i]], (i==nout)?"":FS
    print ""
}
