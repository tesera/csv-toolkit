#!/usr/bin/awk -f
function push(A,B) { A[length(A)+1] = B }
BEGIN {
    FS=","
    split(cols,patterns,",")
}
NR==1 {
    k=1
    for (i=1; i<=NF; i++)
    {
        for(p in patterns)
        {
            if($i ~ patterns[p] && !(i in selected))
            {
                k++
                selected[k] = i
            }
        }
    }
}
NR>=1 {
    for(i in selected)
        if(selected[i])
            printf "%s%s", $selected[i], (i==length(selected))?FS:""
    print ""
}
