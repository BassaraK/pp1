jezyki = ["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
wartosci = ["61","47","37","32","26","18","14","14","9","7"]

def rysujWykres(jezyki,wartosci):
    for i in range(len(jezyki)):
        if len(jezyki[i])<10:
            jezyki[i]=((10-len(jezyki[i]))*" ")+jezyki[i]
        print(jezyki[i]+":","#"*int(wartosci[i]),end="\n")
rysujWykres(jezyki,wartosci)