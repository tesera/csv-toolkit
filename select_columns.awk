#!/usr/bin/awk -f
BEGIN {
    FS=","
    split(cols,out,",")
}
NR==1 {
    for (i=1; i<=NF; i++)
        ix[$i] = i
}
NR>=1 {
    for(i in out)
        printf "%s%s", $ix[out[i]], FS
    print ""
}
END {
    for (i in out) {
        print out[i]
    }
}
